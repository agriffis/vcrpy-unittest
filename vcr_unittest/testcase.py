from __future__ import absolute_import, unicode_literals

import inspect
import logging
import os
import unittest
import vcr


logger = logging.getLogger(__name__)


class VCRTestCase(unittest.TestCase):
    vcr_enabled = True

    def setUp(self):
        super(VCRTestCase, self).setUp()
        if self.vcr_enabled:
            kwargs = self._get_vcr_kwargs()
            if 'cassette_library_dir' not in kwargs:
                kwargs['cassette_library_dir'] = self._get_cassette_library_dir()
            myvcr = vcr.VCR(**kwargs)
            cm = myvcr.use_cassette(self._get_cassette_name())
            self.cassette = cm.__enter__()
            self.addCleanup(cm.__exit__, None, None, None)

    def _get_vcr_kwargs(self, **kwargs):
        return kwargs

    def _get_cassette_library_dir(self):
        testdir = os.path.dirname(inspect.getfile(self.__class__))
        return os.path.join(testdir, 'cassettes')

    def _get_cassette_name(self):
        return '{0}.{1}.yaml'.format(self.__class__.__name__,
                                     self._testMethodName)
