import unittest
from src.menu import Menu

class TestMenu(unittest.TestCase):
        
   def setUp(self):
     self.menu_dict1 = Menu()
     self.menu_dict1.add_item("Nachos", 5)
     self.menu_dict1.add_item("fries",4)

#-->way1: store length in result
   def test_add_item(self):
      result=self.menu_dict1.add_item('cola',3)
      self.assertEqual(3,result)

#-->way2: define __len__ method in menu.py

   def test_remove_item(self):
     self.menu_dict1.remove_item('fries')
     self.assertEqual(1,len( self.menu_dict1))

   def test_get_price(self):
     self.assertEqual(5,self.menu_dict1.get_price("Nachos"))

   def  test_get_no_price_food_is_not_in_menu(self):
      self.assertIsNone(self.menu_dict1.get_price("Pizza"))

   def test_get_menu(self):#-->make inner scope has Menu class
      menu_dict2=Menu()
      menu_dict2.add_item("Juice",4)
      result=menu_dict2.add_item("Crisps",5)
      self.assertEqual(2,result)

      #note: wht it returns 2, after i call it for twice??
      #original method is :

        # def get_menu(self):
        # return self.menu_dict


        

