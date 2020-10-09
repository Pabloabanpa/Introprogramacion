
palabra_1 = input("Escriba una palabra: ")
palabra_2 = input("Escriba otra palbra: ")

if len(palabra_1)>len(palabra_2):
    print((palabra_1),":es la palabra mas larga ya que tiene",len(palabra_1),"caracteres")

elif len(palabra_1)<len(palabra_2):
    print((palabra_2),":es la palabra mas larga ya que tiene",len(palabra_2),"caracteres")

else :
    print("Las dos palabras tienen la misma longitud")

