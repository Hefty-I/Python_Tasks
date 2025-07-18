class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds")
class Book:
    def __init__(self,isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
    
    def in_stock(self,copies):
        if self.copies > 0:
            return True
        else:
            return False
        
    def sell(self, copies):
        if self.in_stock(copies):
            self.copies -= copies
            print(f"Sold {copies} copies of {self.title}")
        else:
            print(f"Sorry, {self.title} is out of stock.")


    def display(self):
        print(f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Pages: {self.pages}, Price: {self.price}, Copies: {self.copies}")
        
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
        
"""Create a list named books that contains the 4 Book instance objects that you have created in question 2. Iterate over this list using a for loop and call display() for each object in the list.
Write a list comprehension to create another list that contains title of books written by Jack."""
books = [book1,book2,book3,book4]
for i in range(len(books)):
    books[i].display()

jack_books = [book.title for book in books if book.author == "Jack"]
print("\nBooks written by Jack:")
for title in jack_books:
    print(title)
    
# 6
"""Make a class Fraction that contains two instance variables, nr and dr (nr stands for numerator and dr for denominator). Define an __init__ method that provides values for these instance variables. Make the denominator optional by providing a default argument of 1.

In the __init__ method, make the denominator positive if it is negative. For example  -2/-3 should be changed to 2/3 and 2/-3 to -2/3.

Write a method named show that prints numerator, then '/' and then the denominator."""
class Fraction:
    def __init__(self, nr, dr = 1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr = -self.nr
            self.dr = -self.dr
        elif self.dr == 0:
            raise ValueError("Denominator cannot be zero")

    def show(self):
        print(f"{self.nr}/{self.dr}")
    
    #7
    """Define a method named multiply that multiples two Fraction instance objects. For multiplying two fractions, you have to multiply the numerator with numerator and denominator with the denominator.

    Inside the method, create a new instance object that is the product of the two fractions and return it. Write your method in such a way that it supports multiplication of a Fraction by an integer also.

    Similarly define a method named add to add two Fraction instance objects. Sum of two fractions n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction by an integer."""
    def multi(self,other):
        if isinstance(other, Fraction):
            new_nr = self.nr * other.nr
            new_dr = self.dr * other.dr
            return Fraction(new_nr, new_dr)
        elif isinstance(other, int):
            return Fraction(self.nr * other, self.dr) # converting the integer part into fraction.
        else:
            raise TypeError("Can only multiply by another Fraction or an integer")
        
    def add(self, other):
        if isinstance(other,Fraction):
            new_nr = (self.nr * other.dr) + (other.nr * self.dr)
            new_dr = self.dr * other.dr
            return Fraction(new_nr, new_dr)
        elif isinstance(other, int):
            new_nr = self.nr + (other * self.dr) # converting the integer part into fraction.
            return Fraction(new_nr, self.dr)
        else:
            raise TypeError("Can only add another Fraction or an integer")
        
# Example usage of the Fraction class
f1 = Fraction(2, 3)
f1.show()
f2 = Fraction(3, 4)
f2.show()
f3 = f1.multi(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multi(5) 
f3.show()



#8
"""For the following class Product, 
create a read only property named selling_price that is calculated by deducting discount from the marked_price. 
The instance variable discount represents discount in percent."""
class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
    
    @property
    def selling_price(self):
        # return self.marked_price = (self.marked_price * (100 - self.discount)) / 100
        return self.marked_price - ( self.marked_price * self.discount / 100)

    def display(self):
        print(self.id,  self.marked_price,  self.discount, self.selling_price)
        # print(f"ID: {self.id}, Marked Price: {self.marked_price}, Discount: {self.discount}%, Selling Price: {self.selling_price}")
        
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

# p1.display()
# p2.display()
# p3.display()
# p4.display()
print(p1.id, p1.selling_price)
print(p2.id, p2.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)

# 9
"""Suppose after some time, 
    you want to give an additional 2% discount on a product, 
    if its price is above 500. 
    To incorporate this change, implement discount as a property in your Product class."""
class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    @property
    def discount(self):
        # Add extra 2% if marked_price > 500
        if self.marked_price > 500:
            return self._discount + 2
        return self._discount
    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount
    @property
    def selling_price(self):
        # return self.marked_price = (self.marked_price * (100 - self.discount)) / 100
        return self.marked_price - ( self.marked_price * self.discount / 100)

    def display(self):
        # print(self.id,  self.marked_price,  self.discount, self.selling_price)
        print(f"ID: {self.id}, Marked Price: {self.marked_price}, Discount: {self.discount}%, Selling Price: {self.selling_price}")
        
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

p1.display()
p2.display()
p3.display()
p4.display()
# print(p1.id, p1.selling_price)
# print(p2.id, p2.selling_price)
# print(p3.id, p3.selling_price)
# print(p4.id, p4.selling_price)
 
p4.discount = 10
print(p4.id, p4.selling_price) 

# 10
"""Write a Circle class with an instance variable named radius and a method named area. Create two more attributes named diameter and circumference and make them behave as read only attributes. 

Perform data validation on radius, user should not be allowed to assign a negative value to it.

For a circle

diameter =  2 * radius

circumference =  2 * 3.14 * radius

area =  3.14 * radius * radius"""
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    @property
    def area(self):
        return 3.14 * self._radius * self._radius
    
c1 = Circle(7)
print("Radius:", c1.radius, "Diameter:", c1.diameter, "Circumference:", c1.circumference, "Area:", c1.area )