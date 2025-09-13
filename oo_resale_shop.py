class ResaleShop:

    import computer
    from typing import Optional

    # What attributes will it need?
    # inventory

    inventory : list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    #   buy (takes in a computer object and adds it to inventory)
    #   update_price (takes in item id and new price, changes price if item exists)
    #   sell (remove item at given id number given it exists)
    #   print inventory (use the computer print function (will have to make))
    #   refurbish

    def buy (self, new_item:computer):
        self.inventory.append(new_item)
        return self.inventory.index(new_item)
    
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id].set_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id: int):
        if self.inventory[item_id]:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        if self.inventory:
        # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.print_computer()}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            item = self.inventory[item_id] # locate the computer
            if int(item.get_year_made()) < 2000:
                item.set_price(0) # too old to sell, donation only
            elif int(item.get_year_made()) < 2012:
                item.set_price(250) # heavily-discounted price on machines 10+ years old
            elif int(item.get_year_made()) < 2018:
                item.set_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                item.set_price(1000) # recent stuff

            if new_os is not None:
                item.set_operating_system(new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
