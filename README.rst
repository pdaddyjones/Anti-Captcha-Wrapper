Anti Captcha Wrapper
==============

.. image:: https://img.shields.io/pypi/v/captcha_solver.svg
    :target: https://pypi.python.org/pypi/captcha_solver
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

"A simple lib connection for solve captchas with anticaptchaofficial",

Usage
-----

.. code-block:: python

   from captcha_solver import CaptchaSolver
   solver = CaptchaSolver("YOUR API KEY")
   solver.resolve("YOUR CAPTCHA IMAGE")


Installation
------------

.. code-block:: python

   pip install -e .

Requirements
^^^^^^^^^^^^

.. code-block:: python

  anticaptchaofficial

  behave

Compatibility
-------------

python 3.6

Licence
-------
MIT

Authors
-------

`anti_captcha_wrapper` was written by `anti_captcha_wrapper <pdaddyjonesthethird@gmail.com>`_.
