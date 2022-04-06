






import random
number = random.randint(1,10)
print("The random number is: ", number)
attempt=int(input('insert number of attempts: '))
guess=int(input('insert your guess: '))
if guess != number:
  print('try again')
else:
  print('right')

while guess != number:
  for i in range(attempt):
    