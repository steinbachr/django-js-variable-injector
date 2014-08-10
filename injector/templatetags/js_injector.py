from django import template
from django.conf import settings
import re
import json
import pdb

register = template.Library()


class InjectionMapNode(template.Node):
    def __init__(self, django_variables):
        self.django_variables = django_variables
        # set the name of the JS map from the user's settings file or use the default
        self.map_name = getattr(settings, 'INJECTOR_MAP_NAME', 'djangovar_map')

    def _js_val_converter(self, val):
        """
        :param val: ``Any`` the value to get the equivalent Javascript value for
        :return: ``str`` the val converted to its proper javascript type
        """
        if type(val) is bool:
            return 'true' if val else 'false'
        elif type(val) is str:
            return "'{v}'".format(v=re.escape(val))
        elif type(val) is unicode:
            return "'{v}'".format(v=re.escape(str(val)))
        elif type(val) is int or type(val) is float:
            return val
        elif type(val) is list or type(val) is tuple:
            escaped = "["
            for v in val:
                escaped += "{val},".format(val=self._js_val_converter(v))
            escaped = escaped.rstrip(",")
            escaped += "]"
            return escaped
        elif type(val) is dict:
            escaped = "{"
            for k, v in val.items():
                escaped += "{k}:{v},".format(k=str(k), v=self._js_val_converter(v))
            escaped = escaped.rstrip(",")
            escaped += "}"
            return escaped
        elif isinstance(val, object):
            obj_fields = val.__dict__
            escaped = self._js_val_converter(obj_fields)
            return escaped
        else:
            return 'null'

    def _render_all_context(self, context):
        """
        when django_variables doesn't exist, we render everything in the context into the html
        """
        html = ''
        context_dicts = context.dicts
        for context_dict in context_dicts:
            for var_name, var_val in context_dict.items():
                try:
                    js_val = self._js_val_converter(var_val)
                except Exception:
                    js_val = 'null'
                html += "{var}: {var_val},".format(var=var_name, var_val=js_val)

        return html

    def _render_from_variables(self, context):
        """
        if django_variables does exist, we use this method to render the passed django variables into javascript
        variables
        """
        html = ''
        for var in self.django_variables:
            try:
                var_val = template.Variable(var).resolve(context)
                try:
                    js_val = self._js_val_converter(var_val)
                except Exception:
                    js_val = 'null'
                html += "{var}: {var_val},".format(var=var, var_val=js_val)
            except template.VariableDoesNotExist:
                html += "{var}: null,".format(var=var)

        return html

    def render(self, context):
        html = "<script>"
        html += "var %s = {" % self.map_name

        if self.django_variables:
            html += self._render_from_variables(context)
        else:
            html += self._render_all_context(context)

        html = html.rstrip(',')
        html += "};"
        html += "</script>"


        html += \
        """
        <script>
        djangovars = function(django_vars, func) {
            var inject = [];
            for (var i = 0 ; i < django_vars.length ; i++) {
                inject.push(%s[django_vars[i]]);
            }

            return func.apply(this, inject);
        };
        </script>
        """ % self.map_name

        return html

@register.tag(name="js_injector")
def js_injector(parser, token):
    try:
        token_contents = token.split_contents()
        tag_name, django_variables = token_contents[0], token_contents[1:]
    except ValueError:
        django_variables = []

    return InjectionMapNode(django_variables)