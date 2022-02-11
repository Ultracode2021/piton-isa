class Galeria:
    fotos=0
    texto=0
    senial=True
    marco="Hecho"
    almacenar=0

    def _init_(self):
        self.fotos=2
        self.texto=2

    def ver():
        pass
    def elegir(self):
        self.almacenar=5

class MiMega(Galeria):
    nombre = "Prueba"
    estilo= "Marca"

    def nombrar(self,nombre):
        self.nombre=nombre


class Portfolio(Galeria):
    nombre= "Privado"
    estilo= "Multi"



paleta=MiMega()
paleta.elegir()
print(paleta.almacenar)
