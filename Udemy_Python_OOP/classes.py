class Product:
    def __init__(self):
        self.name = ""
        self.__price = 0.0 # This is a private attribute
        self.__quantity = 0 # This is a private attribute
    def methodA(self):
        pass
    def __methodB(self): # This is a private method
        pass

p = Product()
p.name = "Laptop"
p._Product__price = 1200.00 # This is how a private attribute is accessed
p._Product__quantity = 5 # This is how a private attribute is accessed
print(f"Product Name: {p.name}, Price: {p._Product__price}, Quantity: {p._Product__quantity}")
print(dir(p)) # This will show all attributes and methods, including private ones