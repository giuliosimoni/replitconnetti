



a=float(input())
b=float(input())
c=float(input())

def minimo(x,y):
  if x < y:
    return x
  else:
    return y

def minore(i,j,k):
  n1=minimo(i,j)
  n2=minimo(i,k)
  smaller=minimo(n1,n2)
  return smaller
  
print(minore(a,b,c))