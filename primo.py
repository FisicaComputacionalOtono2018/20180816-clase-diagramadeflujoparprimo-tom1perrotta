#Autor: Tomas Gomez Gonzalez
#Fecha:17/08/2018
#Primo

n=input("Ingresa un numero: ")

i=2
p=0

if n==1:
  print"El numero 1 no es primo"
else:
  while i<n:
    aux=n%i
    if aux==0:
      p=1
    i=i+1

  if p==0:
    print"Es un numero primo"
  else:
    print"Es un numero compuesto"
