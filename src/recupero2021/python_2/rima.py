parola_1='andare'
parola_2=str(input())


lista_1=tuple(parola_1)
lista_2=tuple(parola_2)


inizio_1=(len(parola_1))-3
fine_1=(len(parola_1))

inizio_2=(len(parola_2))-3
fine_2=(len(parola_2))


print(lista_1[inizio_1:fine_1])
print(lista_2[inizio_2:fine_2])

if lista_1[inizio_1:fine_1]==lista_2[inizio_2:fine_2]:
  print('le parole sono in rima')
else:
  print('le parole NON sono in rima')