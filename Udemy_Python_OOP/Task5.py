# 1
"""Create a class named Course that has instance variables title, instructor, price, lectures, users(list type), ratings, avg_rating.
Implement the methods __str__, new_user_enrolled, received_a_rating and show_details.
From the above class, inherit two classes VideoCourse and PdfCourse. 
The class VideoCourse has instance variable length_video and PdfCourse has instance variable pages."""

class Course:
    def __init__(self, title, instructor, price):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = []
        self.users = []
        self.ratings = []
        self.avg_rating = 0.0
        
    def __str__(self):
        return f"Course Title: {self.title}, Instructor: {self.instructor}, Price: ${self.price}, Average Rating: {self.avg_rating}"
    
    def new_user_enrolled(self, user):
        self.users.append(user)
        print(f"{user} has been enrolled in {self.title}.")
        
    def received_a_rating(self, user, rating):
        if user in self.users:
            self.ratings.append(rating)
            self.avg_rating = sum(self.ratings) / len(self.ratings)
        else:
            print(f"{user} is not enrolled in {self.title}.")

    def show_details(self):
        return f"Title: {self.title}, Instructor: {self.instructor}, Price: ${self.price}, Users Enrolled: {len(self.users)}, Average Rating: {self.avg_rating}"
        
class VideoCourse(Course):
    def __init__(self, title, instructor, price, length_video):
        super().__init__(title, instructor, price)
        self.length_video = length_video


class PdfCourse(Course):
    def __init__(self, title, instructor, price, pages):
        super().__init__(title, instructor, price)
        self.pages = pages
        
        
#-----------------------------------------------------------------------------------------------
# 2        
class Mother:
        def cook(self):
           print('Can cook pasta')
 
class Father:
        def cook(self):
             print('Can cook noodles')
 
class Daughter(Father, Mother):
          pass
 
class Son(Mother, Father):
         def cook(self):
             super().cook()
             print('Can cook butter chicken') 
 
d = Daughter()  
s = Son()
 
d.cook()
print()
s.cook()

#-----------------------------------------------------------------------------------------------
# 3
class Person:
    def greet(self):
        print('I am a Person')
 
class Teacher(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')
 
class Student(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Student')
 
class TeachingAssistant(Student, Teacher):
     def greet(self):
         super().greet()
         print('I am a Teaching Assistant')
       
x = TeachingAssistant()
x.greet()

#-----------------------------------------------------------------------------------------------
# 4
"""In the following inheritance hierarchy we have written code to add 
'S' to id of Student, 'T' to id of Teacher and both 'T' and 'S' to id of Teaching Assistant.
What will be the output of this code. If the code does not work as intended, what changes we need to make."""
class Person:
    def __init__(self,id):
        self.id = id
        
class Teacher(Person):
    def __init__(self,id):
        super().__init__(id) # changed this line to call the parent constructor
        self.id += 'T'
    
class Student(Person):
    def __init__(self,id):
        super().__init__(id) # same for this. called the parent constructor
        self.id += 'S'
   
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        super().__init__(id) # same for this line to call the parent constructor
       
x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)
