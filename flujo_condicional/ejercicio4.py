#Este programa claculará tu monto a pagar de acuerdo a tu consumo.
consumo= int(input("Indeque su consumo de agua en m3:"))
if consumo<100 :
    print("Su monto a pagar es de: 1.00bs.")

elif consumo>100 and consumo<499:
    print("Su monto a paagar es de: 1.20bs. ")

elif consumo>500 and consumo<999:
    print("Su monto a pagar es de: 1.50bs. ")

elif consumo>1000:
    print("Su monto a pagar es de: 2.00bs.")

else:
    print("nonto no registrado.")

