django-js-variable-injector
===========================

Provides a (more) elegant solution for injecting Django template variables into the context of an external Javascript file.

=====
Installation
=====
1. ``pip install django-js-variable-injector``
2. add ``injector`` to ``INSTALLED_APPS``

=====
Usage
=====
The injector can be used in one of two ways. Either you can explicitly define which django variables to inject into the Javascript namespace, or - if no variables are provided - the entire context will attempt to be injected.

Now, to actually use the injector you simply must:

1. Load the template tag library
2. Wrap your javascript execution in the djangovars function.

Of course, I will elaborate. We'll use the following as an example:

**views.py**
```python
def myview(request):
  return render(request, 'test.html', {
    'yo': 'a',
    'mr_white': 1,
    'science': [1, 2, 3],
    'bitch': {
      'a': 1,
      'b': 2
    }
  })
```


Now, we have two different ways that we can inject the variables. Here is the first:

**test.html**
```htmldjango
{% load js_injector %}

<!DOCTYPE html>
<html>
<head>
  {% js_injector %}
  <script type="text/javascript" src="{{STATIC_URL}}injector_test.js"></script> <-- (your scripts should be below the injector)
	<title></title>
</head>
<body>
	....
</body>
</html>
```
This would result in the entire contents of the context being added. 

The other (more granular) way is as follows:
**test.html**
```htmldjango
{% load js_injector %}

<!DOCTYPE html>
<html>
<head>
  {% js_injector yo mr_white science bitch %}
  <script type="text/javascript" src="{{STATIC_URL}}injector_test.js"></script> <-- (your scripts should be below the injector)
	<title></title>
</head>
<body>
	....
</body>
</html>
```
This would result in ONLY yo, mr_white, science, and bitch variables being injected. Regardless of which method you choose, the following Javascript is how you would inject the variables into a namespace.

**injector_test.js**
```htmldjango
djangovars(['yo', 'mr_white', 'science', 'bitch'], function(y, m, s, b) {
    ... your logic here ...
});
```

Omitting variables is also valid, i.e.:

**test.html**
```htmldjango
{% load js_injector %}

<!DOCTYPE html>
<html>
<head>
  {% js_injector yo bitch %}
  <script type="text/javascript" src="{{STATIC_URL}}injector_test.js"></script> <-- (your scripts should be below the injector)
	<title></title>
</head>
<body>
	....
</body>
</html>
```

=====
Configuration
=====
In ``settings.py`` the following configuration variables are available:

* ``INJECTOR_MAP_NAME`` - The injector introduces a JS variable into the global namespace which *could* conceivably conflict with another name (by default, this variable is called ``djangovars_map``). To override this name, set this variable to a different value.


=====
Known Bugs / Planned Improvements
=====
1. Error catching
2. More suggestions welcome!


===
If you like the injector and are using it, please star and/or fork :)

