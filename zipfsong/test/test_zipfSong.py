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
        topSongsInstance = topSongs()
        testSongExample = topSongs.sortSongs(self.simpleList)
        self.assertEqual(testSongExample, , 'Songs do not match')

    def test_complexList(self):
        from zipfSong import topSongs
        topSongsInstance = topSongs()
        testSongsExample = topSongs.sortSongs(self.complexList)
        self.assertEqual(testSongExample, , 'Songs do not match')

    def test_equalPopularity(self):
        from zipfSongs import topSongs
        topSongsInstance = topSongs()
        testSongsExample = topSongs.sortSongs(self.equalPopularity)
        self.assertEqual(testSongExample, , 'Songs do not match')

    def test_checkAllSongs(self):
        from zipfSongs import topSongs
        topSongsInstance = topSongs()
        testSongsExample = topSongs.sortSongs(self.checkAllSongs)
        self.assertEqual(testSongsExample, , 'Songs do not match')
