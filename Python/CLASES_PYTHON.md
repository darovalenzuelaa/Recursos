# 

## creación del constructor
```python
class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
´´´

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


[personaje](personaje.py)

# Encapsulación

¿cómo se encapsula código en python?
Un código se encapsula al poner doble guión bajo "__" delante del atributo o del método y así hacer privada o pública una función o métodos

¿para que se usan los métodos get y set en el código?
Se usan para acceder o modificar los atributos individualmente pero controlándolos. El "get" devuelve el atributo y "set" recibe uno nuevo para cambiarlo por el actual.

¿se puede acceder a los método o atributos una vez encapsulados? justifique min 3 líneas
Sí se puede acceder a los métodos o atributos una vez encapsulados y esto se hace a través de los métodos get o set. Además una vez el atributo se ha convertido en privado con el doble guión bajo, se puede acceder a este utilizando este nuevo nombre, es decir, con el "__". Se usa el nuevo nombre por ejemplo: print(cuenta._CuentaBancaria__pin)

[personaje_encapsulado](personaje_encapsulado.py)

## Herencia

1. ¿Por qué cuando se crea la clase guerrero al inicio heredando de la clase personaje genera error el código?
Genera error ya que la clase nos pide los atributos del personaje.

2. Cuando en el video se menciona la super clase, ¿a qué se refiere?
En caso de añadir un argumento más, este sería el constructor que nos permitiría la heredar los atributos en una nueva clase.

3. ¿Para qué se usa la instrucción pass en python? investigue
Se usa cuando python no admite que haya una sentencia que esté pegada al margen tras la definición de una función ya que la función sería como si estuviera vacía y no los tomaría como válidos. Esto nos permitiría seguir adelante con la buena interpretación del código a pesar de tener un error o algo pendiente.

4. ¿Qué es la función integrada super y para qué se usa, qué beneficio aporta?
Nos permite llamar a los atributos y métodos de la super clase sin tener que esciribirla directamente, esto nos permite el no usar "self" ya que viene implícito en el "super".

5. ¿En el video se menciona la herencia múltiple a que se refiere?
Es cuando se puede heredar los atributos de más de una clase a la vez.

6. ¿Cuál es el beneficio de aplicar herencia en POO?
La herencia en POO nos permite heredar varias clases a clases nuevas y así combinar nuevos atributos o comportamientos distintos al original. Además con la función "super" podemos acceder a los atributos de la clase base traspasando su funcionalidad a través de las subclases. Por lo tanto se pueden modificar nuevas variables sin perder una estructura clara en el código.

## Polimorfismo

1. ¿Para qué se usa el polimorfismo?
Se usa para crear funciones que reciban objetos con métodos que tengan el mismo nombre y así ejecutar acciones diferentes según la clase de ese objeto.

2. ¿En el método daño (self, enemigo) qué deberíamos hacer en el caso de que la fuerza sea menor a la defensa?
Se le podría poner que el daño mínimo sea 1, ya que sino se crearía un bucle.

## Ejemplo de polimorfismo

```python```

  class Guitarra():
     def que_es(self):
         print("Es una Guitarra")

 class Bateria():
     def que_es(self):
         print("Es una Batería")

 def definicion_instrumento(instrumento):
     instrumento.que_es()

 definicion_instrumento(Guitarra())

```python```
