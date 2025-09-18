"""
   Filename: oo_resale_shop.py
Description: A class that simulates a computer resale shop.
     Author: Claire Newcom (cnewcom@smith.edu)
       Date: 18 September 2025  
"""
from computer import Computer

class ResaleShop:

    
    from typing import Optional

    # What attributes will it need?
    # inventory

    """ 
    inventory: a list that stores the inventory of the shop. 
    The inventory consists of computer objects.
    """
    inventory : list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    Initializes an instance of the ResaleShop class
    """
    def __init__(self):
        self.inventory = []
        

    # What methods will you need?
    #   buy (takes in a computer object and adds it to inventory)
    #   update_price (takes in item id and new price, changes price if item exists)
    #   sell (remove item at given id number given it exists)
    #   print inventory (use the computer print function (will have to make))
    #   refurbish

    """ 
    Simulates the aquisition of a new computer in the shop. Takes in
    a computer object, returns the index of that computer object in the 
    inventory (aka the item_id).
    """
    def buy (self, new_item:Computer):
        self.inventory.append(new_item)
        return self.inventory.index(new_item)
    
    """ 
    Takes in an item_id as an int and a new_price as an int. If there is a 
    computer associated with the given id, change the price of that computer,
    if there is not a computer associated with that id number, print an error.
    """
    def update_price(self, item_id: int, new_price: int):
        if (len(self.inventory)-1 >= item_id and item_id>0):
            self.inventory[item_id].set_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")

    """
    Takes in an item_id as an int. If there is a computer associated with the
    given id, remove that item from the inventory, and print that it has been
    sold. If there is not a computer associated with the given id, print an
    error.
    """
    def sell(self, item_id: int):
        if (len(self.inventory)-1 >= item_id and item_id>0):
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")


    """
    Prints out all computers in the inventory. If the inventory is empty, print 
    "No inventory to display."
    """
    def print_inventory(self):
        if self.inventory:
        # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: ' + str(self.inventory.index(item)) + " " + item.print_computer())
        else:
            print("No inventory to display.")

    
    """
    Takes in an item_id as an int and a new_os as an Optional[str]. If there is
    a computer associated with the id, refurbish that item and update the inventory.
    If the id is not associated with a computer, print an error.
    """
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if (len(self.inventory)-1 >= item_id and item_id>0):
            item = self.inventory[item_id] # locate the computer
            item.refurbish_computer(new_os) # call on a helper method in the computer class
            self.inventory[item_id] = item
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


"""
A main method used to test the code.
"""
def main():

    my_Shop = ResaleShop()

    #testing buy  and print_inventory
    my_Shop.print_inventory() # should print No inventory to display
    new_Computer = Computer(description ="2019 MacBook Pro", processor_type = "Intel", hard_drive_capacity = 256, memory = 16, operating_system = "High Sierra", year_made = 2019, price = 1000)
    
    my_Shop.buy(new_Computer)
    my_Shop.print_inventory()

    # testing update price
    my_Shop.update_price(item_id=0, new_price=750)
    my_Shop.print_inventory() #expect price to now be 750
    my_Shop.update_price(item_id=1, new_price=10000) # expect to see: Item 1 not found. Cannot update price.

    # testing refurbish
    comp_1 = Computer(description="new comp 1",processor_type = "Intel", hard_drive_capacity = 256, memory = 16, operating_system = "High Sierra", year_made = 1999, price = 1400)
    comp_2 = Computer(description="new comp 2",processor_type = "Intel", hard_drive_capacity = 256, memory = 16, operating_system = "High Sierra", year_made = 2000, price = 0)
    comp_3 = Computer(description="new comp 3",processor_type = "Intel", hard_drive_capacity = 256, memory = 16, operating_system = "High Sierra", year_made = 2012, price = 1000)
    comp_4 = Computer(description="new comp 4",processor_type = "Intel", hard_drive_capacity = 256, memory = 16, operating_system = "High Sierra", year_made = 2018, price = 500)

    my_Shop.buy(comp_1)
    my_Shop.buy(comp_2)
    my_Shop.buy(comp_3)
    my_Shop.buy(comp_4)

    my_Shop.print_inventory()
    my_Shop.refurbish(item_id=0,new_os="MacOS")
    my_Shop.refurbish(item_id=1,new_os="MacOS")
    my_Shop.refurbish(item_id=2,new_os="MacOS")
    my_Shop.refurbish(item_id=3,new_os="MacOS")
    my_Shop.refurbish(item_id=4,new_os="MacOS")
    my_Shop.refurbish(item_id=5,new_os="MacOS") #should print an error
    
    my_Shop.print_inventory() 
    # 0 should have price 1000, 1 should have price 0
    # 2 should have price 250, 3 should have price 550, 4 should have price 1000

    # testing sell
    my_Shop.sell(0)
    my_Shop.print_inventory() # Macbook should be gone
    my_Shop.sell(5) #should print an error

    my_Shop.refurbish(item_id=-2,new_os="MacOS")
    my_Shop.sell(item_id=-2)
    my_Shop.update_price(item_id=-2, new_price=100) #all 3 should print errors
    


if __name__ == "__main__":
    main()