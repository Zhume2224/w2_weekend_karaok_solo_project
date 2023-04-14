import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
       self.guest=('Lucy',50)


    def test_guest_has_name(self):
        self.assertEqual('Lucy',self.guest.name)


