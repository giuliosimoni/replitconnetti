def print_hist(our_dict):
  for letter in sorted(our_dict.keys()):
    print(letter +" = "+"*"*our_dict[letter])
   
string='ababbccd'
alfabeto=list('abcdefghijklmnopqrstuvwxyz')
a=list(string)
print(a)

def occ_serach(list,symbol):
  count=0
  for i in list:
    if(i==symbol):
      count+=1
  return count

  
mydict={}
def freq(lis):
  for l in alfabeto:
    search=l
    result=occ_serach(lis,search)
    
    if result>0:
      risultato=result
      mydict[l] = result
             
  return risultato

freq(a)
print(mydict)    
print_hist(mydict)