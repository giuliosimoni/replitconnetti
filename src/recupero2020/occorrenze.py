list=[2,3,4,8,5,4,2,4,3,2,3,2,2,2,3]

search=int(input("number to search: "))

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