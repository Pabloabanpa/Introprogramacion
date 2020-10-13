# Este es un prograa que emula la funcion de una calculadora

num1= int(input("Irtroduzca el primer número:"))
op= input("Introduzaca el operador:")
num2= int(input("Introduzaca el segundo número:"))

if op == ("+"):
    print(num1+num2)

elif op == ("-"):
    print(num1-num2)

elif op == ("*"):
    print(num1*num2)

elif op == ("/") :
    print(num1//num2)