class Room:
    def __init__(self, room_num, fee,capacity):
        self.room_num = room_num
        self.fee = fee
        self.capacity=capacity
        self.playlist={}
        self.guests=[]


    def can_check_in(self,guest,room):
        if not self.capacity>0:
             return False
        if not guest.age>21:
             return False
        if guest in room.guests:
             return False
        else:
             return True
   

    def guest_check_in(self,guest,room):
      if self.can_check_in(guest,room):
       self.guests.append(guest)
       self.capacity-=1
       guest.money-=room.fee


    def can_check_out(self,guest,room,food,quantity,menu):

        if guest.money >= guest.total_spend(food,quantity,room,menu):
            return True
        else:
            return False

           
    def guest_check_out(self,guest,room,food,quantity,menu):
        if self.can_check_out(guest,room,food,quantity,menu):
          self.capacity+=1
          guest.money-=guest.total_spend(food, quantity, room, menu)
        return guest.money
#notebug: why do i always have to return guest.money? 
# why is  "guest.money-=guest.total_spend(food, quantity, room, menu)" not enough. i have to store it.
#but self.capacity works 
# i think it is updated and i can directly get the updated guest.money in the test file 


        















     
    #     def order_food(self,menu,food):
    #     self.money-=menu.menu_dict[food]  
