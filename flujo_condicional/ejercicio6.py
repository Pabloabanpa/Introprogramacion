#Este programa dira si tu año de nacimiento es bisiesto o no.
anno = int(input("Introzuca su año de nacimiento:"))
if anno/4:
    print("Su año es bisiesto.")
elif anno / 100:
    print("Su año no es bisiesto")
elif anno/400:
    print("Su año es bisiesto.")
else:
    print("Su año no es bisiesto.")

