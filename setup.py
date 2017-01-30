from setuptools import setup


setup(
    name='simplejson_objects',
    version='0.0.3',
    description='Objects serialization extension for simplejson',
    py_modules=['simplejson_objects'],
    zip_safe=False,
    install_requires=['simplejson'],
    url='https://github.com/CrytekKiev/simplejson_objects',
    download_url='https://github.com/CrytekKiev/simplejson_objects/archive/0.0.3.tar.gz',
    entry_points={
        'kombu.serializers': [
            'simplejson_objects = simplejson_objects:register_args'
        ]
    }
)
