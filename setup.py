import re
import os

from setuptools import setup, find_packages
from os.path import join, dirname


version = re.search("__version__ = '([^']+)'", open(
    os.path.join(os.path.dirname(__file__), 'cropy', '__init__.py')
).read().strip()).group(1)


setup(
    name='cropy',
    version=version,
    author='Jerry Nieuviarts',
    author_email='jerry@mapado.com',
    url='https://github.com/mapado/cropy',
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'scikit-image', 'Pillow'],
    scripts=['cropy/cropy'],
    description='Command line tool and module to crop an image to a specific resolution removing less important parts first',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    zip_safe=False,
    license='FreeBSD',
    classifiers=[
           'Development Status :: 3 - Alpha',
           'Environment :: Console',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: BSD License',
           'Natural Language :: English',
           'Operating System :: POSIX :: Linux',
           'Operating System :: Unix',
           'Operating System :: MacOS :: MacOS X',
           'Programming Language :: Python :: 2.6',
           'Programming Language :: Python :: 2.7',
           'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords=['image', 'crop', 'entropy', 'autocrop', 'resize']
)
