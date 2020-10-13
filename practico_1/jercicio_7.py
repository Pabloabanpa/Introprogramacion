num = int(input("ingrese un número: "))
contador = 0
divisor = 0
for divisor in range(1,num+1):
    if num % divisor == 0 :
        print(divisor)
        contador += 1

print("el número ",num," tiene ",contador," divisores")