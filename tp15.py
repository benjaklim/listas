class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
    
    def __repr__(self):
        return f"{self.nombre} (Nivel: {self.nivel}, Tipo: {self.tipo}, Subtipo: {self.subtipo})"

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, pokemons):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = pokemons

    def porcentaje_batallas_ganadas(self):
        total_batallas = self.batallas_ganadas + self.batallas_perdidas
        return (self.batallas_ganadas / total_batallas) * 100 if total_batallas > 0 else 0

    def __repr__(self):
        return f"{self.nombre} (Torneos ganados: {self.torneos_ganados}, Batallas ganadas: {self.batallas_ganadas}, Batallas perdidas: {self.batallas_perdidas})\nPokemons: {self.pokemons}"

class LigaPokemon:
    def __init__(self):
        self.entrenadores = []

    def agregar_entrenador(self, entrenador):
        self.entrenadores.append(entrenador)

    def cantidad_pokemons(self, nombre_entrenador):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre_entrenador:
                return len(entrenador.pokemons)
        return 0

    def entrenadores_mas_de_tres_torneos(self):
        return [entrenador.nombre for entrenador in self.entrenadores if entrenador.torneos_ganados > 3]

    def pokemon_mayor_nivel(self):
        mayor_entrenador = max(self.entrenadores, key=lambda e: e.torneos_ganados, default=None)
        if mayor_entrenador:
            return max(mayor_entrenador.pokemons, key=lambda p: p.nivel, default=None)
        return None

    def mostrar_datos_entrenador(self, nombre_entrenador):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre_entrenador:
                return entrenador
        return None

    def entrenadores_mayor_porcentaje_batallas_ganadas(self, porcentaje):
        return [entrenador.nombre for entrenador in self.entrenadores if entrenador.porcentaje_batallas_ganadas() > porcentaje]

    def entrenadores_con_pokemon_tipo(self, tipo, subtipo):
        resultado = []
        for entrenador in self.entrenadores:
            for pokemon in entrenador.pokemons:
                if (pokemon.tipo == tipo and pokemon.subtipo == subtipo):
                    resultado.append(entrenador.nombre)
                    break
        return resultado

    def promedio_nivel_pokemons(self, nombre_entrenador):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre_entrenador:
                total_nivel = sum(pokemon.nivel for pokemon in entrenador.pokemons)
                return total_nivel / len(entrenador.pokemons) if entrenador.pokemons else 0
        return 0

    def entrenadores_con_pokemon_determinado(self, nombre_pokemon):
        return [entrenador.nombre for entrenador in self.entrenadores if any(pokemon.nombre == nombre_pokemon for pokemon in entrenador.pokemons)]

    def entrenadores_con_pokemons_repetidos(self):
        resultado = []
        for entrenador in self.entrenadores:
            nombres_pokemons = [pokemon.nombre for pokemon in entrenador.pokemons]
            if len(nombres_pokemons) != len(set(nombres_pokemons)):
                resultado.append(entrenador.nombre)
        return resultado

    def entrenadores_con_pokemons_especificos(self, nombres_pokemons):
        return [entrenador.nombre for entrenador in self.entrenadores if any(pokemon.nombre in nombres_pokemons for pokemon in entrenador.pokemons)]

    def entrenador_tiene_pokemon(self, nombre_entrenador, nombre_pokemon):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre_entrenador:
                for pokemon in entrenador.pokemons:
                    if pokemon.nombre == nombre_pokemon:
                        return (entrenador, pokemon)
        return (None, None)

liga = LigaPokemon()

liga.agregar_entrenador(Entrenador('Ash', 5, 20, 100, [
    Pokemon('Pikachu', 50, 'Eléctrico', ''),
    Pokemon('Charizard', 80, 'Fuego', 'Volador'),
    Pokemon('Bulbasaur', 45, 'Planta', 'Veneno')
]))

liga.agregar_entrenador(Entrenador('Misty', 3, 15, 85, [
    Pokemon('Starmie', 55, 'Agua', 'Psíquico'),
    Pokemon('Psyduck', 35, 'Agua', '')
]))

liga.agregar_entrenador(Entrenador('Brock', 1, 10, 60, [
    Pokemon('Onix', 70, 'Roca', 'Tierra'),
    Pokemon('Geodude', 40, 'Roca', 'Tierra')
]))

liga.agregar_entrenador(Entrenador('Gary', 4, 5, 95, [
    Pokemon('Blastoise', 85, 'Agua', ''),
    Pokemon('Eevee', 25, 'Normal', '')
]))

# a
print(f"Ash tiene {liga.cantidad_pokemons('Ash')} Pokémons")

# b
print(f"Entrenadores con más de tres torneos ganados: {liga.entrenadores_mas_de_tres_torneos()}")

# c
print(f"El Pokémon de mayor nivel del entrenador con más torneos ganados: {liga.pokemon_mayor_nivel()}")

# d
print(f"Datos del entrenador Ash: {liga.mostrar_datos_entrenador('Ash')}")

# e
print(f"Entrenadores con porcentaje de batallas ganadas mayor al 79%: {liga.entrenadores_mayor_porcentaje_batallas_ganadas(79)}")

# f
print(f"Entrenadores con Pokémons tipo fuego y planta o agua/volador: {liga.entrenadores_con_pokemon_tipo('Fuego', 'Volador')}")

# g
print(f"Promedio de nivel de los Pokémons de Ash: {liga.promedio_nivel_pokemons('Ash')}")

# h
print(f"Entrenadores que tienen a Pikachu: {liga.entrenadores_con_pokemon_determinado('Pikachu')}")

# i
print(f"Entrenadores con Pokémons repetidos: {liga.entrenadores_con_pokemons_repetidos()}")

# j
print(f"Entrenadores que tienen a Tyrantrum, Terrakion o Wingull: {liga.entrenadores_con_pokemons_especificos(['Tyrantrum', 'Terrakion', 'Wingull'])}")

# k
entrenador, pokemon = liga.entrenador_tiene_pokemon('Ash', 'Charizard')
if entrenador and pokemon:
    print(f"Entrenador {entrenador.nombre} tiene al Pokémon {pokemon.nombre}: {entrenador}, {pokemon}")
else:
    print("El entrenador no tiene al Pokémon.")
