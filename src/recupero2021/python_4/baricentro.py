from statistics import mean
import numpy as np
import math

class Student():
    def __init__(self, age, height, weight):
        self.age = int(age)
        self.height = int(height)
        self.weight = int(weight)

class Students():
    def __init__(self, *students):
        self.students = list(students)

    # implementation of height() and weight() would be similar
    def age(self):
        return mean(map(lambda x: x.age, self.students))

    def add(self, student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def partecipanti(self):
      # for i in range(len(self.students))
      return '{}'.format(self.students[1])

students = Students(Student('15', '123', '33'))

students.add(Student('99', '144', '28'))
students.add(Student('20', '134', '22'))

print(students.partecipanti())

class squadra:
  def __init__(self,nome,punteggio):
    self.nome=nome
    self.punteggio=int(punteggio)
  def name(self):
    return '{}'.format(self.nome)
  def score(self):
    return '{}'.format(self.punteggio)

squadra_1=squadra('SQUADRA A', 10)
squadra_2=squadra('SQUADRA B', 20)

print(squadra_1.name())
print(squadra_2.name())
print(squadra_1.score())
print(squadra_2.score())

class campionato:
  def __init__(self, *squadra):
    self.campionato=list(squadra)

  def partecipanti(self):
    return '{}'.format(self.campionato)

camp=campionato(squadra('SQUADRA A', 10))

print(campionato.partecipanti())






class campionato:
  def __init__(self, *punti):
    self.punti = list(punti)

  def add(self, punto):
    self.punti.append(punto)
    
  def baricentro(self):
    x_c=mean(map(lambda a: a.x, self.punti))
    y_c=mean(map(lambda a: a.y, self.punti))
    return np.array([x_c,y_c])

punti = Punti(Punto('15', '123'))

punti.add(Punto('99', '144'))
punti.add(Punto('20', '134'))

print(punti.baricentro())
print(type(punti.baricentro()))

class Student():
    def __init__(self, age, height, weight):
        self.age = int(age)
        self.height = int(height)
        self.weight = int(weight)

class Students():
    def __init__(self, *students):
        self.students = list(students)

    # implementation of height() and weight() would be similar
    def age(self):
        return mean(map(lambda x: x.age, self.students))

    def add(self, student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)

students = Students(Student('15', '123', '33'))

students.add(Student('99', '144', '28'))
students.add(Student('20', '134', '22'))

print(students.age())

      

class Punto:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
    
  def coordinates(self):
    return '{} {} {}'.format(self.x, self.y, self.z) 

  def change(self,new_x,new_y,new_z):
    x=new_x
    y=new_y
    z=new_z
    self.x=x
    self.y=y
    self.z=z
    return self

  def distance(self,other_x,other_y,other_z):
    dist=math.sqrt((float(self.x)-float(other_x))**2+(float(self.y)-float(other_y))**2+(float(self.z)-float(other_z))**2)
    return dist

punto_1 = Punto(1,2,1000)
punto_2 = Punto(3,4,1500)

print(punto_1.coordinates()) # qui non serve (emp_1)
print(type(Punto.coordinates(punto_1))) # stessa cosa della riga di sopra, ma qui serve (emp_1)

punto_1.change(5,6,7)
print(punto_1.coordinates())


D=punto_1.distance(1,2,3)
print(D)


class Employee:
  def __init__(self,first,last,pay):
    self.first=first
    self.last=last
    self.pay=pay
    self.email=first+'.' +last+ '@company.com'
    
  def fullname(self):
    return '{} {}'.format(self.first, self.last) 

emp_1 = Employee('Giulio','Simoni',1000)
emp_2 = Employee('Test','User', 1500)

emp_1.fullname() # qui non serve (emp_1)
print(Employee.fullname(emp_1)) # stessa cosa della riga di sopra, ma qui serve (emp_1)
  



import numpy as np

data = np.loadtxt("src/ex2_data_python_4.txt", dtype='f') # 'f'='float'

X=[]
Y=[]
for i in range(len(data)):
  for j in range(2):
    if j==0:
      X.append(data[i][j])
    else:
      Y.append(data[i][j])

print(X)
print(Y)

coordinatesCenter = []

def findCenter(xList, yList, coordinates):
  xCenter=np.sum(xList)/len(xList)
  yCenter=np.sum(yList)/len(yList)
  coordinates.append(xCenter)
  coordinates.append(yCenter)
  return coordinates


findCenter(X,Y, coordinatesCenter)

np.array(coordinatesCenter)

print(coordinatesCenter)