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

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()