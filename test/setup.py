from setuptools import setup, find_packages

version = '0.0'

setup(
    name='testsidegself',
    version=version,
    description="Tests for selenium-ide-gocept-selenium-format.",
    author='Michael Howitz',
    author_email='mh@gocept.com',
    url='',
    license='Apache License, Version 2.0',
    include_package_data=True,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    zip_safe=False,
    install_requires=[],
    )
