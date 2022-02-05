xa=float(input("xa: "))
xb=float(input("xb: "))
ya=float(input("ya: "))
yb=float(input("yb: "))

def distance (i,j,k,l):
  dis=((i-j)**2+(k-l)**2)**0.5
  return dis

l=distance (xa,xb,ya,yb)
print("Distance is: ",l)