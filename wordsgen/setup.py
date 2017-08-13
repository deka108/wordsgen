from setuptools import setup


setup(
    name='wordsgen',
    version=0.1,
    py_modules=['wordsgen'],
    install_requires=[
        'click',
        'nltk',
        'six'
    ],
    entry_points='''
       [console_scripts]
       wordsgen=main:cli
   ''',
)