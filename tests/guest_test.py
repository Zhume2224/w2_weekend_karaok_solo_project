import unittest
from src.guest import Guest
from src.menu import Menu
from src.room import Room





class TestGuest(unittest.TestCase):

    def setUp(self):
       self.guest=Guest('Lucy',50,21)
       self.room1=Room(1,30,4)
       
       self.menu1 = Menu()
       self.menu1.add_item('Burger', 10)
       self.menu1.add_item('Fries', 5)


    def test_guest_has_name_money_legalage(self):
        self.assertEqual('Lucy',self.guest.name)
        self.assertEqual(50,self.guest.money)
        self.assertEqual(21,self.guest.age)

# #note:method1:set a dict in guest.py in the order_food method
#     def test_guest_money_decrease_order_food_from_menu(self):  
#         self.guest.order_food('Burger')
#         self.assertEqual(40,self.guest.money)

#note:method2: pass in money directly
    def test_guest_money_decrease_order_food_from_menu(self):  
        self.guest.order_food('Burger')
        self.assertEqual(40,self.guest.money)

    def test_guest_money_decrease_pay_room_fee(self):
        room1=Room(1,30,4)
        self.guest.pay_room_fee(room1)
        self.assertEqual(20,self.guest.money)

    def test_get_guest_total_spend(self):
        total=self.guest.total_spend('Burger',self.room1)
        self.assertEqual(40,total)










