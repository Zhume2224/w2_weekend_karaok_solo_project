import unittest
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1=Song("Lover", "Taylor Swift")


    def test_song_has_name_and_singer(self):
        self.assertEqual("Lover",self.song1.name)
        self.assertEqual("Taylor Swift",self.song1.singer)




 