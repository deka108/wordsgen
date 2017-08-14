from setuptools import setup, find_packages

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='wordsgen',
    version=0.1,
    description='wordsgen - A collections of utilities for generating words',
    long_description=long_description,
    author='deka',
    author_email='deka108@gmail.com',
    install_requires=[
        'click>=6',
        'nltk>=3.2',
        'six>=1.10'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
       [console_scripts]
       wordsgen=wordsgen.main:cli
       ''',
)