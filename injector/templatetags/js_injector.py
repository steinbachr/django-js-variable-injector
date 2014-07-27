import datetime
from django import template
import json
import pdb

register = template.Library()


class InjectionMapNode(template.Node):
    def __init__(self):
        pass

    def _js_val_converter(self, val):
        """
        :param val: ``Any`` the value to get the equivalent Javascript value for
        :return: ``str`` the val converted to its proper javascript type
        """
        if type(val) is bool:
            return 'true' if val else 'false'
        elif type(val) is str:
            return "'{v}'".format(v=val)
        elif val is None:
            return 'null'
        else:
            return val

    def render(self, context):
        html = "<script>"
        html += "var djangovar_map = {"

        view_variables = context.dicts[-1]
        for var_name, var_val in view_variables.items():
            html += "{var}: {var_val},".format(var=var_name, var_val=self._js_val_converter(var_val))

        html = html.rstrip(',')
        html += "};"
        html += "</script>"


        html += \
        """
        <script>
        djangovars = function(django_vars, func) {
            var inject = [];
            for (var i = 0 ; i < django_vars.length ; i++) {
                inject.push(djangovar_map[django_vars[i]]);
            }

            return func.apply(this, inject);
        };
        </script>
        """

        return html

@register.tag(name="js_injector")
def js_injector(parser, token):
    return InjectionMapNode()