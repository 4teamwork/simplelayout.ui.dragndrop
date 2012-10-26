from setuptools import setup, find_packages
import os

version = '3.0b3.dev0'

setup(name='simplelayout.ui.dragndrop',
      version=version,
      description="simplelayout drag and drop support",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],

      keywords='',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/simplelayout.ui.dragndrop',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['simplelayout', 'simplelayout.ui'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'collective.js.jqueryui',
        ],

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
