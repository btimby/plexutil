import unittest
import mock

from plexutil.test import PlexTestCase


class CompatTestCase(unittest.TestCase):
    pass


class TestTestCase(unittest.TestCase):
    def test_mocks(self):
        o = PlexTestCase()
        o.setUp()
        self.assertIsInstance(o.mLog, mock.patch)
        o.tearDown()


class UtilTestCase(unittest.TestCase):
    pass
