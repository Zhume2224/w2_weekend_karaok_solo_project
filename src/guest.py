
class Guest:
    def __init__(self, name, money,age):
        self.name = name
        self.money = money
        self.fav_song=[]
        self.age=age

# #note:method1:set a dict in guest.py in the order_food method
#     def order_food(self,food):
#         menu1={'Burger':10}
#         self.money-=menu1[food]
  
#note:method2: pass in money directly
#this is bug becasue menu is an instance of the Menu class, which is not subscriptable.
# --> In your code, you're trying to access an item in the menu object using square brackets, which is not possible because the menu object is not a dictionary or a list, but an instance of the Menu class.
    def order_food(self,menu,food):
        self.money-=menu.menu_dict[food]  


    def pay_room_fee(self,room):
        self.money-=room.fee

   

    