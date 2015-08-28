vcrpy-unittest
==============

|Build Status|

This package provides ``VCRTestCase`` for simple integration between
`VCR.py`_ and Python's venerable unittest_.

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
``_get_vcr_kwargs``, ``_get_cassette_library_dir`` and ``_get_cassette_name``. See
`the source <vcr_unittest/testcase.py>`__ for the default implementations, and
`VCR.py`_ for more information.

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
<LICENSE.txt>`__ for more details.

Acknowledgements
----------------

Thanks to @kevin1024 for `VCR.py`_, and to @IvanMalison for his constructive
critique on this package. Also thanks to @nedbat for his `post regarding
unittest and context managers
<http://nedbatchelder.com/blog/201508/using_context_managers_in_test_setup.html>`__,
and to @davepeck for `httreplay <https://github.com/davepeck/httreplay>`__ which
served me well for so long.

.. _VCR.py: https://github.com/kevin1024/vcrpy
.. _unittest: https://docs.python.org/2/library/unittest.html
.. |Build Status| image:: https://travis-ci.org/agriffis/vcrpy-unittest.svg?branch=master
   :target: https://travis-ci.org/agriffis/vcrpy-unittest
