   
from setuptools import setup

setup(name='mypackage',
      version='1.0',
      description='My super cool package',
      url='https://github.com/my_name/my_package',
      packages=['mypackage'],
      python_requieres='3.9',
      install_requires=[
            'some_package==1.0.0'
      ])