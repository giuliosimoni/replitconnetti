a=range(1,10)
b=[el*2 for el in a]
print(b)

l=[1,2]
l2=['a','b']
l3=[4,5]
f=[(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]
print(f)

m=[]
for e1 in l:
  for e2 in l2:
    for e3 in l3:
      m.append((e1,e2,e3))
print(m)


import time
l=range(10000000)
v=range(1000000)
b=[el for el in l]
c=[el for el in v]
T1=time.process_time()
a=b+c
T2=time.process_time()
print(T2-T1,'s')
T3=time.process_time()
b.extend(c)
T4=time.process_time()
print(T4-T3,'s')