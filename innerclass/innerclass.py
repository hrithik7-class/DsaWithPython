# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.

# ExampleGet your own Python Server
# Create an inner class:

# class Outer:
#   def __init__(self):
#     self.name = "Outer Class"

#   class Inner:
#     def __init__(self):
#       self.name = "Inner Class"

#     def display(self):
#       print("This is the inner class")

# outer = Outer()
# print(outer.name)


class outer:
    def __init__(self):
        self.name = "outer class"

    class inner:
        def __init__(self, outer_instance):
            self.outer = outer_instance

        def display(self):
            print(f"outer name is {self.outer.name}")

out = outer()
Inner = outer.inner(out)

Inner.display()


# class Outer:
#   def __init__(self):
#     self.name = "Emil"

#   class Inner:
#     def __init__(self, outer):
#       self.outer = outer

#     def display(self):
#       print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()
