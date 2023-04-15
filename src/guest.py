
class Guest:
    def __init__(self, name, money,age):
        self.name = name
        self.money = money
        self.fav_song=''
        self.age=age
    

# #note:method1:set a dict in guest.py in the order_food method
#     def order_food(self,food):
#         menu1={'Burger':10}
#         self.money-=menu1[food]
  
#note:method2: pass in money directly
#this is bug becasue menu is an instance of the Menu class, which is not subscriptable.
# --> In your code, you're trying to access an item in the menu object using square brackets, which is not possible because the menu object is not a dictionary or a list, but an instance of the Menu class.
    def order_food(self,food):
        menu={'Burger':10}
        self.money-=menu[food]  
        


    def pay_room_fee(self,room):
        self.money-=room.fee

    def total_spend(self,food,room):
        total=0
        menu={'Burger':10,
        'Fries':4}
        if food in menu:
            total+=(menu[food]+room.fee)
            return total
        else:
            return False

#note: before fixed, 
    # def total_spend(self, food, quantity,room):
    #   menu = {'Burger': 10, 'Fries': 4}
    #   if food in menu:
    #     total = menu[food]*quantity + room.fee
    #     return total
    #   else:
    #     total=room.fee

#note:trying to fix:
    def total_spend(self, food, quantity, room, menu):
      if food in menu.menu_dict:
          total = menu.menu_dict[food] * quantity + room.fee
          return total
      else:
          total = room.fee
          return total





    

   

    