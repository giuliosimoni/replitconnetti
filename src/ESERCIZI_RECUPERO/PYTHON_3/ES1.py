elenco_disponibili = {"Farenheit 451": 10, "Zibaldone": 7, "Aristotle's Metaphysics": 5, "L'Alchimista": 1, "Harry Potter": 2, "Cime tempestose": 1}

domanda=str('YES')
while domanda=='YES':
  Titolo_a_scelta=str(input('Titolo a scelta: '))
  a=False
  for libro in elenco_disponibili:
    if libro==Titolo_a_scelta:
      n= elenco_disponibili[libro]-1
      elenco_disponibili[libro] = n
      if n==0:
        print('WARNING')
        # del elenco_disponibili[libro]
      a=True
  print(a)
  print(elenco_disponibili)
  
  domanda=str(input('Continuare: '))

print('end')
