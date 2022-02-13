
from ast import Break


print("PRUEBA DE EDAD DE TIMOTHY")
timmy = 0
while timmy < 16:
     print("rompela con timmy ", (timmy))
     timmy += 1
     if timmy > 15:
        print("rupert")


tic = 4
tip = 8

print("la variable tic es de tipo", type(tic))
print("la variable tip es del tipo", type(tip))

if(type(tic) == type(tip)):
        print("la variable ", (tic),"y la variable ", (tip), "son del mismo tipo")
else:
        print("ambas variabes no son del mismo tipo")
for t in range(1,21):
        if(t % 2 == 0):
                print("el numero", (t), "es par")
        else:
                print("el numero", (t), "es impar") 

for g in range(0,6):
        print((g), "a la tercera potencia es igual a", (g ** 3))
r = 0       
while r < tip+1:
        print(r)
        r += 1

h = 4
p = 1

#for g in range(1,h+1):
        #p = p * g
#print(p)

while h > 1:
        p = p * h
        h = h - 1
print(p)