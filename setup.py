import re

from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


def read_description():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.rst'), 'rt') as fin:
        return fin.read()


def read_version():
    with open(path.join(here, 'argui', '__init__.py'), 'rt') as f:
        m = re.search(r"__version__\s*=\s*'(.*?)'", f.read(), re.M)
        return m.group(1)


setup(
    name='argui',

    version=read_version(),
    description='GUI for scripts using argparse',
    long_description=read_description(),

    keywords='argparse gui',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Desktop Environment',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Widget Sets'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    url='http://pypi.python.org/pypi/argui',

    author='Johann Goetz',
    author_email='theodore.goetz@gmail.com',

    license='GPL',

    packages=find_packages(),

    install_requires=[],

    extras_require={
        'test': ['wxPython', 'PyQt5'],
    },
)
