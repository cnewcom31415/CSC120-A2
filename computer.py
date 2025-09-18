class Computer:

    from typing import Optional

    # What attributes will it need?
    # Based on the procedural shop, a computer has the features:
    #           - description  - processor_type  - hard_drive_capacity
    #           - memory  - operating_system  - year_made  - price

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: float

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
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

    def print_computer(self):
        return("Description: " + self.description + ", Processor type: " + self.processor_type + ", Hard Drive Capacity: " + str(self.hard_drive_capacity) + ", Memory: " + str(self.memory) + ", Operating System: " + self.operating_system +  ", Year Made: " + str(self.year_made) + ", Price: " + str(self.price))

    def refurbish_Computer(self, new_os: Optional[str] = None):
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
        

    def get_description(self):
        return self.description
    
    def set_description(self, new_des: str):
        self.description = new_des

    def get_processor_type(self):
        return self.processor_type
    
    def set_processor_type(self, new_type:str):
        self.processor_type = new_type

    def get_hard_drive_capacity(self):
        return self.hard_drive_capacity
    
    def set_hard_drive_capacity(self, new_hdc: int):
        self.hard_drive_capacity = new_hdc

    def get_memory(self):
        return self.memory
    
    def set_memory(self, new_mem: int):
        self.memory = new_mem

    def get_operating_system(self):
        return self.operating_system
    
    def set_operating_system(self, new_OS: str):
        self.operating_system = new_OS

    def get_year_made(self):
        return self.year_made
    
    def set_year_made(self, new_year_made:int):
        self.year_made = new_year_made

    def get_price(self):
        return self.price

    def set_price(self, new_price:float):
        self.price = new_price