stringa='Puoi modificare la tua scelta, in qualsiasi momento, accedendo al pannello delle preferenze'
 
print(stringa.lower())
print(stringa.upper())
 
lista=tuple(stringa)
 
search='n'
 
def occ_serach(lista,symbol):
  count=0
  for i in lista:
    if(i==symbol):
      count+=1
  return count
 
result=occ_serach(lista,search)
if(result>0):
  print(result)
else:
  print("not found!")
print("with inbuilt function: ",lista.count(search))
 
print('momento' in stringa)
print('Momento' in stringa)
