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

Extracting Color Palettes
=============


PaletteTools allows for two different ways to extract a color palette from an image.
The first of these two functions will return a string in the format of a text/css MIME type:

.. code-block:: python

    import palettetools as pt
    url = "https://assets.imgix.net/examples/bluehat.jpg"

    css_palette = pt.extract_colors_css(url)
    
    # Will return the following:
    #
    #.image-fg-1 { color:#0d0c10 !important; }
    #.image-bg-1 { background-color:#0d0c10 !important; }
    #.image-fg-2 { color:#015091 !important; }
    #.image-bg-2 { background-color:#015091 !important; }
    #.image-fg-3 { color:#0870d3 !important; }
    #.image-bg-3 { background-color:#0870d3 !important; }
    #.image-fg-4 { color:#239be0 !important; }
    #.image-bg-4 { background-color:#239be0 !important; }
    #.image-fg-5 { color:#b1dfeb !important; }
    #.image-bg-5 { background-color:#b1dfeb !important; }
    #.image-fg-6 { color:#f0c9b4 !important; }
    #.image-bg-6 { background-color:#f0c9b4 !important; }
    #.image-fg-ex-1 { color:#000000 !important; }
    #.image-bg-ex-1 { background-color:#000000 !important; }
    #.image-fg-ex-2 { color:#ffffff !important; }
    #.image-bg-ex-2 { background-color:#ffffff !important; }
    #.image-fg-vibrant { color:#0d95e4 !important; }
    #.image-bg-vibrant { background-color:#0d95e4 !important; }
    #.image-fg-muted-dark { color:#38445c !important; }
    #.image-bg-muted-dark { background-color:#38445c !important; }
    #.image-fg-muted { color:#966760 !important; }
    #.image-bg-muted { background-color:#966760 !important; }
    #.image-fg-vibrant-light { color:#72c5f4 !important; }
    #.image-bg-vibrant-light { background-color:#72c5f4 !important; }
    #.image-fg-muted-light { color:#d8b6aa !important; }
    #.image-bg-muted-light { background-color:#d8b6aa !important; }
    #.image-fg-vibrant-dark { color:#015091 !important; }
    #.image-bg-vibrant-dark { background-color:#015091 !important; }

This can be appended to a pre-existing CSS file through the following script:

.. code-block:: python

    >>> import palettetools as pt
    >>> url = "https://assets.imgix.net/examples/bluehat.jpg"
    >>> css = pt.extract_colors_css(url)
    >>> file = open("colors.css", 'w')
    >>> file.write(css)
    >>> file.close()

Color palettes can also be extracted as a JSON object through the following function. Also note that the object has 3 keys: **colors** , **average_luminance** , and **dominant_colors**

.. code-block:: python

    import palettetools as pt
    url = "https://assets.imgix.net/examples/bluehat.jpg"

    json_palette = pt.extract_colors_json(url)

    print json_palette

    # Will return the following:
    # {
    #   "colors": [
    #     {
    #       "red": 0.0509804,
    #       "hex": "#0d0c10",
    #       "blue": 0.0627451,
    #       "green": 0.0470588
    #     },
    #     {
    #       "red": 0.00392157,
    #       "hex": "#015091",
    #       "blue": 0.568627,
    #       "green": 0.313725
    #     },
    #     {
    #       "red": 0.0313725,
    #       "hex": "#0870d3",
    #       "blue": 0.827451,
    #       "green": 0.439216
    #     },
    #     {
    #       "red": 0.137255,
    #       "hex": "#239be0",
    #       "blue": 0.878431,
    #       "green": 0.607843
    #     },
    #     {
    #       "red": 0.694118,
    #       "hex": "#b1dfeb",
    #       "blue": 0.921569,
    #       "green": 0.87451
    #     },
    #     {
    #       "red": 0.941176,
    #       "hex": "#f0c9b4",
    #       "blue": 0.705882,
    #       "green": 0.788235
    #     }
    #   ],
    #   "average_luminance": 0.708396,
    #   "dominant_colors": {
    #     "vibrant": {
    #       "red": 0.0509804,
    #       "hex": "#0d95e4",
    #       "blue": 0.894118,
    #       "green": 0.584314
    #     },
    #     "muted_light": {
    #       "red": 0.847059,
    #       "hex": "#d8b6aa",
    #       "blue": 0.666667,
    #       "green": 0.713725
    #     },
    #     "muted": {
    #       "red": 0.588235,
    #       "hex": "#966760",
    #       "blue": 0.376471,
    #       "green": 0.403922
    #     },
    #     "vibrant_dark": {
    #       "red": 0.00392157,
    #       "hex": "#015091",
    #       "blue": 0.568627,
    #       "green": 0.313725
    #     },
    #     "vibrant_light": {
    #       "red": 0.447059,
    #       "hex": "#72c5f4",
    #       "blue": 0.956863,
    #       "green": 0.772549
    #     },
    #     "muted_dark": {
    #       "red": 0.219608,
    #       "hex": "#38445c",
    #       "blue": 0.360784,
    #       "green": 0.266667
    #     }
    #   }
    # }
  

Extracting Color Palettes
=============

PaletteTools can also give a suggested color for overlaid text on a specific image. The function will either return the hexadecimal value for **white** or **black** depending on which is more visible for the passed in image: 

.. code-block:: python

    import palettetools as pt
    url = "https://assets.imgix.net/examples/bluehat.jpg"

    color_suggested = pt.overlaid_text_color(url)

    print color_suggested
    
    # Will return:
    #
    # 000

Testing
===========

To run the all tests run::

    tox
