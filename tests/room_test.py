import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.menu import Menu

class TestRoom(unittest.TestCase):

    def setUp(self):
      self.room1=Room(1,30,4)
      self.room2=Room(1,40,8)

      self.guest1=Guest('Milo',50,22)
      self.guest2=Guest('Ken',10,30)

      self.song1=Song("Lover", "Taylor Swift")
      self.song2=Song('Snow','White')

      self.menu1={
        'Nachos':5,
        "fries":4,
         'cola':3,
           'gin':4
    } 

    def test_room_has_number_fee_capacity(self):
     self.assertEqual(1,self.room1.room_num)
     self.assertEqual(30,self.room1.fee)  
     self.assertEqual(4,self.room1.capacity)  
    
# guest check-in->
# room capaciy decrease, guest name into list,guest money reduce
    def test_room_capacity_decrese(self):
      self.guest_check_in(self.guest1,self.room1)
      self.assertEqual(3,self.room1.capacity)
      self.assertEqual(20,self.guest1.money)
      #add: room.guest count +1

#guest check out->
#room capacity increase
#guest money decrease by (menu comsume+room fee)

    def test_guest_check_out(self):






    # def test_room_full(self):#capacity minus one
    #  self.room1.guest_check_in

    #  self.room1.guest_check_in(self.guest1)
    #  self.assertEqual(3,self.room1.capacity)
  




  #  def guest_age_above_21(self):
  #  def guest_can_afford_fee(self):
  #  def test_guest_can_check_in(self):







  #  def test_room_has_no_space(self):
  #   room_no_space=Room(1,30,4)

    #capacity>0

# def test_room_has_no_space(self):
#     #room capacity<=0
#     #"room is full"

# def test_guest_can_check_in(self):
#     #guest.money>room.fee
#     #room capacity>0
#     #guest.age>21

# def test_guest_money_can_decrease(self):
#     #guest.money-=fee
#     #guest.money-=menu.price

# def test_guest_can_check_out(self):
#     #after money_can_decrease():
#     #guest.money>=0
    

# def test_room_capacity_can_increase(self):
#     #provided guest checks out
#     #capacity+=1

# def test_room_capacity_can_decrease(self):
#     #provided guest checks in
#     #capacity-=1

# def test_playlist_can_increase(self):
#     #playlist.append.songs 

# def test_shoutout_guest_fav_song(self):
#     #person a makes list
#     #person b pass in the fav_song
#     #if song is in, shoutout
#     #if sone is notin, add in

# def test_guest_cannot_sing_song(self):
#     # song is not on the list 
#     #return add the song first



# find song by name 
# add song
# remove song