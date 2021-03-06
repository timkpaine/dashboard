from setuptools import setup, find_packages
from codecs import open
import io
import os
import os.path

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
name = 'workspaces'


def get_version(file, name='__version__'):
    path = os.path.realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]

version = get_version(pjoin(here, 'dashboard', '_version.py'))

with open(pjoin(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(pjoin(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.read().split()

setup(
    name=name,
    version=version,
    description='Dashboards',
    long_description=long_description,
    url='https://github.com/timkpaine/dashboard',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='dashboards',
    packages=find_packages(exclude=[]),
    install_requires=requires,
    extras_require={'dev': requires + ['pytest', 'pytest-cov', 'pylint', 'flake8']}
)
