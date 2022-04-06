l1=[]
l2=[]

l1=list(input("Enter (x_a;y_a): "))
l2=list(input("Enter (x_b;y_b): "))



xa=float(l1[1])
xb=float(l2[1])
ya=float(l1[3])
yb=float(l2[3])

print("xa: ",xa)
print("ya: ",ya)
print("xb: ",xb)
print("yb: ",yb)

def distance (i,j,k,l):
  dis=((i-j)**2+(k-l)**2)**0.5
  return dis

l=distance (xa,xb,ya,yb)
print("Distance is: ",l)