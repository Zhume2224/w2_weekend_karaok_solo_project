class Room:
    def __init__(self, room_num, fee,capacity):
        self.room_num = room_num
        self.fee = fee
        self.capacity=capacity
        self.playlist=[]
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
 #notebug: append guest1 and guest2 to guests=[] or guests={} . which is better and how to get name, money and age from it??
#  guest1=Guest('Milo',70,22)
# guest2=Guest('Julie',50,28)


    def can_check_out(self,guest,room,food,quantity,menu):

        if guest.money >= guest.total_spend(food,quantity,room,menu):
            return True
        else:
            return False

           
    def guest_check_out(self,guest,room,food,quantity,menu):
        if self.can_check_out(guest,room,food,quantity,menu):
          self.capacity+=1
          self.guests.remove(guest)
          final_spend=guest.total_spend(food, quantity, room, menu)
          return final_spend

#notebug: is it necessary to specify which room?because i think different rooms will have different playlist.
    def increase_playlist(self,song,room):
        if song not in room.playlist:
           room.playlist.append(song)
        else:
            return 'Whoo, good choice!'
        















     
    #     def order_food(self,menu,food):
    #     self.money-=menu.menu_dict[food]  
