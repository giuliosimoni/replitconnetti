import math

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
