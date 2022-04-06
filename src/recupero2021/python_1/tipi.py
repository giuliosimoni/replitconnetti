intero_a = 1
intero_b = 2
float_a = 3.14159
float_b = 2.718
complesso_a = 1 + 2j
complesso_b = 3 - 5j
booleano_a = True
booleano_b = False
stringa_a = "hello"
stringa_b = "world"
print(intero_a + intero_b)
print(float_a + float_b )
print(complesso_a + complesso_b)
print(booleano_a and booleano_b )
print(stringa_a + stringa_b )
print(str(complesso_a)+str(complesso_b))
print(str(float_a)+str(float_b))

stringa_a = "5"
stringa_b = "-3"
print(stringa_a + stringa_b ) #explicit
print(float(stringa_a) + float(stringa_b) ) #explicit
print(int(stringa_a) + int(stringa_b) ) #explicit
print(intero_a + float_a) #implicit
print(intero_a / intero_b) #implicit