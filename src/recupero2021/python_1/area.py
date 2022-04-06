p=30
l=12

def quadrato(perimetro):
  area=(perimetro/4)**2
  return area
def rettangolo(perimetro, lato):
  area=lato*(perimetro/2-lato)
  return area
def cerchio(perimetro):
  area=3.14*(perimetro/6.28)**2
  return area
def triangolo_rettangolo(perimetro, lato):
  ipotenusa=(0.5*perimetro**2+lato**2-perimetro*lato)/(perimetro-lato)
  area=lato*(perimetro-ipotenusa-lato)/2
  return area

print(quadrato(p))
print(rettangolo(p,l))
print(cerchio(p))
print(triangolo_rettangolo(p,l))