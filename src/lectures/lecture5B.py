import matplotlib
import matplotlib.pyplot as p

xList=list()
yList=list()
for i in range(40):
  xList.append(i)
  yList.append(i**2)

p.plot(xList,yList,'--yo')
p.savefig("grafico.png")