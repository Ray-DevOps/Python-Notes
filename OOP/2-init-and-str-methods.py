#                 The __init__() Function
            ------------------------------------------


# All classes have a function called __init__(), which is always executed when the class is being initiated.
# The __init__() function is used to assign values to object properties, or other operations that are necessary 
# to do when the object is being created.
# The self parameter is a reference to the current instance of the class (the object), and is used to access 
# variables that belongs to the class. It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:

class People:
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

john = People("John", 36, "carpenter")

print(john.name)           ---------->        john thomas
print(john.age)            ---------->        36
print(john.profession)     ---------->        carpenter

john.age = 37                                 # We can always modify the value of an attribute after assigning it

print(john.age)            ---------->        36



#                 The __str__() Function
            ------------------------------------------

# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

class People:
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

  def __str__(self):
    return f"My name is {self.name}, I am {self.age}, I work as a {self.profession}"

john = People("john thomas", 36, "carpenter")

print(john)        ---------->   My name is john thomas, I am 36, I work as a carpenter



#                 Object Methods
            ------------------------------------------

# Objects can also contain methods. Methods in objects are functions that belong to the object.

class People:
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

  def intro_method(self):
    print(f"Hello, my name is {self.name}, I am {self.age} years old")

john = People("john thomas", 36, "carpenter")
anita = People("anita kelly", 27, "receptionist")

john.intro_method()      ---------->   Hello, my name is john thomas, I am 36 years old
anita.intro_method()     ---------->   Hello, my name is anita kelly, I am 27 years old



#                 Modifying and Deleting Object Properties
            --------------------------------------------------

class People:
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

john = People("john thomas", 36, "carpenter")
anita = People("anita kelly", 27, "receptionist")

print(john.age)              ---------->    36
john.age = 40
print(john.age)              ---------->    40

print(anita.profession)      ---------->   receptionist
del anita
print(anita.profession)      ---------->   NameError: name 'anita' is not defined