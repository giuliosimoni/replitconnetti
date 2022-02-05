class MyClass:
  def __init__(self, name, age):
    self.attribute1 = name
    self.attribute2 = age

  def myfunc(self):
    print("Hello my attrib1 is " + self.attribute1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc1(self):
    print("My name is " + self.name)

  def myfunc2(self):
    print("My age is " + self.age)

p1 = Person("John", "36")
p1.myfunc1()
p1.myfunc2()

string='Hello World!'
print(lambda string : print(string))

sum [arg1 ,arg2]: arg1 + arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print( "Value of total : ", sum( 20, 20 ))