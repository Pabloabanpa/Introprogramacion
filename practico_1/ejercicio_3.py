num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba otro número: "))
cociente = num1//num2
resto = num1%num2

if resto==0 :
    print("La division es exacta")
else :
    print("la division no es exacta")
print(f"cociente:{cociente}")
print(f"resto:{resto}")
