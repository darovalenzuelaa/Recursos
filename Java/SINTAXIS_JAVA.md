## Texto, Números, Booleanos, Listas, Objetos

---------------------------

## Textos.

Hay que crear una variable con "String", luego el nombre de la variable, luego "=" y finalmente entre comillas se escribe el texto.

**Ejemplo:**

```java
public class Main {
    public static void main(String[] args) {
        String libro = "Hola que tal"
    }
}
```

---------------------------

## Números.

**1. Número telefónico o color. Guardar número.**

```java
public class Main {
    public static void main(String[] args) {
        String telf = "677 607 65";
        String colr = "amarillo";
    }
}
```

**2. Números enteros y decimales.**
Guardar número. Se utiliza la palabra "int", y decimales con "double" y booleanos con "boolean".

```java
class Main {
    public static void main(String[] args) {
        
        int entero = 100;
        double decimal = 1.13747;
        
    }
}
```

---------------------------

## Booleanos.
Son valores de verdadero o falso.

```java
class Main {
    public static void main(String[] args) {
        
       boolean autorizado = true;
       boolean seleccionado = false;

    }
}
```

---------------------------

## Listas.

Se utiliza "ArrayList", además "<Integer>" que nos sirve para números enteros y luego se añaden puntos a la lista llamando al método "add".

**1. Lista de números.**

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> números = new Arraylist<Integer>();
            números.add(1);
            números.add(2);
            números.add(3);
            números.add(4);
            números.add(5);
            System.out.println(números.get(0));
    }
}
```

**2. Lista de texto.**

```java
class Main {
    public static void main(String[] args) {
        
        String[] animales = { "perro", "gato", "tigre" };
        
    }
}
```

**3. Lista con datos mixtos**

```java
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {

        List<Object> datosMixtos = new ArrayList<Object>();
        datosMixtos.add("texto");
        datosMixtos.add("69");
        datosMixtos.add(true);
        String[] lista = { "lista dentro de otra lista" };
        datosMixtos.add(lista);

    }
}
```

---------------------------

## Objetos.

## HashMap. 

**Un HashMap es una tabla o mapa el cual nos permite acceder a una propiedad utilizando una llave. En el ejemplo se utiliza la llave "7" para abrir el valor "Cristiano Ronaldo". Por lo tanto se utiliza para acceder de forma muy rápida a un valor a través de una llave única. Y existen HashMap de texto a texto y HashMap de texto a lista de texto, entre otros. Y este se importa a través de "import java.util.HashMap;" además de "String" que sería el tipo de la clave y "Integer" que sería el tipo de valor.**

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, String> jugadores = new Hashmap<Integer, String>();
        jugadores.put(10, "Messi");
        jugadores.put(7, "Cristiano Ronaldo");
        System.out.println(jugadores.get(7));

    }
}
```
----------------------

## Módulos.

Los módulos nos permiten dividir un código entre muchos archivos lo que nos permite organizarnos y trabajar mejor con ellos además de crear un objeto a partir de la clase.

**Javac:** Este comando compila la clase que se indique por lo que crea una nueva clase, lo que significa que compila una clase que nos sirve para correr la clase externa en el archivo main. En resumen así es como se crean las bibliotecas.



