list=[5,5,4,6,8,5,8,7,6]
search=5
def searchOccurrence(list,number):
  count=0
  for i in list:
    if (i==number):
      count+=1
  return count

result=searchOccurrence(list, search)
if (result>0):
  print("count is: ",result)
else:
  print("not found")
print("using inbuilt function: ", list.count(search))