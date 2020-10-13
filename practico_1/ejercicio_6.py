print("Este es un progma que ordena los números por su valor de menor a mayor.")
num1 = int(input("Ingrese el primernúmero por favor:"))
num2 = int(input("Ingrese el segundo número por favor:"))
num3 = int(input("Imgrese el ultimo númeor por favor:"))

min = min(num1,num2,num3)
max = max(num1,num2,num3)
mid = (num1+num2+num3)-min-max
print(min,"  ",mid,"  ", max)



