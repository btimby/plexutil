import unittest
import mock


class PlexTestCase(unittest.TestCase):
    '''Makes tests easier to write.'''

    def setUp(self):
        '''mock stuff usually provided by Plex Media Server.'''
        self.mLog = mock.patch('Log')
        self.mLog.start()
    
    def tearDown(self):
        '''Stop mocking.'''
        self.mLog.stop()
