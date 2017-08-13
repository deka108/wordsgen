from setuptools import setup

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='wordsgen',
    version=0.1,
    description='wordsgen - A collections of utilities for generating words',
    long_description=long_description,
    py_modules=['wordsgen'],
    author='deka',
    author_email='deka108@gmail.com',
    install_requires=[
        'click>=6',
        'nltk>=3.2',
        'six>=1.10'
    ],
    packages=['wordsgen'],
    entry_points='''
       [console_scripts]
       wordsgen=main:cli
       ''',
)