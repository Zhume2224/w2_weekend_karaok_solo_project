class Menu:
    def __init__(self):
        self.menu_dict = {}
        

    def __len__(self):
      return len(self.menu_dict)

    def add_item(self, food, price):
        self.menu_dict[food] = price
        return len(self.menu_dict)

    def remove_item(self, food):
        if food in self.menu_dict:
            del self.menu_dict[food]
        # return len(self.menu_dict)


    def get_price(self, food):
        if food in self.menu_dict:
            return self.menu_dict[food]
        else:
            return None

    def get_menu(self):
        return self.menu_dict
