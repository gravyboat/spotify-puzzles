#/usr/bin/python2.6

import unittest
import sys

sys.path.insert(0, '../')

simpleList = [('', , ), ('', , )]
complexList = [('', , ), ('', , )]
equalPopularity = [('', , ), ('', , )]
checkAllSongs = [('', , ), ('', , )]

class zipfSongTestCase(unittest.TestCase):

    def setUp(self):
        self.simpleList = simpleList
        self.complexList = complexList
        self.equalPopularity = equalPopularity
        self.checkAllSongs = checkAllSongs

    def test_simpleList(self):
        from zipfSong import topSongs

    def test_complexList(self):


    def test_equalPopularity(self):


    def test_checkAllSongs(self):
