# content of setup.py
from setuptools import setup, find_packages

setup(
    name='library-manager-ahmadreza',
    version='0.1.0',
    packages=find_packages(),
    description='A basic library system to manage books written in Python.',
    author='Ahmadreza Haj Talebi',
    url='https://github.com/ahmadreza-hajtalebi/maktabkhooneh_python_assignments',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', # (۹) این خط رو دست نزن، میگه حداقل پایتون 3.6 میخواد
)