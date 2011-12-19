Purpose
=======

Formatter for `Selenium IDE`_ which produces `gocept.selenium`_ compatible code.

Create xpi file
===============

To create an installer file run::

  python make.py


Testing the formatter itself
============================

Set up
------

* ``cd`` to the `test` directory.
* Run::

  python2.7 bootstrap.py
  bin/buildout

Test run
--------

* To produce a the test cases in `testcase.html` in the `parts` directory run::

  bin/extract-commands

* Open a Firefox browser where `Selenium IDE`_ is installed.
* Create an xpi file of the package (see above) and install it in Firefox.
* Open `testcase.html` in `Selenium IDE` and export it for `gocept.selenium`
  (File -> Export Test Case As... -> Python 2 (gocept.selenium)), name the
  exported file ``testcase.py`` and save it in the `parts` directory.
* Run the comparer::

  bin/compare-result

* It should not show any errors.




.. _`gocept.selenium` : http://pypi.python.org/pypi/gocept.selenium
.. _`Selenium IDE` : http://seleniumhq.org/download/