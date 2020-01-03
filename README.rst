=======
Purpose
=======

Formatter for `Selenium IDE`_ which produces `gocept.selenium`_ compatible code.
(Code originally based on python-format from Selenium IDE.)

=====
Usage
=====

Install it in Firefox as Add-on, it provides a new export and clipboard
formatter for `Selenium IDE`.

===========
Development
===========

How to work on this package is described in HACKING.rst.


.. _`gocept.selenium` : http://pypi.python.org/pypi/gocept.selenium
.. _`Selenium IDE` : http://seleniumhq.org/download/


=========
Reasoning
=========

The default python-format plug-in creates PEP-8-ified varients of the
commands (underscores instead of camel case) used in the Selenium test.

gocept.selenium supports to use the same commands as defined in the
[[http://release.seleniumhq.org/selenium-core/1.0/reference.html|Selenium-API]]
(including assertions).

selenium-ide-gocept-selenium-format formats the Selenium test to be runnable
using gocept.selenium without the need to manually convert the code back.
