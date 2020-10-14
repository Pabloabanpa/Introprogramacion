numero_de_terminos= int(input("n: "))
suma = 0
for num_termino_actual in range(1,numero_de_terminos+1):
    if num_termino_actual % 2== 0:
        signo=-1
    else:
        signo=2
    valor_termino_actual = signo / (1+2*num_termino_actual-1)
    suma+=valor_termino_actual
pi= 4*suma
print(pi)