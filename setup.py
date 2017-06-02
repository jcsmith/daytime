from setuptools import setup

setup(
    name='daytime',
    packages=['daytime'],
    include_package_data=True,
    install_requires=[
        'flask',
	'pyephem'
    ],
)
