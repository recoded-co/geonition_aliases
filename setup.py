from setuptools import setup
from setuptools import find_packages

setup(
    name='geonition_aliases',
    version='0.0.1',
    author='Dariusz Walczak',
    url='',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "geoforms": [
            "templates/*.html",
            "templates/*.api.js",
            "templates/jstranslations.txt",
            "templates/help/*.html",
            "templates/admin/geoforms/geoformelement/*.html",
            "locale/*/LC_MESSAGES/*.po",
            "locale/*/LC_MESSAGES/*.mo",
            "static/js/*",
            "static/css/*.css",
            "static/css/images/*.png"
        ],
    },
    zip_safe=False,
    install_requires=['django',
                      'django-modeltranslation'],
)
