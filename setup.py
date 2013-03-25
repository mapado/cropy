import re
import os

from setuptools import setup, find_packages
from os.path import join, dirname


version = re.search("__version__ = '([^']+)'", open(
    os.path.join(os.path.dirname(__file__), 'aptcrop', '__init__.py')
).read().strip()).group(1)


setup(
    name='aptcrop',
    version=version,
    author='Jerry Nieuviarts',
    author_email='jerry@mapado.com',
    url='https://github.com/mapado/apt-crop-content-based-image-crop',
    packages=find_packages(),
    install_requires=['numpy>=0.8.0', 'scipy>=0.11.0', 'scikit-image>=0.8.2', 'PIL>=1.1.7'],
    scripts=['aptcrop/aptcrop'],
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
