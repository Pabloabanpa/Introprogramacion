

num_pal= int(input("Cantidad e palabras:"))
palabra_mas_larga = ""
for i in range(1,num_pal+1):
    palabra_actual= input(f"Ingrese palabras")
    if len(palabra_actual) >= len(palabra_mas_larga) :
        palabra_mas_larga=palabra_actual
print("la palabra mas larga es", palabra_actual)
for i in range(1,num_pal+1):
    palabra_actual= input(f"Ingrese palabras")
    if len(palabra_actual) <= len(palabra_mas_larga) :
        palabra_mas_larga=palabra_actual
print("la palabra mas corta es", palabra_actual)
