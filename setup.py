from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='RZA',
      version=version,
      description="Riak + ZODB Alright?",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='whit',
      author_email='whit at nocoast.us',
      url='http://whitmorriss.org',
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
