nuemro1 = float(input("por favor introduzaca un número:"))
es_igual = nuemro1 == 5
print(f"el número es igual a 5:{es_igual}")
es_igual_2 = (nuemro1 == 5.0)
print(f"el número es igual a 5.0:{es_igual_2}")
es_mayor_que_menor_que = nuemro1 > 0 or nuemro1 < 10
print(f"el número es mayor que 0 y menor que 10: {es_mayor_que_menor_que}")
es_menor_que_mayor_que = nuemro1 < 0 or nuemro1 > 10
print(f"el número es menor que 0 o mayor que 10:{es_menor_que_mayor_que}")
es_igual_y_mayor_que =  nuemro1 ==5 or nuemro1 > 10 and nuemro1 < 20
print(f"Elnúmeroes igual a 5, o es mayor que 10 y menor que 20: {es_igual_y_mayor_que}")