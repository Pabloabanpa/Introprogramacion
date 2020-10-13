dia =  int(input("Ingrese su día de nacimineto:"))
mes = int(input("Ingrese su mes e nacimiento:"))
año = int(input("Ingrese su año de nacimiento:"))

from time import localtime
t = localtime(12, 10, 2020)
t.tm_mday

t.tm_mon

t.tm_year

