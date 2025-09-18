"""
   Filename: computer.py
Description: A class that simulates a computer.
     Author: Claire Newcom (cnewcom@smith.edu)
       Date: 18 September 2025
    
"""

class Computer:

    from typing import Optional

    # What attributes will it need?
    # Based on the procedural shop, a computer has the features:
    #           - description  - processor_type  - hard_drive_capacity
    #           - memory  - operating_system  - year_made  - price

    """
    description: The description of the computer as a string
    """
    description: str

    """
    processor_type: the processor type of the computer as a string
    """
    processor_type: str

    """
    hard_drive_capacity: the hard drive capacity of the computer as an int
    """
    hard_drive_capacity: int

    """
    memory: The amount of memory of the computer as an int
    """
    memory: int

    """
    operating_system: The operating system of the computer as a string
    """
    operating_system: str

    """
    year_made: the year the computer was made as an integer
    """
    year_made: int

    """
    price: the price of the computer as a float (because money can have decimals)
    """
    price: float

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    Initializes an instance of the Computer class
    """
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:float):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
    # What methods will you need?
    #       - updatePrice (or setPrice)
    #       - getPrice
    #       - getters and setters for all attributes
    #       - printComputer

    """
    A helper function for print_inventory in the ResaleShop class. This
    method returns a string representing a Computer object.
    """
    def print_computer(self):
        return("Description: " + self.description + ", Processor type: " + self.processor_type + ", Hard Drive Capacity: " + str(self.hard_drive_capacity) + ", Memory: " + str(self.memory) + ", Operating System: " + self.operating_system +  ", Year Made: " + str(self.year_made) + ", Price: " + str(self.price))


    """
    A helper function for refurbish in the ResaleShop class. This method
    takes in a new_os as an Optional[str]. Depending on the year the computer
    was made, the price of the computer changes. If there was a new_os given,
    change this computer's os to that.
    """
    def refurbish_computer(self, new_os: Optional[str] = None):
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price =250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        if new_os is not None:
            self.operating_system = new_os # update details after installing new OS
        

    """
    Returns the description attribute of this computer
    """
    def get_description(self):
        return self.description
    
    """
    Takes in a new description as a string. Sets the description attribute 
    of this computer to that new value.
    """
    def set_description(self, new_des: str):
        self.description = new_des


    """
    Returns the processor_type attribute of this computer
    """
    def get_processor_type(self):
        return self.processor_type
    

    """
    Takes in a new processor_type as a string. Sets the processor_type attribute 
    of this computer to that new value.
    """
    def set_processor_type(self, new_type:str):
        self.processor_type = new_type


    """
    Returns the hard_drive_capacity attribute of this computer
    """
    def get_hard_drive_capacity(self):
        return self.hard_drive_capacity
    

    """
    Takes in a new hard_drive_capacity as an int. Sets the hard_drive_capacity attribute 
    of this computer to that new value.
    """
    def set_hard_drive_capacity(self, new_hdc: int):
        self.hard_drive_capacity = new_hdc


    """
    Returns the memory attribute of this computer
    """
    def get_memory(self):
        return self.memory
    

    """
    Takes in a new memory as an int. Sets the memory attribute 
    of this computer to that new value.
    """
    def set_memory(self, new_mem: int):
        self.memory = new_mem


    """
    Returns the operating_system attribute of this computer
    """
    def get_operating_system(self):
        return self.operating_system
    

    """
    Takes in a new operating_system as a string. Sets the operating_system attribute 
    of this computer to that new value.
    """
    def set_operating_system(self, new_OS: str):
        self.operating_system = new_OS


    """
    Returns the year_made attribute of this computer
    """
    def get_year_made(self):
        return self.year_made
    

    """
    Takes in a new year_made as an int. Sets the year_made attribute 
    of this computer to that new value.
    """
    def set_year_made(self, new_year_made:int):
        self.year_made = new_year_made


    """
    Returns the price attribute of this computer
    """
    def get_price(self):
        return self.price


    """
    Takes in a new price as a float. Sets the price attribute 
    of this computer to that new value.
    """
    def set_price(self, new_price:float):
        self.price = new_price