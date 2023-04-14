import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
       self.guest=Guest('Lucy',50)


    def test_guest_has_name_and_money(self):
        self.assertEqual('Lucy',self.guest.name)
        self.assertEqual(50,self.guest.money)


