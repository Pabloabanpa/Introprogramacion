num = int(input("Introduzca un número:"))
def collatz(num):
    sec=[num]
    while num > 1:
        if num%2==0:
            num//=2
        else :
            num = num*3+1
        sec.append(num)
    return sec
secuencia = collatz(num)

for i in secuencia :
    print(i,end=" ")

#falta la parte grafica
