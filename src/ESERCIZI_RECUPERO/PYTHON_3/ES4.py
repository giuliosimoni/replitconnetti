cancelletti=input("Enter the number of #: ")
if cancelletti.replace('-','').isdigit()==True:
  numero=int(cancelletti)
  if numero>0:
    for i in range(numero):
      print("#",end=" ")
  else:
    print('not positive')
    
else:
  print('not a number')


