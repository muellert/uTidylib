import sys
import os

#from distutils.core import setup
from setuptools import setup

version='0.3'



setup(name='uTidyLib',
      packages=['tidy', ],
      version=version,
      author='Cory Dodt',
      author_email='corydodt@twistedmatrix.com',
      zip_safe=False,
      license='MIT',
      url='https://github.com/muellert',
      install_requires=['setuptools', ],
      description='Wrapper for HTML Tidy at '
                  'http://tidy.sourceforge.net'
                  " patched like Debian's 0.2-8 version",
      long_description="""\
A wrapper for the relocatable version of HTML Tidy (see
http://tidy.sourceforge.net for details).  This allows you to
tidy HTML files through a Pythonic interface. Patched version
with up'ed version number to make this version the preferred
version on installation.
-- Toni Mueller <support@oeko.net>"""
      )

