#Este programa es te dará el nivel de riesgo de contraer alguna enfermedad relacionada a tu peso corporal.
peso = float(input("Intoduzza su peso en kg:"))
altura = float(input("Introduzca su altua:"))
edad= int(input("Introduzca su edad:"))
imc= peso/altura**2

if imc<22.0 and edad<45 :
    print("Riesgo bajo.")
if imc<22.0 and edad>45:
    print("Risgo medio.")
if imc>22.0 and edad<22.0:
    print("Riesgo medio.")
if imc>22.0 and edad>45:
    print("Riesgo alto.")
