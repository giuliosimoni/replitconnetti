import random

flag=True
while flag:
  num = input('Type a number for an upper bound: ')
  if num.isdigit():
    print("Let's play!")
    num = int(num)
    flag=False
  else:
    print('Invalid input: try again!')

secret = random.randint(1,num)


guess = None
count=1

while guess != secret:
  guess = input('Please type a number between 1 and ' + str(num) + ": ")
  if guess.isdigit():
    guess = int(guess)

  if guess == secret:
    print('You got it!')

  else:
    print('Please try again!')
    count += 1

print('It took you', count, 'guesses')








list=[2,3,4,8,5,4,2,4,3,2,3,2,2,2,3]

a=type(list[0])

search=input("Symbol to search: ")


def cerca(lista, simbolo):
  a=False
  k=0
  for l in lista:
    k+=1
    if l==simbolo:
      a=True
      k=posizione
  return a
      
cerca(list, search)

def occ_serach(list,number):
  count=0
  for i in list:
    if(i==number):
      count+=1
  return count

result=occ_serach(list,search)
if(result>0):
  print(result)
else:
  print("not found!")
print("with inbuilt function: ",list.count(search))