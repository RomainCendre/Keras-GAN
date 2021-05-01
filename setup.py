  from setuptools import setup
from setuptools import find_packages


version = '0.1'

setup(name='keras-gan',
      version=version,
      url='https://github.com/eriklindernoren/Keras-GAN',
      license='MIT',
      install_requires=['keras'],
      include_package_data=True,
      packages=find_packages())
