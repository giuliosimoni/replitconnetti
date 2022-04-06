point_a= str(input("Enter (x_a;y_a): "))
point_b= str(input("Enter (x_b;y_b): "))

x_a, y_a = map(float, point_a.strip('()').split(','))
x_b, y_b = map(float, point_b.strip('()').split(','))

print("(x_a;y_a): (",x_a,",",y_a,")")

print("(x_b;y_b): (",x_b,",",y_b,")")


def distance (i,j,k,l):
  dis=((i-j)**2+(k-l)**2)**0.5
  return dis

l=distance (x_a,x_b,y_a,y_b)
print("Distance is: ",l)