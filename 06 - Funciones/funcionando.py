from math import fabs


#def factores_totales(varto):
    #cons = 1
    #while (varto) > 0:
        #cons = cons * (varto)
       #(varto) -= 1
    #return(cons)

#print(factores_totales(8))

def Factorialito(til):
    verdad = True
    for b in range(1,(til)):
        if(til % b == 0):
            verdad = False
            break
    return(verdad)

#print(Factorialito())

def factorialito_el_mas_grande(lista):
    primitos = []
    for elemento in lista:
        if Factorialito(elemento):
            primitos.extend(elemento)
    return primitos
listar = list(range(1,30))
primitos =(factorialito_el_mas_grande(listar))
print(primitos)