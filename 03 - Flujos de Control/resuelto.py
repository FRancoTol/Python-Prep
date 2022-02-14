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
print()

