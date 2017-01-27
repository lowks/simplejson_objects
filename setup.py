from setuptools import setup


setup(
    name='simplejson_objects',
    version='0.0.1',
    packages=['simplejson_objects'],
    zip_safe=False,
    install_requires=['simplejson'],
    entry_points={
        'kombu.serializers': [
            'simplejson_objects = simplejson_objects:register_args'
        ]
    }
)
