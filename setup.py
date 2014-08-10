from setuptools import setup, find_packages
import sys, os


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = '1.1.1'

setup(name='django-js-variable-injector',
      version=version,
      description="A (more) elegant solution for injecting Django template variables into the context of an external Javascript file",
      long_description="""\
A (more) elegant solution for injecting Django template variables into the context of an external Javascript file""",
      classifiers=['Development Status :: 4 - Beta'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django js injection template variables',
      author='Bobby Steinbach',
      author_email='steinbach.rj@gmail.com',
      url='https://github.com/steinbachr/django-js-variable-injector',
      license='MIT',
      packages=get_packages('injector'),
      package_data=get_package_data('injector'),
      include_package_data=True,
      zip_safe=False
      )