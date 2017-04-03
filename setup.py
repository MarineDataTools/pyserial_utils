from setuptools import setup
import os

ROOT_DIR='pyserial_utils'
with open(os.path.join(ROOT_DIR, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(name='pyserial_utils',
      version=version,
      description='A set of utilities based on pyserial to identify usable serial ports and to check, create and delete lock files in linux systems.',
      url='https://github.com/MarineDataTools/pyserial_utils',
      author='Peter Holtermann',
      author_email='peter.holtermann@io-warnemuende.de',
      license='MIT',
      packages=['pyserial_utils'],
      scripts = [],
      entry_points={},
      package_data = {'':['VERSION']},
      zip_safe=False)
