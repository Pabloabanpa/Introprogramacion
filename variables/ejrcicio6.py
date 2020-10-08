peso_del_usuario = input("Intreduzca su peso en kg:")
estatura_del_usuario = float(input("Introduzaca su estatura en centimetros: "))

peso_en_kg = int(peso_del_usuario)
altura_en_metros = float(int(estatura_del_usuario) * 100)

imc = peso_del_usuario / estatura_del_usuario**2
print(f"tu idice de masa corporal es {imc} " )