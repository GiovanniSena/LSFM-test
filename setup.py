import os, io
from setuptools import setup, find_packages

setup(
    name='lightroot',
    version='0.1',
    author='s.amarteifio14@imperial.ac.uk',
    author_email='s.amarteifio14@imperial.ac.uk',
    license='MIT',
    url='git@https://github.com/GiovanniSena/LSFM_CYCB_analysis_v2',
    keywords='root microscopy tracking fuzzy registration',
    description='lightroot is an image processing pipeline for preprocessing lightsheet microscopy data and tracking transient fluorescent events in structured point clouds',
    long_description=('lightroot is an image processing pipeline for preprocessing lightsheet microscopy data and tracking transient fluorescent events in structured point clouds'),
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'lightroot = lightroot.__main__:main'
            ],
    },
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Computer Vision',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)

