from black import ParameterSource


listaza = ["pelo", "cabeza", "ojo", "ojo", "pollo", "pata", "muslo", "muslo", "muslo", "tiro", "tiro"]
listonaza = ["berenjenas", 3, "pan rayado", 1,  "papa", 3,"leche", "sal"]
listaza.sort()
print(listaza)
nueva_lista = " "
palitos = []

for partes in listaza:
    if partes == nueva_lista:
        print("doppleganger")
    else:
        palitos.append(partes)
    nueva_lista = partes
print(palitos)

r = ["piston", "uculele", "porotos","remolacha"]
j = [1, 2, 3, 4]
rj = zip(r,j)
print(type(rj))
list[rj]
print(rj)
