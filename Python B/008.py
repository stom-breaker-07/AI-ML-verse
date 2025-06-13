# OOPs in detail
# OOPs in python which is object oriented program in python mainly 4 features :
# Data encapsulation
#      -> Data encapsulation in Python's OOP is the practice of bundling data (attributes) and methods (functions)
#      within a class while restricting direct access to the data. It ensures controlled access through public,
#      protected, or private modifiers and promotes security and data integrity using getter and setter methods.

# Inheritance
# Overriding
# Polymorphism

# A class a blueprint for creating objects, encapsulating data (attributes) and behavior (methods) into a
# single logical unit. It defines the structure and actions of the objects derived from it.

# defining a class called Person

class Person:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def person_info(self):
        print("Name : ",self.name)
        print("Age :",self.age)

p1=Person("Ram",20)
p1.person_info()

#Name :  Ram
#Age : 20


# Initation of class method and class atribute

class Person2:
    count=0
    def __init__(self ,a,b):
        self.name=a
        self.age=b
        Person2.count+=1
    def Show_info(self):
        print("Name : ", self.name)
        print("Age :", self.age)

    @classmethod
    def show_cnt(cls):
        print(f'Total number of object created are , {cls.count}')

p2_1=Person2("John Wick",32)
p2_1.Show_info()
p2_2=Person2("Tony Stark",42)
p2_2.Show_info()
p2_3=Person2("Bruce Banner",38)
p2_3.Show_info()

Person2.show_cnt()

#Output
# Name :  John Wick
# Age : 32
# Name :  Tony Stark
# Age : 42
# Name :  Bruce Banner
# Age : 38
# Total number of object created are , 3
