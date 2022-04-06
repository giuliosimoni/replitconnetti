from statistics import mean
import numpy as np

class Punto:
  def __init__(self,x,y):
    self.x=float(x)
    self.y=float(y)
    
class Punti:
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