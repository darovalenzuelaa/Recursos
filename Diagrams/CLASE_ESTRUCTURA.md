```mermaid
classDiagram
class Pokemon {
  +nombre : string
  +vida : int
  +ataque : int
  +nivel : int
  -experiencia : int

  +PokemonStats(nombre : string, vida : int, ataque : int)
  +get_experiencia() : int
  +set_experiencia(nueva_exp : int) : void
  +atacar(enemigo : Pokemon) : void
  +ganar_experiencia(exp : int) : void
  +subir_nivel() : void
  +evolucionar() : void
  +esta_derrotado() : bool
}
```

-----------------------------------
## **¿Qué entendió sobre las relaciones?**
Existen distintos tipos de relaciones:

**1. Herencia:** Sirve para distinguir cada clase con sus respectivas características o también para enlazar una subclase a la clase principal lo cual sería la relación de herencia. Es decir que las subclases heredan todos los métodos y atributos de la superclase.

**2. Abstracción:** Se pone en cursiva cuando podría ser una clase abstracta.

**3. Asociación:** Es una asociación básica sin que dependa de donde proviene.

**4. Agregación:** Es un tipo de asociación donde se especifica un todo y sus partes. Se podría hacer una subclase enlazada a otra subclase lo que nos permite agregar una relación.

**5. Composición:** Esta no puede existir fuera del todo, por lo que esta subclase no puede existir separada de la clase principal de la que deriva.

**6. Multiplicidad:** Permite definir recepciones numéricas en las relaciones lo que nos permite definir cantidades según corresponda el caso.

¿su clase de ejemplo que creo tiene relaciones con otras clases? ¿por qué? fundamente (min 5 líneas máx. 30).
