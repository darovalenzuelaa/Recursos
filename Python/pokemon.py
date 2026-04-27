class Pokemon:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = 35
        self.__experiencia = 0

    def get_experiencia(self):
        return self.__experiencia

    def set_experiencia(self, nueva_exp):
        if nueva_exp >= 0:
            self.__experiencia = nueva_exp

    def atacar(self, enemigo):
        enemigo.vida -= self.ataque
        if enemigo.vida < 0:
            enemigo.vida = 0
        print(f"{self.nombre} ha a atacado a {enemigo.nombre} y le quitó {self.ataque} de vida.")
        print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")

    def ganar_experiencia(self, exp):
        self.__experiencia += exp
        print(f"{self.nombre} ganó {exp} puntos de experiencia.")
        
        if self.__experiencia >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.__experiencia = 0
        self.vida += 20
        self.ataque += 5

        print(f"{self.nombre} subió al nivel {self.nivel}.")
        print(f"Nuevas estadísticas -> Vida: {self.vida}, Ataque: {self.ataque}")

        if self.nivel == 36:
            self.evolucionar()

    def evolucionar(self):
        print(f"¡{self.nombre} está evolucionando!")
        self.nombre = "Blaziken"
        self.vida += 30
        self.ataque += 10
        print(f"Ahora es {self.nombre}")
        print(f"Estadísticas mejoradas -> Vida: {self.vida}, Ataque: {self.ataque}")

    def esta_derrotado(self):
        return self.vida <= 0


pokemon1 = Pokemon("Combusken", 100, 20)
pokemon2 = Pokemon("Grovyle", 100, 15)

turno = 1

while not pokemon1.esta_derrotado() and not pokemon2.esta_derrotado():
    print(f"\n--- Turno {turno} ---")

    pokemon1.atacar(pokemon2)
    if pokemon2.esta_derrotado():
        print(f"{pokemon2.nombre} fue derrotado.")
        pokemon1.ganar_experiencia(100)
        break

    pokemon2.atacar(pokemon1)
    if pokemon1.esta_derrotado():
        print(f"{pokemon1.nombre} fue derrotado.")
        pokemon2.ganar_experiencia(100)
        break

    turno += 1