import matplotlib 
import matplotlib.pyplot as p

xList=list()
yList=list()
for i in range(20):
  xList.append(i)
  yList.append(i**2)

p.plot(xList,yList,'-gx')
p.xlabel("integers")
p.savefig("src/graph2.png")