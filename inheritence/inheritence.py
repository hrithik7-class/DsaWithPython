class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



# # x = Person("John", "Doe")
# # x.printname()



# class Child(Person):
#   pass


# c1 = Child("dev" , "joe")

# c1.printname()


# class child(Person):
#   def __init__(self , fname , lname):
#    Person.__init__(self, fname , lname)

class child(Person):
  def __init__(self , fname , lname):
    super().__init__(fname , lname)


c1 = child("hrithk" , "kesarwani")    
c1.printname()


