django-js-variable-injector
===========================

Provides a (more) elegant solution for injecting Django template variables into the context of an external Javascript file

=====
Installation
=====
1. ``pip install django-js-variable-injector``
2. add injector to ``INSTALLED_APPS``

=====
Usage
=====
Using the injector has two parts:
1. Load the template tag library
2. Wrap your javascript exectution in the djangovars function.

Of course, I will elaborate. We'll use the following as an example:

views.py:
````
def myview(request):
  return render(request, 'test.html', {
    'yo': 'a',
    'mr white': 1,
    'science': [1, 2, 3],
    'bitch': {
      'a': 1,
      'b': 2
    }
  })
````

test.html
````
{% load js_injector %}

<!DOCTYPE html>
<html>
<head>
  {% js_injector %}
  <script type="text/javascript" src="{{STATIC_URL}}injector_test.js"></script>
  (your scripts should be below the injector)
	<title></title>
</head>
<body>
	....
</body>
</html>
````

injector_test.js
````
djangovars(['yo', 'mr white', 'science', 'bitch'], function(y, m, s, b) {
    ... your logic here ...
});
````



=====
Known Bugs / Planned Improvements
=====
1. Add some type of handling for non-primitives
2. Error catching
3. More suggestions welcome!

