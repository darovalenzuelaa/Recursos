print("Hola mundo! Soy Darío Valenzuela :D")

# Comentario de código

"""
Texto que no se va a interpretar
"""

# Variables
texto = "Siguiendo el tutorial"
nombre = "Darío Valenzuela"
altura = "No lo sé jeje"
year = 2099

print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada de Datos
"""
sitioweb = input("¿Cuál es tu página web?: ")
print("El sitio web del usuario es: " + sitioweb)
"""

# Condiciones
"""
altura = int(input("¿Cuál es tu altura?: "))

if altura >= 180:
    print("Eres una persona alta!")
else: 
    print("Eres bajito")
"""

# Funciones
"""
var_altura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura(altura):
    resultado = ""

    if altura >= 180:
        resultado = "Eres una persona alta!"
    else: 
        resultado = "Eres bajito"

    return resultado

print(mostrarAltura(var_altura))
"""

# Listas
personas = ["Darío", "Felipe", "Valenzuela"]

print(personas[2])

for persona in personas:
    print("-" + persona)

