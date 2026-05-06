## Diagrama de flujo para proyecto Pokemon en python.

```mermaid
flowchart TD

A[Inicio] --> B[Crear pokemon1 y pokemon2]
B --> C[turno = 1]

C --> D{Ambos vivos}

D -- No --> Z[Fin]

D -- Si --> E[Mostrar turno]

E --> F[pokemon1 ataca]
F --> G{pokemon2 derrotado}

G -- Si --> H[Mostrar derrota]
H --> I[Ganador gana experiencia]

G -- No --> J[pokemon2 ataca]

J --> K{pokemon1 derrotado}

K -- Si --> H

K -- No --> L[turno = turno + 1]
L --> D

I --> M{Experiencia suficiente}

M -- Si --> N[Subir nivel]
M -- No --> Z

N --> O{Nivel 36}

O -- Si --> P[Evolucionar]
O -- No --> Z

P --> Z
```

## Prompt Utilizado para la generación del ejemplo de flujo"

[prompt](prompt_flowchart.md)

