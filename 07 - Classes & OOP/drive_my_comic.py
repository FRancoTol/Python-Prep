import string


class Comics:
    def __init__(self, calidad, portada, genero, editorial):
        
        self.calidad = calidad
        self.portada = portada
        self.genero = genero
        self.editorial = editorial
        self.vel = 0
        self.cantidad = 0

    def lectura(self, velocidad):
        self.vel += velocidad
    
    def fatiga(self, velocidad):
        '''
        emoingngeiwong
        '''
        self.vel -= velocidad
    
    def paginas_por_minuto(self, hojas):
        self.cantidad += hojas


    def ir_a_dormir(self):
        self.vel = (0)
        print("el vago ya no quiere leer y se va la cama y su marca paginas es apoyado en la pagina", (self.cantidad))


    def km_speedy(self):
        if self.vel == 0:
            print("¿cuando arrancamos maquina?")
        else:
            print("la velocidad de lectura es ahora de ", self.vel, "km")
    
    def lectulon(self):
        if self.cantidad == 0:
            print("la cantidad de hojas leidas es 0")
        else:
            print("la cantidad de hojas leidas es ahora de", self.cantidad)
    

    
sandman = Comics("prestige", "blanda", "mistery", "vertigo comics")
spiderman = Comics("absolute", "hardcover", "adventure", "marvel comics")
bloodshot = Comics("digital", "none", "gore/action/realist", "valiant comics")
sandman.fatiga(45)
sandman.lectura(100)
sandman.paginas_por_minuto(98)
print(sandman.km_speedy())
print(sandman.lectulon())
print(sandman.ir_a_dormir())

class Novela_Grafica(Comics):
    def ultra_serio(self):
        print("teta, sangre y filosofia barata salen despedidos de sus hojas como un manantial inagotable de presuntuosos genios")
        self.lectura(100)
        print("te hayas motivado por leer material rotulado como solo para jovenes adultos")
        





