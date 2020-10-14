# Este programa da como resultado la suma del tiempo en minutos de todos los tramos de un viaje.
tiempo= int(input("Duracion de tramo:"))
suma = 0
while tiempo>0:
    suma=tiempo+suma
    tiempo= int(input("Duracion de tramo:"))
operacion_1 = suma // 60
operacion_2 = suma % 60
if operacion_1 < 10:
    print(f"El tiempo total de viaje: {operacion_1}:0{operacion_2} horas")
else:
    print(f"El tiempo total de viaje: {operacion_1}:{operacion_2} horas")

