horas_trabajadas = int(input("por favor introduzaca sus horas trabajadas:"))
pago_por_hora = float(input("ingrese la cantidad de su salario por hora:"))
pago_total = (horas_trabajadas) * (pago_por_hora)
mensaje = "monto a pagar:" + str(pago_total)
print(mensaje)