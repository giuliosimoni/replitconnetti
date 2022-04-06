list_sent=["hello World","I love Python"]
our_dict={}
for sent in list_sent:
  for letter in sent:
    if letter.isalpha:
      if letter in our_dict.keys():
        our_dict[letter]+=1
      else:
        our_dict[letter]=1



def print_hist(our_dict):
  for letter in sorted(our_dict.keys()):
    print(letter +" = "+"*"*our_dict[letter])

print_hist(our_dict)
    
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
      print(result)
      risultato=result
      mydict[l] = result
         
     
  return risultato

freq(a)
print(mydict) 
mylist=list(mydict)
print(mylist)     

print_hist(mydict)

def histogram(list1):
  for i in range(len(list1)):
    for j in range(list1[i]):
      print('*',end='')
    print('')

lst=[]
ln=int(input("Enter List Length: "))
print("Enter ", ln," integers")
for i in range(ln):
  data=int(input())
  lst.append(data)

print("histogram({})".format(lst))
histogram(lst)




  
