import setuptools

__package__ = 'search_location_api'

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name=__package__,
    version='0.1.0',
    description='Mapbox search api framework',
    url='***',
    author='Prasad',
    zip_safe=False,
    package_dir={__package__: __package__},
    packages=[__package__],
    install_requires=required,
)
