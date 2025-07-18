class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    @property # this is a read-only property
    def age(self):
        return self._age

    @age.setter # this is a write-only property
    def age(self, value):
        if value >= 20 and value <= 100:
            self._age = value
        else:
            print("Invalid age. Age must be between 20 and 100.")

p = person("John", 25)
p.display()

p.age = 30 
p.display()

# read and write properties in Bank and Book classes

# if there is no setter method, the property is read-only
# @property
# def name(self): # this is a read-only property
    # return "Bank and Book Classes with Properties"
    
# if there is no getter method, the property is write-only
# @property
# def password(self): # this is a write-only property
#   raise AttributeError("Password is write-only")
# @password.setter
# def password(self, value):
#         self._password = value


# if there is both getter and setter method, the property is read-write
# @property
# def name(self):
#         return self._name

# @name.setter
# def name(self, value):
#         self._name = value
