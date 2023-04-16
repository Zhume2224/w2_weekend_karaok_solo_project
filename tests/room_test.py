import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.menu import Menu

class TestRoom(unittest.TestCase):

    def setUp(self):
      self.room1=Room(1,30,5)
      self.room1.playlist=[self.song1,self.song2,self.song3]
      self.room2=Room(1,40,8)

      self.guest1=Guest('Milo',60,22)
      self.guest2=Guest('Ken',10,30)

      self.song1=Song("Lover", "TS")
      self.song2=Song('Snow','White')
      self.song3=Song('Chocolate','1975')
      
      self.menu_dict1=Menu()
      self.menu_dict1.add_item("Nachos", 5)
      self.menu_dict1.add_item("Fries",4)
   


    def test_room_has_number_fee_capacity_playlist(self):
     self.assertEqual(1,self.room1.room_num)
     self.assertEqual(30,self.room1.fee)  
     self.assertEqual(4,self.room1.capacity)  
     self.assertEqual([],self.room1.playlist)  
  

   
# guest check-in->
# room capaciy decrease, guest name into list,guest money reduce
    def test_room_capacity_decrese(self):
      self.room1.guest_check_in(self.guest1,self.room1)
      self.assertEqual(3,self.room1.capacity)
      self.assertEqual(60,self.guest1.money)
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
#room capacity increase
#show totoal spend
#guest list has one person less
    def test_guest_check_out(self):
        room1=Room(1,30,5)
        room2=Room(1,30,2)


        guest1=Guest('Milo',70,22)
        guest2=Guest('Julie',50,28)
     
        menu1 = Menu()
        menu1.add_item('Burger', 10)
        menu1.add_item('Fries', 5)

        room2.guest_check_in(guest1,room2)
        room2.guest_check_in(guest2,room2)#-->2 guests checked in 

        final_spend=room2.guest_check_out(guest1,room2,'Burger',1,menu1)
        guest_remain=len(room2.guests)
       
        self.assertEqual(1,room2.capacity)#-->2 checkin, 1 check out
        self.assertEqual(40, final_spend)#-->guest1 total money spend
        self.assertEqual(1, guest_remain)#-->1 guest left in room 


#add songs to playlist
#-->playlist increase
#-->shout out fav-song

    def test_add_songs_to_playlist(self):
      self.room1.increase_playlist(self.song1,self.room1)
      self.assertEqual(3,len(self.room1.playlist))
      self.assertEqual('Whoo, good choice!',self.room1.increase_playlist(self.song1,self.room1))
