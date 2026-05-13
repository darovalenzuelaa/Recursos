## Base de Datos.

---------------------

**Ejemplos softwares de base de datos**

1. SQLite
2. Acces
3. MySQL
4. PostgreSQL
5. SQLServer

-----------------------

**Ejemplo Base de Datos**

**Clase:** Mascota

**-Nombre:** *String*

**-Raza:** *String*

**-Género:** *String*

**-Edad:** *Int*

---------------------------

**Tabla**

|ID|Nombre|Raza   |Género |Fecha de Nacimiento|Especie|
|--|------|-------|-------|-------------------|-------|
|1 |Carlos|Dálmata|M      |9 Marzo 2016       |Perro  |
|2 |Perla |Poodle |F      |13 Abril 2015      |Perro  |
|3 |Pepe  |Iguen  |M      |20 Noviembre       |Iguana |

------------------------------ 

**Modelo Entidad Relación (MER-ERM)**

|Mascota|                            
|-------|                        
|ID|                                  
|Nombre|
|Raza|
|Género|
|Fecha Nacimiento|
|Especie|

|Tutor|
|-----|
|ID|
|Nombre|
|Dirección|
|Correo|
|Teléfono|
|Rut|

*Poner foto*

--------------------------------------------

**¿Qué es una Base de Datos?**
Una Base de Datos es un sistema, software o método que nos sirve para almacenar datos el cual nos permite el uso de esta información de forma organizada. Nos permite recopilar y gestionar grandes cantidades de datos lo cual nos serviría para gestionar información ya sea en empresas, webs, apps, etc.

**¿Por qué en el ejemplo visto en clases es mejor usar float a cambios de int en el ingreso del campo edad?**
Sería mejor ya que **float** nos permite el uso de decimales, es decir, nos serviría para una edad dinámica, por ejemplo, 27,50 (27 años y 6 meses). Aunque la mejor opción es **date**.

**¿Por qué ingresar edad en un sistema de base de datos no es recomendable y cuál sería una mejor opción en este caso?**
No es recomendable ya que la edad es un dato variable que cambia todos los días lo que nos obligaría a actualizar manualmente las fechas.
Lo mejor sería usar la fecha de nacimiento pues sería un dato que no cambiaría.
Y la otra opción es usar el comando **date** ya que éste entiende como funcionan los días y los meses.
Se usa el formato AAAA-MM-DD. 1999-02-17

```sql
CREATE TABLE estudiantes (
    id INT,
    nombre VARCHAR(50),
    fecha_nacimiento DATE  -- Aquí le dices al sistema qué tipo de dato es
);
```







