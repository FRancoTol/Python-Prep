liston = []
t = -1
while t > -16:
    if( t % 2 == 0):
        print("el numero", (t),"es par")
    liston.append(t)
    t -= 1
print(liston)

for g in range(-16,-1):
    if(g % 2 == 0):
        print((g), "es par")
    else:
        print((g), "no es par")

for put, pit in enumerate(liston):
    print(put, pit)

lista = [1,2,5,7,8,10,13,14,15,17,20]
for k in range(1,21):
    if(not(k in lista)):
        lista.insert((k -1), k)
print(lista)

fibo =[0,1]
lo = 2
while lo < 30:
    fibo.append(fibo[lo-1] + fibo[lo-2])
    lo += 1
print(fibo)

li = 25

while li < 30:
    print(fibo[li]/fibo[li-1])
    li += 1

cadena = "Hola, Mundo. Esta es una practia del lenguaje de programacion de Python"

for orden, letra in enumerate(cadena):
    if( letra == "n"):
        print(orden)

diccionando = { "libro" : ["geralt de rivia"], 
                "titulos" : ["el ultimo deseo", "la espada del destino", "la sangre de los elfos", "tiempo de odio"],
                "material" : ["tapa dura cartone", "hoja cocida"]}

print(diccionando)

for h in (diccionando):
    print(h)

for f in list(cadena):
    print(f)

sylvester = ["metralleta", "arco", "cuchillo"]
arnold = ["escopeta", "machine gun", "brazo robotico"]
indestructibles = zip(sylvester, arnold)
indestructibles = tuple(indestructibles)
print(indestructibles)
div_7 = []
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

for r in lis:
    if(r % 7 == 0):
        div_7.append(r)
print(div_7)
