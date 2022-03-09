"""Setup for modelo_de_aprendizaje_bandler_y_grinder XBlock."""


import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='modelo_de_aprendizaje_bandler_y_grinder-xblock',
    version='0.1',
    description='modelo_de_aprendizaje_bandler_y_grinder XBlock',   # TODO: write a better description.
    license='UNKNOWN',          # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        'modelo_de_aprendizaje_bandler_y_grinder',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'modelo_de_aprendizaje_bandler_y_grinder = modelo_de_aprendizaje_bandler_y_grinder:MOdeloAprendizajeXBlock',
        ]
    },
    package_data=package_data("modelo_de_aprendizaje_bandler_y_grinder", ["static", "public"]),
)
