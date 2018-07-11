"""Setup for recap XBlock."""

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
    name='recap-xblock',
    version='0.3.3',
    description='Recap XBlock',   # TODO: write a better description.
    license='UNKNOWN',          # TODO: choose a license: 'AGPL v3' and 'Apache 2.0' are popular.
    packages=[
        'recap',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils',
        'xhtml2pdf'
    ],
    entry_points={
        'xblock.v1': [
            'recap = recap:RecapXBlock',
        ]
    },
    package_data=package_data("recap", ["static", "public"]),
)
