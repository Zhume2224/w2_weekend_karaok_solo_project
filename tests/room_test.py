import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom:(unittest.TestCase):

def setUp(self):
    self.room1=Room(1,30,4)
    self.room2=Room(1,40,8)

    self.guest1=Guest('Milo',50)
    self.guest2=Guest('Ken',10)

    self.song1=Song("Lover", "Taylor Swift")
    self.song2=Song('Snow','White')

def test_room_has_number_fee_capacity(self):

def test_room_has_space(self):
    #capacity>0

def test_room_has_no_space(self):
    #room capacity<=0
    #"room is full"

def test_guest_can_check_in(self):
    #guest.money>room.fee
    #room capacity>0

def test_guest_money_can_decrease(self):
    #guest.money-=fee
    #guest.money-=menu.price

def test_guest_can_check_out(self):
    #after money_can_decrease():
    #guest.money>=0
    

def test_room_capacity_can_increase(self):
    #provided guest checks out
    #capacity+=1

def test_room_capacity_can_decrease(self):
    #provided guest checks in
    #capacity-=1

def test_playlist_can_increase(self):
    #playlist.append.songs 

def test_shoutout_guest_fav_song(self):
    #if song is in, shoutout
    #if sone is notin, add in





