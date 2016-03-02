vcrpy-unittest
==============

|Build Status| |Coverage Report| |PyPI| |Gitter|

This package provides ``VCRTestCase`` for simple integration between
`VCR.py`_ and Python's venerable unittest_.

Installation
------------

Install from PyPI_:

.. code:: sh

   pip install vcrpy-unittest

Usage
-----

Inherit from ``VCRTestCase`` for automatic recording and playback of HTTP
interactions.

.. code:: python

   from vcr_unittest import VCRTestCase
   import requests

   class MyTestCase(VCRTestCase):
       def test_something(self):
           response = requests.get('http://example.com')

Similar to how VCR.py returns the cassette from the context manager,
``VCRTestCase`` makes the cassette available as ``self.cassette``:

.. code:: python

    self.assertEqual(len(self.cassette), 1)
    self.assertEqual(self.cassette.requests[0].uri, 'http://example.com')

By default cassettes will be placed in the ``cassettes`` subdirectory next to the
test, named according to the test class and method. For example, the above test
would read from and write to ``cassettes/MyTestCase.test_something.yaml``

The configuration can be modified by overriding methods on your subclass:
``_get_vcr_kwargs``, ``_get_cassette_library_dir`` and ``_get_cassette_name``.
To modify the ``VCR`` object after instantiation, for example to add a matcher,
you can hook on ``_get_vcr``, for example:

.. code:: python

    class MyTestCase(VCRTestCase):
        def _get_vcr(self, **kwargs):
            myvcr = super(MyTestCase, self)._get_vcr(**kwargs)
            myvcr.register_matcher('mymatcher', mymatcher)
            myvcr.match_on = ['mymatcher']
            return myvcr

See
`the source
<https://github.com/agriffis/vcrpy-unittest/blob/master/vcr_unittest/testcase.py>`__
for the default implementations of these methods, and `VCR.py`_ for more
information.


Compatibility
-------------

``VCRTestCase`` supports a subset of the Python versions supported by VCR.py.
Specifically Python 2.6 is excluded, because it lacks ``TestCase.addCleanup``.
Adding support for Python 2.6 would be pretty easy with ``tearDown`` but that
implementation is fragile because it depends on nothing else going wrong in the
inheritance chain. Rather than take on this additional complexity, Python 2.6 is
simply excluded for now.

License
-------

This library uses the MIT license, which is the same as VCR.py. See `LICENSE.txt
<https://github.com/agriffis/vcrpy-unittest/blob/master/LICENSE.txt>`__ for more
details.

Acknowledgements
----------------

Thanks to `@kevin1024`_ for `VCR.py`_, and to `@IvanMalison`_ for his
constructive critique on this package. Also thanks to `@nedbat`_ for his `post
regarding unittest and context managers
<http://nedbatchelder.com/blog/201508/using_context_managers_in_test_setup.html>`__,
and to `@davepeck`_ for `httreplay <https://github.com/davepeck/httreplay>`__
which served me well for so long.

.. _PyPI: https://pypi.python.org/pypi/vcrpy-unittest
.. _VCR.py: https://github.com/kevin1024/vcrpy
.. _unittest: https://docs.python.org/2/library/unittest.html

.. _@kevin1024: https://github.com/kevin1024
.. _@IvanMalison: https://github.com/IvanMalison
.. _@nedbat: https://github.com/nedbat
.. _@davepeck: https://github.com/davepeck

.. |Build Status| image:: https://img.shields.io/travis/agriffis/vcrpy-unittest/master.svg?style=plastic
   :target: https://travis-ci.org/agriffis/vcrpy-unittest?branch=master
.. |Coverage Report| image:: https://img.shields.io/coveralls/agriffis/vcrpy-unittest/master.svg?style=plastic
   :target: https://coveralls.io/github/agriffis/vcrpy-unittest?branch=master
.. |PyPI| image:: https://img.shields.io/pypi/v/vcrpy-unittest.svg?style=plastic
   :target: PyPI_
.. |Gitter| image:: https://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-green.svg?style=plastic
   :target: https://gitter.im/kevin1024/vcrpy
