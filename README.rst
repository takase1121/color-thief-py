Color Thief
===========

A Python module for grabbing the color palette from an image.
This is suited for ``python-mss`` ``Screenshot`` object

Installation
------------

::

    $ pip install pip install https://github.com/takase1121/color-thief-py/archive/master.zip

Usage
-----

.. code:: python
    import mss
    from colorthief import ColorThief

    with mss.mss() as screen:
        screenshot = mss.grab(mss.monitors[0])
        color_thief = ColorThief(screenshot)
        # get dominant color
        dominant_color = color_thief.get_color(quality=1)
        # build a color palette
        palette = color_thief.get_palette(color_count=6)

API
---

.. code:: python

    class ColorThief(object):
        def __init__(self, screenshot):
            """Create one color thief for one image.

            :param screenshot: A screenshot object from python-mss
            """
            pass

        def get_color(self, quality=10):
            """Get the dominant color.

            :param quality: quality settings, 1 is the highest quality, the bigger
                            the number, the faster a color will be returned but
                            the greater the likelihood that it will not be the
                            visually most dominant color
            :return tuple: (r, g, b)
            """
            pass

        def get_palette(self, color_count=10, quality=10):
            """Build a color palette.  We are using the median cut algorithm to
            cluster similar colors.

            :param color_count: the size of the palette, max number of colors
            :param quality: quality settings, 1 is the highest quality, the bigger
                            the number, the faster the palette generation, but the
                            greater the likelihood that colors will be missed.
            :return list: a list of tuple in the form (r, g, b)
            """
            pass

Thanks
------

Thanks to Lokesh Dhakar for his `original work
<https://github.com/lokesh/color-thief/>`_
and `Shipeng Feng's fork
<https://github.com/fengsp/color-thief-py/>`_

Better
------

If you feel anything wrong, feedbacks or pull requests are welcome.
