class Room:
    def __init__(self, room_num, fee,capacity):
        self.room_num = room_num
        self.fee = fee
        self.capacity=capacity
        # note try1:with playlist
    #     self.playlist={
    # "Lover": "Taylor Swift",
    # "Shallow": "Lady Gaga",
    # "Happy": "Pharrell Williams",
    # "Uptown": "Bruno Mars",
    # "Sorry": "Justin Bieber",
    # "Havana": "Camila Cabello"}
    #note: guest add play list
        self.playlist={}

        self.menu= {
        "Nachos": 5,
        "fries": 4,
         "coke": 3,
         "beer":5,
         "cider":3}

         