### Práctica Python Orientado a Objetos

**1. Creación del constructor:**

```python
class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
```

**2. ¿Qué es self?: Es un argumento que hace referencia a sí mismo, es decir, al objeto y permite tener acceso a los a tributos y métodos de la clase.**

```python
class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
```
        
**3. ¿Qué es def?: Es un comando que sirve para crear funciones**

```python
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)  
        print("·Vida:", self.vida)
```

**4. ¿Cómo accedo a un atributo del personaje?:** Hay que crear la función con el comando self, luego los print con lo que se quiere mostrar y luego los atributos correspondientes. luego se escribe la función a través de la variable y luego se ejecutan todos los print dentro del método.

```python
mi_personaje = Personaje("Undertaker", 10, 1, 5, 100)
mi_personaje.atributos()
mi_personaje.subir_nivel(1, 2, 0)
mi_personaje.atributos()
```

**5. ¿Cómo accedo a un método de la clase personaje?:** Se escribe def, luego el nombre del método y entre paréntesis self agregando el nombre de los atributos, luego se modifican las estadísticas con la suma del valor actual y su incremento.

```python
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
```

[personaje](personaje.py)

------------

# Encapsulación

**1. ¿Cómo se encapsula código en python?:**
Un código se encapsula al poner doble guión bajo "__" delante del atributo o del método y así hacer privada o pública una función o métodos

**2. ¿Para que se usan los métodos get y set en el código?:**
Se usan para acceder o modificar los atributos individualmente pero controlándolos. El "get" devuelve el atributo y "set" recibe uno nuevo para cambiarlo por el actual.

**3.¿Se puede acceder a los métodos o atributos una vez encapsulados?:**
Sí se puede acceder a los métodos o atributos una vez encapsulados y esto se hace a través de los métodos get o set. Además una vez el atributo se ha convertido en privado con el doble guión bajo, se puede acceder a este utilizando este nuevo nombre, es decir, con el "__". Se usa el nuevo nombre por ejemplo: print(cuenta._CuentaBancaria__pin)

[personaje_encapsulado](personaje_encapsulado.py)

------------

## Herencia

**1. ¿Por qué cuando se crea la clase guerrero al inicio heredando de la clase personaje genera error el código?**
Genera error ya que la clase nos pide los atributos del personaje.

**2. Cuando en el video se menciona la super clase, ¿a qué se refiere?**
En caso de añadir un argumento más, este sería el constructor que nos permitiría la heredar los atributos en una nueva clase.

**3. ¿Para qué se usa la instrucción pass en python?**
Se usa cuando python no admite que haya una sentencia que esté pegada al margen tras la definición de una función ya que la función sería como si estuviera vacía y no los tomaría como válidos. Esto nos permitiría seguir adelante con la buena interpretación del código a pesar de tener un error o algo pendiente.

**4. ¿Qué es la función integrada super y para qué se usa, qué beneficio aporta?**
Nos permite llamar a los atributos y métodos de la super clase sin tener que esciribirla directamente, esto nos permite el no usar "self" ya que viene implícito en el "super".

**5. ¿En el video se menciona la herencia múltiple a que se refiere?**
Es cuando se puede heredar los atributos de más de una clase a la vez.

**6. ¿Cuál es el beneficio de aplicar herencia en POO?**
La herencia en POO nos permite heredar varias clases a clases nuevas y así combinar nuevos atributos o comportamientos distintos al original. Además con la función "super" podemos acceder a los atributos de la clase base traspasando su funcionalidad a través de las subclases. Por lo tanto se pueden modificar nuevas variables sin perder una estructura clara en el código.

------------

## Polimorfismo

**1. ¿Para qué se usa el polimorfismo?**
Se usa para crear funciones que reciban objetos con métodos que tengan el mismo nombre y así ejecutar acciones diferentes según la clase de ese objeto.

**2. ¿En el método daño (self, enemigo) qué deberíamos hacer en el caso de que la fuerza sea menor a la defensa?**
Se le podría poner que el daño mínimo sea 1, ya que sino se crearía un bucle.

## Ejemplo de polimorfismo

```python

  class Guitarra():
     def que_es(self):
         print("Es una Guitarra")

 class Bateria():
     def que_es(self):
         print("Es una Batería")

 def definicion_instrumento(instrumento):
     instrumento.que_es()

 definicion_instrumento(Guitarra())
```
------------

## Proyecto Final: [Pokemon].

**Esta clase está basada en el estilo de combate del videojuego Pokemon y lo elegí ya que de por sí ya tiene atributos que se pueden deducir fácilmente, y los que elegí son:**

**1. Nombre:** Los cuales serían "Combusken", el cual al ser el Pokemon que ganará el combate por tener mas ataque que el rival terminaría evolucionando a "Combusken" ya que al ganar el combate ganará experiencia que lo hará evolucionar.

**2. Vida:** Un atributo importante porque al acabarse la vida de un pokemon, este sería derrotado, de la misma forma, el otro pokemon sería vencedor lo que le permitirá ganar experiencia al ganar el combate.

**3. Ataque:** Este atributo es vital puesto hará que la vida le baje al rival en cada turno.

**4. Nivel:** El subir nivel tras ganar el combate hará que el pokemon evolucione, y el nivel esta puesto al nivel 35, por lo tanto al igual que en el juego real, el pokemon Combusken evolucionará al nivel 36 a Blaziken.

**5. Experiencia:** Es el atributo que nos permite subir de nivel y además es un atributo privado. Y funciona a través de un getter y un setter.



**En lo que respecta a los métodos el primero estos son:**

**1. Atacar:** Aquí se define el pokemon que ataca y el pokemon que recibe el daño (self, enemigo) respectivamente. Basícamente se le resta a la vida el daño de ataque del rival. Y se usa un if para que la vida llegue a 0 y no quede en numeros negativos. Luego simplemente se verbaliza lo ocurrido a través de un print.

**2. Ganar Experiencia:** Aquí se define que un personaje pueda ganar 100 de experiencia, y si llega a 100, este pokemon sube de nivel.

**3. Subir Nivel:** Esto sirve para sumar 1 nivel, lo que nos haría llegar al nivel 36 para evolucionar. Además nos sumaría estadísticas en los atributos vida y ataque. Como en el juego real.

**4. Evolucionar:** En este método el pokemon pasaría a ser un nuevo personaje ya que se le cambia el nombre (simulando una evolución), y al evolucionar sería un pokemon más fuerte aún por lo que se le sumarían aún más estadísticas.  

Finalmente se simula el combate usando un ciclo, con el comando "while" el cual se repite hasta que la vida de un pokemon llegue a 0 lo que significaría que el pokemon ha sido derrotado por lo tanto el ciclo se terminaría con el comando "break". Pero es importante recalcar que el ciclo revisa en cada turno si la vida del personaje ha llegado a 0, si no es así se pasaría al siguiente turno, hasta que la vida de algún pokemon llegue a 0.

------------

[Ver código de práctica final](pokemon.py)




