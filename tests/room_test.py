import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.menu import Menu

class TestRoom(unittest.TestCase):

    def setUp(self):
      self.room1=Room(1,30,4)
      self.room2=Room(1,40,8)

      self.guest1=Guest('Milo',60,22)
      self.guest2=Guest('Ken',10,30)

      self.song1=Song("Lover", "Taylor Swift")
      self.song2=Song('Snow','White')
      
      self.menu_dict1=Menu()
      self.menu_dict1.add_item("Nachos", 5)
      self.menu_dict1.add_item("Fries",4)
      self.menu_dict1.add_item("Cola",4)
      self.menu_dict1.add_item("Gin",6)


    def test_room_has_number_fee_capacity(self):
     self.assertEqual(1,self.room1.room_num)
     self.assertEqual(30,self.room1.fee)  
     self.assertEqual(4,self.room1.capacity)  
   
# guest check-in->
# room capaciy decrease, guest name into list,guest money reduce
    def test_room_capacity_decrese(self):
      self.room1.guest_check_in(self.guest1,self.room1)
      self.assertEqual(3,self.room1.capacity)
      self.assertEqual(30,self.guest1.money)
      result=len(self.room1.guests)
      self.assertEqual(1,result)
#compelete:)

    def test_guest_cannot_checkout(self):
      guest2=Guest('Ken',4,30)
      room2=Room(1,40,8)
      menu2=Menu()
      menu2.add_item("Fries",4)
      result=room2.can_check_out(guest2,room2,'Fries',1, menu2)
      self.assertEqual(False,result)
#compelete:)


#guest check out->
    def test_guest_check_out(self):
      room1=Room(1,30,5)
      guest1=Guest('Milo',60,22)
      guest2=Guest('Milo',60,22)

      menu=Menu()
      menu.add_item("Fries",4)

      room1.guest_check_in(guest1,room1)
      room1.guest_check_in(guest2,room1)#-->2 guests checked in 

      guest1.total_spend('Fries',1,room1,menu)
      result=room1.guest_check_out(guest1,room1,'Fries',1,menu)
      self.assertEqual(3,room1.capacity)
      self.assertEqual(26,result)
#notebug: why is this code wrong?
#result of guest_check_out increase room capacity
# decrease guest money by deduct roomfee and food price

# room1.guest_check_out(guest1,room1,'Fries',1,menu)
#self.assertEqual(26,guest1.money)
#complete :) 





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