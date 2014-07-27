from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='django-js-variable-injector',
      version=version,
      description="A (more) elegant solution for injecting Django template variables into the context of an external Javascript file",
      long_description="""\
A (more) elegant solution for injecting Django template variables into the context of an external Javascript file""",
      classifiers=['Development Status :: 3 - Alpha'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django js injection template variables',
      author='Bobby Steinbach',
      author_email='steinbach.rj@gmail.com',
      url='https://github.com/steinbachr/django-js-variable-injector',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )