```python```

creación del constructor

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

que es self? es un argumento que hace referencia a sí mismo, es decir, al objeto y permite tener acceso a los a tributos y métodos de la clase

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

        
que es def?  es un comando para crear funciones


como accedo a un atributo del personaje? hay que crear la función con el comando self, luego los print con lo que se quiere mostrar y luego los atributos correspondientes. luego se escribe la función a través de la variable y luego se ejecutan todos los print dentro del método

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)
        
¿como accedo a un método de la clase personaje?

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

se escribe def, luego el nombre del método y entre paréntesis self agregando el nombre de los atributos, luego se modifican las estadísticas con la suma del valor actual y su incremento

```python```
[personaje](personaje.py)

# Encapsulación

¿cómo se encapsula código en python?
¿para que se usan los métodos get y set en el código?
¿se puede acceder a los método o atributos una vez encapsulados? justifique min 3 líneas
