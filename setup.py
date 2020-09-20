"""
Color Thief
-----------

A module for grabbing the color palette from an image.

Links
`````

* `github <https://github.com/takase1121/color-thief-py>`_
* `development version
  <http://github.com/takase1121/color-thief-py/zipball/master#egg=color-thief-py-dev>`_

"""
from setuptools import setup


setup(
    name='colorthief',
    version='0.2.2',
    url='https://github.com/takase1121/color-thief-py',
    license='BSD',
    author='Takase',
    author_email='takase1121@gmail.com',
    description='A module for grabbing the color palette from an image.',
    long_description=__doc__,
    py_modules=['colorthief'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
