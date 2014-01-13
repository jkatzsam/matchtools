from setuptools import setup, find_packages
readme = open('README.txt').read()
setup(
	name='matchlib',
	version='0.1',
    author='Russell J. Funk and Julian Katz-Samuels',
	author_email='funk@umich.edu',
    license='',
    description='Package that provides data-cleaning tools.',
    long_description=open('README.txt').read(),
    packages=['matchlib'],
      )