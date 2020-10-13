from time import localtime
t=localtime()
t.tm_mday

t.tm_mon

t.tm_year

day= int(input("Ingrese su dia de nacimiento:"))
mes= int(input("Ingrese su mes de nacimiento:"))
anno= int(input("Ingrese su año de nacimiento:"))

edad= t.tm_year-anno

print("Usteed tiene",edad,"annos")
