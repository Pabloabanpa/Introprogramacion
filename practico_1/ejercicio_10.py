# Este programa da como resultado la suma del tiempo en minutos de todos los tramos de un viaje.
tramo_1 = int(input("Ingrese el tiempo del primer tarmo:"))
tramo_2 =int(input("Ingrese la distania del segundo tramo:"))
tramo_3 = int(input("Ingese la distancia del ultimo tramo:"))

suma_de_tramos = tramo_1+tramo_2+tramo_3
resto1 = suma_de_tramos//60
resto2 = suma_de_tramos%60
print(f"El tiempo total de viaje: {resto1}:{resto2} horas")

