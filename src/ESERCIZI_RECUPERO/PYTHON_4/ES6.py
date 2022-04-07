g = lambda a: a + 10 # aggiunge 10

print(g(5))
print(g(7))
print(g(9))

animali = ['cani', 'gatti', 'scoiattoli', 'alci']
f = lambda animale: animale.capitalize() # cambia l'iniziale da minuscola a maiuscola 

for j in range(4):
  print(f(animali[j]))

a=float(input())
b=float(input())

k = lambda x, y: (x+y)*0.5

print(k(a,b))
