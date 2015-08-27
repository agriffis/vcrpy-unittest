from __future__ import absolute_import, unicode_literals

import inspect
import logging
import os
import unittest
import vcr


logger = logging.getLogger(__name__)


class VCRTestCase(unittest.TestCase):
    vcr_enabled = True

    def __init__(self, *args, **kwargs):
        super(VCRTestCase, self).__init__(*args, **kwargs)
        self.__context_manager = None

    def setUp(self):
        super(VCRTestCase, self).setUp()
        if self.vcr_enabled:
            self._start_vcr()

    def tearDown(self):
        if self.__context_manager:
            self._stop_vcr()
        super(VCRTestCase, self).tearDown()

    def run(self, *args, **kwargs):
        try:
            return super(VCRTestCase, self).run(*args, **kwargs)
        finally:
            try:
                assert not self.__context_manager, "VCR still running!"
            except AssertionError:
                self._stop_vcr()
                raise

    def _start_vcr(self):
        assert not self.__context_manager, "VCR already started."
        myvcr = vcr.VCR(**self._get_vcr_kwargs())
        name = self._get_cassette_name()
        self.__context_manager = myvcr.use_cassette(name)
        self.cassette = self.__context_manager.__enter__()

    def _stop_vcr(self):
        assert self.__context_manager, "VCR already stopped."
        try:
            self.__context_manager.__exit__(None, None, None)
        finally:
            self.__context_manager = None

    def _get_vcr_kwargs(self):
        return dict(
            match_on=['method', 'uri', 'headers', 'raw_body'],
            filter_headers=['authorization'],
            cassette_library_dir=self._get_cassette_library_dir(),
        )

    def _get_cassette_library_dir(self):
        testdir = os.path.dirname(inspect.getfile(self.__class__))
        return os.path.join(testdir, 'cassettes')

    def _get_cassette_name(self):
        return '{0}.{1}'.format(self.__class__.__name__,
                                self._testMethodName)
