========
Overview
========


.. |travis| image:: https://travis-ci.org/sherwinski/palette-tools.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/sherwinski/palette-tools

.. |version| image:: https://img.shields.io/pypi/v/palettetools.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/palettetools


A Python library for extracting and analyzing color palettes from images.
All images must be served through Imgix, more information can be found at http://www.imgix.com.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install palettetools

Documentation
=============


To use the project:

.. code-block:: python

    import palettetools as pt
    url = "https://assets.imgix.net/examples/bluehat.jpg"

    print pt.extract_colors_css(url)
    print pt.extract_colors_json(url)
    print pt.overlaid_text_color(url)

Testing
===========

To run the all tests run::

    tox
