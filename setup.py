from setuptools import setup

setup(
   name='jikanpy',
   version='1.0.0',
   description='Python wrapper for the Jikan API',
   author='Andrew Conant',
   packages=['jikanpy'],
   install_requires=['requests', 'aiohttp'],
)