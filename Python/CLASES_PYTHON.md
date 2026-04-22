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
Un código se encapsula al poner doble guión bajo "__" delante del atributo o del método y así hacer privada o pública una función o métodos
¿para que se usan los métodos get y set en el código?
Se usan para acceder o modificar los atributos individualmente pero controlándolos. El "get" devuelve el atributo y "set" recibe uno nuevo para cambiarlo por el actual.
¿se puede acceder a los método o atributos una vez encapsulados? justifique min 3 líneas
Sí se puede acceder a los métodos o atributos una vez encapsulados y esto se hace a través de los métodos get o set. Además una vez el atributo se ha convertido en privado con el doble guión bajo, se puede acceder a este utilizando este nuevo nombre, es decir, con el "__". Se usa el nuevo nombre por ejemplo: print(cuenta._CuentaBancaria__pin)
