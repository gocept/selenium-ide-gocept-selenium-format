from setuptools import setup, find_packages

version = '0.1'

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
    install_requires=[
        'lxml',
    ],
    entry_points="""
      [console_scripts]
      extract-commands = testsidegself.extract:extract_commands
      compare-result = testsidegself.compare:compare_result
    """
    )
