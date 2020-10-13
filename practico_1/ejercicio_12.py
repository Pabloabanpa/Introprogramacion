p1 = input("Ingrese una palabra:")
p2 = input("Ingrese una palabra:")
p3 = input("Ingrese una palabra:")
p4 = input("Ingrese una palabra:")
p5 = input("Ingrese una palabra:")

if len(p1)>len(p2) and len(p1)>len(p3) and len(p1)>len(p4) and len(p1)>len(p5) :
    print(f"la lapabra mas parga es {p1} ")

elif len(p2)>len(p1) and len(p2)>len(p3) and len(p2)>len(p4) and len(p2)>len(p5) :
    print(f"la lapabra mas parga es {p2} ")

elif len(p3) > len(p1) and len(p3) > len(p2) and len(p3) > len(p4) and len(p3) > len(p5):
    print(f"la lapabra mas parga es {p3} ")

elif len(p4) > len(p1) and len(p4) > len(p3) and len(p4) > len(p2) and len(p4) > len(p5):
    print(f"la lapabra mas parga es {p4} ")

elif len(p5) > len(p1) and len(p5) > len(p3) and len(p5) > len(p4) and len(p5) > len(p2):
    print(f"la lapabra mas parga es {p5} ")

elif len(p5) < len(p1) and len(p5) < len(p3) and len(p5) < len(p4) and len(p5) < len(p2):
    print(f"la lapabra mas parga es {p5} ")

elif len(p5) < len(p1) and len(p5) < len(p3) and len(p5) < len(p4) and len(p5) < len(p2):
    print(f"la lapabra mas corta es {p5} ")
