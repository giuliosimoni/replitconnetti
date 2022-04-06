person = {'name': 'Giulio', 'age': 23}
p = ['Giulio Simoni', 23]

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(p)
print(sentence)

class Person():

  def __init__(self,name,age):
    self.name = name
    self.age = age

p1 = Person('Simoni', '23')

sentence = 'My surname is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

sentence = 'My name is {name]} and I am {0[age]} years old.'.format(person)
print(sentence)

"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.