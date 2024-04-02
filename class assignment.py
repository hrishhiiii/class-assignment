# #1
# class StringProcessor:
#     def __init__(self):
#         self.input_string = ""
#     def get_string_from_input(self):
#         self.input_string = input("Enter a string: ")
#     def print_string_in_uppercase(self):
#         if self.input_string:
#             print(self.input_string.upper())
#         else:
#             print("No string has been input yet. Please use get_string_from_input() first.")
# processor = StringProcessor()
# processor.get_string_from_input()
# processor.print_string_in_uppercase()

#2
# class ExampleClass:
#     class_parameter = "Class Parameter"
#     def __init__(self, instance_parameter):
#         self.instance_parameter = instance_parameter
# instance1 = ExampleClass("Instance Parameter 1")
# instance2 = ExampleClass("Instance Parameter 2")
# print("Instance 1 - Class Parameter:", instance1.class_parameter)
# print("Instance 1 - Instance Parameter:", instance1.instance_parameter)
# print("Instance 2 - Class Parameter:", instance2.class_parameter)
# print("Instance 2 - Instance Parameter:", instance2.instance_parameter)

#3
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def compute_area(self):
#         return math.pi * self.radius ** 2
# radius = float(input("Enter the radius of the circle: "))
# circle = Circle(radius)
# area = circle.compute_area()
# print("Area of the circle:", area)

#4
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawal of {amount} successful.")
#         else:
#             print("Withdrawal failed. Insufficient funds.")
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposit of {amount} successful.")
#         else:
#             print("Deposit failed. Please deposit a positive amount.")
#     def check_balance(self):
#         print(f"Current balance: {self.balance}")
# account = BankAccount(1000)  
# account.check_balance()     
# account.deposit(500)        
# account.check_balance()     
# account.withdraw(200)       
# account.check_balance()     
# account.withdraw(2000)      

#5
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         return self.length ** 2
# shape = Shape()
# print("Area of Shape:", shape.area())  # Output: Area of Shape: 0
# square = Square(5)
# print("Area of Square:", square.area())  # Output: Area of Square: 25

#6
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_details(self):
#         print("Car Details:")
#         print("Make:", self.make)
#         print("Model:", self.model)
#         print("Year:", self.year)
# car = Car("Toyota", "Camry", 2022)
# car.display_details()

#7
# class Student:
#     total_students = 0  
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         Student.total_students += 1  
#     def display_details(self):
#         print("Student Details:")
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Grade:", self.grade)
#         print("Total number of students:", Student.total_students)
# student1 = Student("Alice", 16, 11)
# student1.display_details()
# student2 = Student("Bob", 17, 12)
# student2.display_details()

#8
# class BankAccount:
#     def __init__(self, account_number, initial_balance=0):
#         self.__balance = initial_balance
#         self.__account_number = account_number
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposit of ${amount} successful.")
#         else:
#             print("Deposit amount should be greater than zero.")
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawal of ${amount} successful.")
#         else:
#             print("Withdrawal failed. Insufficient funds.")
#     def display_balance(self):
#         print(f"Account Number: {self.__account_number}")
#         print(f"Current Balance: ${self.__balance}")
# account = BankAccount("123456789", 1000)  
# account.display_balance()                
# account.deposit(500)                      
# account.display_balance()                
# account.withdraw(200)                     
# account.display_balance()                
# account.withdraw(2000)                    

#9
# class Author:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year
# class Book:
#     def __init__(self, title, year, author):
#         self.title = title
#         self.year = year
#         self.author = author
#     def display_book_details(self):
#         print("Book Details:")
#         print("Title:", self.title)
#         print("Year:", self.year)
#         print("Author:", self.author.name)
#         print("Author's Birth Year:", self.author.birth_year)
# author1 = Author("J.K. Rowling", 1965)
# book1 = Book("Harry Potter and the Philosopher's Stone", 1997, author1)
# book1.display_book_details()


