#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario de lo contrario devuelva false.

print("Este programa incicara si el carcter ingresado es una vocal")

es_vocal=input("introduce un caracter :")

def vocal_F_V(v):

    if es_vocal == "a" or es_vocal == "e" or es_vocal == "i" or es_vocal == "o" or es_vocal == "u":
        print(True)
    if es_vocal == "A" or es_vocal == "B" or es_vocal == "I" or es_vocal == "O" or es_vocal == "U":
        print(True)
    else:
        print(False)

vocal_F_V(v="")
