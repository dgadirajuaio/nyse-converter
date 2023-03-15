from setuptools import setup

setup(
    name='nyseconverter',
    version='0.1',
    description='NYSE Converter',
    url='https://github.com/dgadirajuaio/nyse-converter',
    author='Durga Gadiraju',
    author_email='dgadiraju@itversity.com',
    license='MIT',
    packages=['nyseconverter'],
    zip_safe=False,
    install_requires=[
        'dask[complete]<=2023.3.0',
    ],
    entry_points={
        'console_scripts': ['nysec=nyseconverter:main'],
    }
)
