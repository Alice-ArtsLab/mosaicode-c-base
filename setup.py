# -*- coding: utf-8 -*-

from glob import glob

DISTUTILS_DEBUG = "True"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(name='mosaicode-lib-c-base',
    #install_requires=['mosaicode'],
    python_requires='>=2.7',
    tests_require=[],
    test_suite='',
    version='0.1.0.dev',
    packages=find_packages(exclude=["tests.*", "tests"]),
    scripts=[],
    description='Base extension for C extensions',
    author='ALICE: Arts Lab in Interfaces, Computers, and Experiences',
    author_email='mosaicode-dev@googlegroups.com',
    maintainer="ALICE: Arts Lab in Interfaces, Computers, and Experiences",
    maintainer_email="mosaicode-dev@googlegroups.com",
    license="GNU GPL3",
    url='https://github.com/Alice-ArtsLab',
#    data_files=[
#        ('/usr/share/mosaicode/extensions/examples/c/base',
#        glob("examples/*"))
#        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: C',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Code Generators',
        ],
    )
