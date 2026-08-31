![Logo](images/logo_crewai)

## Presentado por

- Juan Diaz
- Daniel Tejada

## 1. Descripción general del framework

[**CrewAI**](https://github.com/crewAIInc/crewAI) es un framework de código abierto para Python orientado a la construcción de sistemas de **IA multiagente**.

Su concepto principal es el de un **Crew**, que representa un equipo de agentes de IA que colaboran para alcanzar un objetivo común.

Cada agente puede tener:

* Un rol específico.
* Un objetivo.
* Un contexto o experiencia definida mediante `backstory`.
* Herramientas.
* Tareas específicas.
* Un modelo de lenguaje.

CrewAI también incorpora **Flows**, que permiten controlar el flujo de ejecución de una aplicación, manejar estados, eventos, condiciones y combinar diferentes equipos de agentes.

De forma simplificada, podemos representar su arquitectura así:

```text
                    ┌─────────────────────┐
                    │        FLOW         │
                    │   Orquestación      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        CREW         │
                    │ Equipo de agentes   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │Investigador│   │  Analista  │   │  Revisor   │
       │   Agent    │   │   Agent    │   │   Agent    │
       └────────────┘   └────────────┘   └────────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                       Resultado final
```

Una forma sencilla de entenderlo es:

> **Los Agents realizan el trabajo, los Crews coordinan la colaboración y los Flows controlan el flujo general de la aplicación.**

---

# 2. Tipo de framework

CrewAI puede clasificarse principalmente como un framework **basado en roles y multiagente**, aunque también incorpora características importantes de los frameworks **orientados a workflows**.

| Tipo                    | CrewAI                            |
| ----------------------- | --------------------------------- |
| Basado en workflows     | ✅ Sí                              |
| Basado en grafos        | ⚠️ No es su abstracción principal |
| Basado en roles         | ✅ Sí                              |
| Multiagente             | ✅ Sí                              |
| Orientado a eventos     | ✅ Sí, mediante Flows              |
| Orquestación de agentes | ✅ Sí                              |
| Manejo de estado        | ✅ Sí                              |

Por lo tanto, una clasificación apropiada sería:

> **CrewAI = Role-based + Multi-agent + Workflow orchestration**

## Arquitectura basada en roles

Los agentes normalmente se definen a partir de un rol, un objetivo y un contexto.

Por ejemplo:

```text
Investigador
     ↓
Busca y analiza información

Redactor
     ↓
Construye el contenido

Revisor
     ↓
Evalúa y mejora el resultado
```

Cada agente tiene una responsabilidad diferente.

Esto hace que CrewAI sea especialmente intuitivo para problemas que pueden dividirse en diferentes roles.

---

## Arquitectura basada en workflows

Además de los `Crew`, CrewAI proporciona `Flows`.

Un `Flow` permite controlar cómo se ejecuta una aplicación y puede encargarse de:

* Mantener el estado.
* Ejecutar diferentes pasos.
* Controlar eventos.
* Implementar condiciones.
* Realizar bifurcaciones.
* Ejecutar diferentes Crews.
* Integrar lógica Python con agentes.

Por ejemplo:

```text
                 FLOW
                   │
                   ▼
            Investigación
                   │
                   ▼
              Análisis
                   │
                   ▼
             Generación
                   │
                   ▼
             Validación
                   │
                   ▼
             Resultado
```

La diferencia conceptual es:

```text
Crew
 ↓
Colaboración entre agentes

Flow
 ↓
Control de la aplicación
```

---

# 3. Adecuación para sistemas multiagente y escalabilidad

CrewAI está diseñado específicamente para construir **sistemas multiagente**.

Un `Crew` puede contener varios agentes especializados, donde cada uno tiene una responsabilidad diferente.

Por ejemplo, para construir un sistema de investigación:

```text
                  Research Crew
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   Investigador      Analista        Revisor
        │               │               │
        ▼               ▼               ▼
   Buscar datos     Analizar       Validar
                    información     resultados
```

Los agentes pueden tener:

* Diferentes roles.
* Diferentes objetivos.
* Diferentes herramientas.
* Diferentes modelos.
* Diferentes tareas.

## Ejecución secuencial

Una de las formas más sencillas de coordinar agentes es mediante una ejecución secuencial.

```text
Agente A
   ↓
Agente B
   ↓
Agente C
   ↓
Resultado
```

El resultado de una tarea puede convertirse en contexto para la siguiente.

Este enfoque es útil cuando existe una dependencia clara entre las tareas.

---

## Ejecución jerárquica

También es posible utilizar una estructura donde un agente actúa como coordinador o administrador de otros agentes.

```text
                 Manager
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Agente A  Agente B  Agente C
```

El agente administrador puede coordinar el trabajo y delegar responsabilidades.

Esto resulta útil cuando el problema requiere una coordinación más dinámica.

---

## Escalabilidad

CrewAI permite comenzar con una arquitectura sencilla:

```text
Usuario
   ↓
Agente
   ↓
Resultado
```

y posteriormente evolucionar hacia arquitecturas más complejas:

```text
                         Usuario
                            │
                            ▼
                           Flow
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          Research Crew          Analysis Crew
                 │                     │
        ┌────────┼────────┐     ┌──────┴──────┐
        ▼        ▼        ▼     ▼             ▼
    Agente A  Agente B  Agente C Agente D  Agente E
                 │                     │
                 └──────────┬──────────┘
                            ▼
                       Validación
                            │
                            ▼
                       Resultado
```

Para aplicaciones más grandes, el `Flow` puede utilizarse como capa superior de orquestación, mientras que los `Crew` se encargan de tareas que requieren colaboración entre agentes.

---

# 4. Gestión de memoria

CrewAI proporciona mecanismos de **memoria** para que los agentes puedan conservar y reutilizar información.

La memoria puede ser útil para mantener:

* Información de conversaciones anteriores.
* Información relevante de tareas anteriores.
* Contexto.
* Información sobre entidades.
* Datos que pueden ser reutilizados posteriormente.

Conceptualmente:

```text
                    Agente
                      │
                      ▼
                 Sistema de memoria
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Memoria     Memoria     Memoria
      temporal     a largo     entidades
                    plazo
```

Por ejemplo:

```text
Interacción 1:

Usuario:
"Mi empresa utiliza Python."


Interacción 2:

Usuario:
"¿Qué lenguaje utilizamos?"

Agente:
"Python..."
```

La segunda respuesta puede beneficiarse de información almacenada previamente.

## Memoria vs. estado del Flow

Es importante diferenciar estos dos conceptos.

### Memoria

Permite conservar información que puede ser reutilizada posteriormente.

### Estado del Flow

Permite mantener información necesaria durante la ejecución de un workflow.

Por ejemplo:

```python
from pydantic import BaseModel


class Estado(BaseModel):
    tema: str = ""
    investigacion: str = ""
    resultado: str = ""
```

El estado puede utilizarse para compartir información entre diferentes pasos del workflow.

En términos simples:

```text
Memoria
→ Información que se conserva y puede reutilizarse.

Estado
→ Información necesaria para controlar una ejecución.
```

---

# 5. Soporte para herramientas

Una de las capacidades importantes de CrewAI es permitir que los agentes utilicen **herramientas (Tools)**.

Una herramienta permite que un agente pueda realizar acciones más allá de simplemente generar texto.

Algunos ejemplos son:

* Búsquedas web.
* APIs.
* Bases de datos.
* Funciones de Python.
* Lectura y procesamiento de archivos.
* Servicios externos.
* Herramientas personalizadas.

La arquitectura puede verse así:

```text
                    Agente
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Web Search   Database     Python
        Tool         Tool        Tool
```

También podemos crear nuestras propias herramientas.

Por ejemplo, una herramienta para calcular impuestos:

```python
from crewai.tools import tool


@tool
def calcular_impuesto(valor: float, tasa: float) -> float:
    """Calcula el impuesto sobre un valor."""
    return valor * tasa
```

Después podemos asignarla a un agente:

```python
from crewai import Agent


analista = Agent(
    role="Analista financiero",
    goal="Analizar información financiera",
    backstory="Eres un analista financiero experimentado.",
    tools=[calcular_impuesto]
)
```

De esta manera, el agente puede utilizar la herramienta cuando sea necesaria.

El flujo conceptual sería:

```text
                    Agente
                       │
                       ▼
               Analiza el problema
                       │
                       ▼
              ¿Necesita una Tool?
                 │           │
                Sí           No
                 │           │
                 ▼           ▼
             Ejecutar      Generar
              Tool         respuesta
                 │
                 ▼
           Analizar resultado
                 │
                 ▼
              Continuar
```

---

# 6. Ventajas y desventajas

## Ventajas

### 1. Especialización mediante roles

Cada agente puede especializarse en una responsabilidad concreta.

Por ejemplo:

```text
Investigador
Analista
Programador
Redactor
Revisor
Administrador
```

Esto permite dividir problemas complejos en tareas más pequeñas.

### 2. Soporte nativo para sistemas multiagente

La colaboración entre agentes es uno de los principales objetivos del framework.

El desarrollador no necesita implementar desde cero toda la lógica de coordinación.

### 3. Orquestación mediante Flows

Los `Flows` permiten tener un mayor control sobre la aplicación:

* Estado.
* Eventos.
* Condiciones.
* Ejecución.
* Ramificaciones.
* Integración entre diferentes Crews.

### 4. Facilidad para crear prototipos

La abstracción de alto nivel permite construir prototipos de sistemas multiagente relativamente rápido.

---

## Desventajas

### 1. Mayor consumo de recursos

Cada agente puede generar llamadas adicionales al modelo.

Por ejemplo:

```text
1 agente
 ↓
1 llamada al LLM
```

frente a:

```text
Investigador
 ↓
Redactor
 ↓
Revisor
 ↓
Varias llamadas al LLM
```

Esto puede aumentar:

* Latencia.
* Consumo de tokens.
* Costos.
* Uso de recursos.

### 2. Comportamiento no determinista

Al estar basados en modelos de lenguaje, los agentes pueden producir resultados diferentes ante situaciones similares.

Por ejemplo, pueden:

* Elegir diferentes herramientas.
* Generar respuestas diferentes.
* Delegar tareas de manera diferente.
* Necesitar diferentes cantidades de iteraciones.

### 3. Debugging más complejo

A medida que aumenta el número de agentes, también aumenta la dificultad para identificar el origen de un problema.

Por ejemplo:

```text
Flow
 ↓
Crew A
 ├── Agent 1
 ├── Agent 2
 └── Agent 3
      ↓
Crew B
 ├── Agent 4
 └── Agent 5
```

Cuando ocurre un error, puede ser necesario analizar diferentes agentes, tareas, herramientas y pasos del workflow.

---

# 7. Ejemplo de código

El siguiente ejemplo muestra un sistema multiagente sencillo.

El objetivo será crear un pequeño informe sobre un tema utilizando dos agentes:

1. **Investigador:** recopila y organiza información.
2. **Redactor:** utiliza la investigación para generar el informe.

```python
from crewai import Agent, Task, Crew, Process


# ============================================================
# AGENTES
# ============================================================

investigador = Agent(
    role="Investigador",
    goal="Encontrar información relevante sobre el tema",
    backstory=(
        "Eres un investigador experimentado especializado "
        "en encontrar y organizar información relevante."
    ),
    verbose=True
)


redactor = Agent(
    role="Redactor técnico",
    goal="Crear un informe claro utilizando la investigación",
    backstory=(
        "Eres un redactor técnico experimentado capaz "
        "de transformar información compleja en explicaciones claras."
    ),
    verbose=True
)


# ============================================================
# TAREAS
# ============================================================

tarea_investigacion = Task(
    description=(
        "Investiga el siguiente tema: {tema}. "
        "Identifica los conceptos más importantes, "
        "sus ventajas y sus aplicaciones prácticas."
    ),
    expected_output=(
        "Un resumen estructurado con la información "
        "más importante sobre el tema."
    ),
    agent=investigador
)


tarea_redaccion = Task(
    description=(
        "Utilizando la investigación realizada, "
        "crea un informe técnico sobre {tema}."
    ),
    expected_output=(
        "Un informe técnico claro que incluya introducción, "
        "conceptos principales, ventajas y conclusión."
    ),
    agent=redactor
)


# ============================================================
# CREW
# ============================================================

crew = Crew(
    agents=[
        investigador,
        redactor
    ],
    tasks=[
        tarea_investigacion,
        tarea_redaccion
    ],
    process=Process.sequential,
    verbose=True
)


# ============================================================
# EJECUCIÓN
# ============================================================

resultado = crew.kickoff(
    inputs={
        "tema": "Sistemas de IA multiagente"
    }
)

print(resultado)
```

## Flujo de ejecución

El código implementa el siguiente flujo:

```text
                    Usuario
                       │
                       ▼
              Agente investigador
                       │
                       ▼
              Tarea de investigación
                       │
                       ▼
                  Investigación
                       │
                       ▼
                 Agente redactor
                       │
                       ▼
                Tarea de redacción
                       │
                       ▼
                 Informe final
```

La idea importante es que los agentes tienen **roles diferentes y responsabilidades diferentes**.

El investigador se concentra en obtener y organizar información, mientras que el redactor utiliza ese contexto para producir el resultado final.

---

# 8. ¿Cuándo utilizar CrewAI?

CrewAI resulta especialmente interesante cuando un problema puede dividirse naturalmente en diferentes responsabilidades.

Algunos casos de uso son:

* Sistemas de investigación.
* Generación de contenido.
* Análisis de información.
* Desarrollo de software asistido por agentes.
* Automatización de procesos empresariales.
* Sistemas de atención al cliente.
* Sistemas de toma de decisiones.
* Workflows que requieren múltiples agentes especializados.

Una regla sencilla podría ser:

```text
Problema sencillo
        │
        ▼
   LLM / Agent
```

```text
Problema complejo
con responsabilidades diferentes
        │
        ▼
   Multi-Agent / Crew
```

```text
Aplicación compleja
con múltiples etapas y control
        │
        ▼
     Flow
       +
     Crew
       +
    Agents
```

---

# 9. Resumen

CrewAI es un framework orientado a la construcción de **sistemas de IA multiagente**, basado principalmente en roles y con capacidades de orquestación mediante workflows.

Sus principales abstracciones son:

| Componente | Función                                           |
| ---------- | ------------------------------------------------- |
| `Agent`    | Agente especializado que realiza trabajo          |
| `Task`     | Define el trabajo que debe realizarse             |
| `Crew`     | Coordina la colaboración entre agentes            |
| `Flow`     | Controla el workflow y el estado de la aplicación |
| `Tool`     | Permite interactuar con sistemas externos         |
| `Memory`   | Permite conservar y reutilizar información        |

La idea central puede resumirse en:

> **Agents proporcionan inteligencia especializada, Crews permiten la colaboración y Flows proporcionan control sobre el workflow.**

Por esta razón, CrewAI resulta especialmente adecuado para aplicaciones donde una tarea compleja puede dividirse en diferentes roles y donde varios agentes necesitan colaborar para alcanzar un resultado.


## Referencias

https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai

https://www.ibm.com/think/topics/crew-ai

https://www.ibm.com/mx-es/think/topics/crew-ai


<https://www.markdownguide.org>
<fake@example.com>

https://medium.com/@tahirbalarabe2/what-is-crew-ai-collaborative-autonomous-agent-framework-cbffc7926e1b

