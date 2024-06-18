class Superheroe:
    def __init__(self, nombre, año_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.año_aparicion = año_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia
    
    def __repr__(self):
        return f"{self.nombre} ({self.casa_comic}, {self.año_aparicion}): {self.biografia}"

class ListaSuperheroes:
    def __init__(self):
        self.superheroes = []

    def agregar_superheroe(self, superheroe):
        self.superheroes.append(superheroe)

    def eliminar_superheroe(self, nombre):
        self.superheroes = [s for s in self.superheroes if s.nombre != nombre]

    def obtener_año_aparicion(self, nombre):
        for s in self.superheroes:
            if s.nombre == nombre:
                return s.año_aparicion
        return None

    def cambiar_casa_comic(self, nombre, nueva_casa):
        for s in self.superheroes:
            if s.nombre == nombre:
                s.casa_comic = nueva_casa
                break

    def superheroes_con_palabra(self, palabras):
        resultado = []
        for s in self.superheroes:
            if any(palabra in s.biografia.lower() for palabra in palabras):
                resultado.append(s.nombre)
        return resultado

    def superheroes_anteriores_a(self, año):
        resultado = []
        for s in self.superheroes:
            if s.año_aparicion < año:
                resultado.append((s.nombre, s.casa_comic))
        return resultado

    def casa_de_superheroe(self, nombres):
        resultado = {}
        for s in self.superheroes:
            if s.nombre in nombres:
                resultado[s.nombre] = s.casa_comic
        return resultado

    def informacion_superheroes(self, nombres):
        resultado = {}
        for s in self.superheroes:
            if s.nombre in nombres:
                resultado[s.nombre] = s
        return resultado

    def superheroes_por_letra(self, letras):
        resultado = {letra: [] for letra in letras}
        for s in self.superheroes:
            if s.nombre[0] in letras:
                resultado[s.nombre[0]].append(s.nombre)
        return resultado

    def contar_superheroes_por_casa(self):
        contador = {'Marvel': 0, 'DC': 0}
        for s in self.superheroes:
            if s.casa_comic in contador:
                contador[s.casa_comic] += 1
        return contador

lista_superheroes = ListaSuperheroes()

lista_superheroes.agregar_superheroe(Superheroe('Linterna Verde', 1940, 'DC', 'Usa un anillo de poder'))
lista_superheroes.agregar_superheroe(Superheroe('Wolverine', 1974, 'Marvel', 'Tiene garras retráctiles y un traje amarillo'))
lista_superheroes.agregar_superheroe(Superheroe('Dr. Strange', 1963, 'DC', 'Hechicero supremo'))
lista_superheroes.agregar_superheroe(Superheroe('Capitana Marvel', 1968, 'Marvel', 'Piloto con superpoderes'))
lista_superheroes.agregar_superheroe(Superheroe('Mujer Maravilla', 1941, 'DC', 'Guerrera amazona con armadura'))
lista_superheroes.agregar_superheroe(Superheroe('Flash', 1940, 'DC', 'El hombre más rápido'))
lista_superheroes.agregar_superheroe(Superheroe('Star-Lord', 1976, 'Marvel', 'Líder de los Guardianes de la Galaxia'))
lista_superheroes.agregar_superheroe(Superheroe('Batman', 1939, 'DC', 'El caballero oscuro'))
lista_superheroes.agregar_superheroe(Superheroe('Superman', 1938, 'DC', 'El hombre de acero'))
lista_superheroes.agregar_superheroe(Superheroe('Spider-Man', 1962, 'Marvel', 'El hombre araña'))

# a
lista_superheroes.eliminar_superheroe('Linterna Verde')

# b
print(f"Año de aparición de Wolverine: {lista_superheroes.obtener_año_aparicion('Wolverine')}")

# c
lista_superheroes.cambiar_casa_comic('Dr. Strange', 'Marvel')

# d
print(f"Superhéroes que mencionan 'traje' o 'armadura': {lista_superheroes.superheroes_con_palabra(['traje', 'armadura'])}")

# e
print(f"Superhéroes anteriores a 1963: {lista_superheroes.superheroes_anteriores_a(1963)}")

# f
print(f"Casas de Capitana Marvel y Mujer Maravilla: {lista_superheroes.casa_de_superheroe(['Capitana Marvel', 'Mujer Maravilla'])}")

# g
print(f"Información de Flash y Star-Lord: {lista_superheroes.informacion_superheroes(['Flash', 'Star-Lord'])}")

# h
print(f"Superhéroes por letra B, M, S: {lista_superheroes.superheroes_por_letra(['B', 'M', 'S'])}")

# i
print(f"Superhéroes por casa de comic: {lista_superheroes.contar_superheroes_por_casa()}")
