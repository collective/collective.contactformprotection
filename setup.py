"""Installer for the collective.contactformprotection package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.contactformprotection",
    version="1.0a1",
    description="This package protects the default contact form of Plone which is generally accessible via /contact-form. We add a (H/Re)captcha field depending on your installation and provide a checkbox in the controlpanel to disable it globally.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Peter Mathis",
    author_email="peter.mathis@kombinat.at",
    url="https://github.com/collective/collective.contactformprotection",
    project_urls={
        "PyPI": "https://pypi.org/project/collective.contactformprotection/",
        "Source": "https://github.com/collective/collective.contactformprotection",
        "Tracker": "https://github.com/collective/collective.contactformprotection/issues",
        # 'Documentation': 'https://collective.contactformprotection.readthedocs.io/en/latest/',
    },
    license="GPL version 3",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "z3c.jbot",
        "plone.api>=1.8.4",
        "plone.app.dexterity",
    ],
    extras_require={
        "recaptcha": [
            "plone.formwidget.recaptcha",
        ],
        "hcaptcha": [
            "plone.formwidget.hcaptcha",
        ],
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
