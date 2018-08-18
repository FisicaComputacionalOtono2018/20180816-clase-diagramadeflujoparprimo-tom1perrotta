#Autor: Tomas Gomez Gonzalez
#Fecha:17/08/2018
#Primo con Funcion

def primo(n,p):
  i=2
  p=0

  if n==1:
    p=1
  else
    while i<n:
    aux=n%i
    if aux==0:
      p=1
    i=i+1

  return p

#Inicio
n=input("Ingresa un numero: ")
p=1000
primo(n,p)

print "p="
print(p)

if p==1:
  print"El numero no es primo"
else:
  print"El numero es primo"
