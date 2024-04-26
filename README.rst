.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.contactformprotection/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.contactformprotection/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.contactformprotection/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.contactformprotection?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.contactformprotection/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.contactformprotection

.. image:: https://img.shields.io/pypi/v/collective.contactformprotection.svg
    :target: https://pypi.python.org/pypi/collective.contactformprotection/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.contactformprotection.svg
    :target: https://pypi.python.org/pypi/collective.contactformprotection
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.contactformprotection.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.contactformprotection.svg
    :target: https://pypi.python.org/pypi/collective.contactformprotection/
    :alt: License


================================
collective.contactformprotection
================================

This package protects the default contact form of Plone which is generally accessible via `/contact-info`.

Features
--------

- Add a (H/Re)captcha field depending on the installed 3rd party addon. This can be installed as `extra_require` optionally.
  In case both are installed, you can choose whichone you want in the controlpanel.

```
eggs =
    collective.contactformprotection[hcaptcha,recaptcha]
```

- Provide a checkbox in the controlpanel to disable the form globally


Documentation
-------------

The features mentioned above are all set in the configuration registry. See `plone.app.registry` how to set these
values TTW or in a package profile.


Installation
------------

Install collective.contactformprotection by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.contactformprotection


and then running ``bin/buildout``


Authors
-------

Peter Mathis, petschki



Contribute
----------

- Issue Tracker: https://github.com/collective/collective.contactformprotection/issues
- Source Code/Documentation: https://github.com/collective/collective.contactformprotection


License
-------

The project is licensed under the GPLv3.
