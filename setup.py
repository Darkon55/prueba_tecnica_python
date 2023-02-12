from setuptools import setup

setup(
    name='apiTest',
    version='0.1.0',
    py_modules=['apiTest'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        apiTest=apiTest:cli
    '''
)