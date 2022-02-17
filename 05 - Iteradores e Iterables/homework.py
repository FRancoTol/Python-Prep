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
while lo < 31:
    fibo.append(fibo[lo-1] + fibo[lo-2])
    lo += 1
print(fibo)

print(sum(fibo))



while 2 == 2:
    print("ESTOY SOLITO, Y NO HAY NADIE AQUI A MI LADO")