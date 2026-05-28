class Person:
 def __init__(self,name,age):
    self.name = name
    self.age = age
 def greet(self):
    print(f"Hello my name is {self.name} and age is {self.age}")


p1 = Person("John" , 36)


p1.greet()  

p2 =Person("John",41)
p2.age =24
p2.greet()


p3 = Person("nina" ,25)
p2.name = "hennah"
del p3


