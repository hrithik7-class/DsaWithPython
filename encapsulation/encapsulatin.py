# Python Encapsulation
# Encapsulation is about protecting data inside a class.

# It means keeping data (properties) and methods together in a class, while controlling how 
# the data can be accessed from outside the class.

# This prevents accidental changes to your data and hides the internal details of how your class 
# works.


# In Python, you can make properties private by using a double underscore __ prefix:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age) # This will cause an error

# to print the age the method who is public 

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

# p1 = Person("Tobias", 25)
# print(p1.get_age())


# Set Private Property Value
# To modify a private property, you can create a setter method.

# The setter method can also validate the value before setting it:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# p1.set_age(26)
# print(p1.get_age())

# Why Use Encapsulation?
# Encapsulation provides several benefits:

# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified



# Python also has a convention for protected properties using a single underscore _ prefix:

# Example
# Create a protected property:

# class Person:
#   def __init__(self, name, salary):
#     self.name = name
#     self._salary = salary # Protected property

# p1 = Person("Linus", 50000)
# print(p1.name)
# print(p1._salary) # Can access, but shouldn't


# Name Mangling
# Name mangling is how Python implements private properties and methods.

# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

# For example, __age becomes _Person__age.

# Example
# See how Python mangles the name:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

# p1 = Person("Emil", 30)

# # This is how Python mangles the name:
# print(p1._Person__age) # Not recommended!

class student:
    def __init__(self):
      self.result = 0
    
    def __validate(self , num):
       if not isinstance(num ,(float , int)):
          return False
       
       return True
       

    def addFun(self , num):
       if self.__validate(num):
          self.result += num
          
       else:     
          print("Invalid number")
       return num      
          
calc = student()

# print(calc.addFun(45))
calc.addFun("abc")    