firp = 4
tip = 1
while firp > 0:
        tip = tip * firp       
        firp -= 1
print(tip)

listonaza = ["berenjenas", 3, "pan rayado", 1,  "papa", 3,"leche", "sal"]
print(listonaza)
print(listonaza[3:6])
print(listonaza[:6])
print(listonaza[4:])
listonaza.append("pan")
print(listonaza)
listonaza.insert(3, "chokmpi")
print(listonaza)
listonaza.extend(["pelona", "pilcha", "manzana"])
print(listonaza)
print(listonaza.index("leche"))
listonaza.remove("pan")
print(listonaza)
print(listonaza.pop())
print(listonaza * 3)
listin = [1, 2, 3, 4, 5, 6, 7, 8]
listin.sort(reverse = True)
print(listin)
listillo = tuple(listin)
print(listillo)
print(listillo[1])
print(4 in listillo)
print(listillo.count(3))
diccionando = { "masa madre" : ["harina organica", "agua", "starter"],
                "pan campo" : ["pie", "harina", "agua", "sal"],
                "clave" : ("fermentacion en frio") ,
                "final": 24 }
print(diccionando["masa madre"])
diccionando["coccion"] = "fuego 250 por 30 min en olla"
print(diccionando["coccion"])
diccionando["final"] = "24 horas en frio de 5 grados"
print(diccionando)
del diccionando["coccion"]
print(diccionando)
palotes = {"pintorsco" : ["pintado", "pintor", "pincelada", "pinchar"],
           "lienzo" : (1,2,3,4,5,),
           "clavadito" :{ "adicionales" : ["pickles", "remolacha"],
                          "aderezos" : ["mayonesa", "platzulesa"]}}
print(palotes["clavadito"]["adicionales"])
print(palotes.keys())
print(len(diccionando))


