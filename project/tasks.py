from crewai import Task
from agents import investigator_agent, writer_agent

# Tarea asignada al Agente 1 (Llama 3)
research_task = Task(
    description="""Investiga las principales ventajas de ejecutar modelos de lenguaje (LLMs) 
    de forma local frente al uso de APIs en la nube. Considera aspectos como privacidad, 
    costo, latencia y control.""",
    expected_output="""Un resumen en lista de puntos con los beneficios y desafíos clave 
    de usar LLMs locales.""",
    agent=investigator_agent
)

# Tarea asignada al Agente 2 (Mistral)
write_task = Task(
    description="""Toma los resultados de la investigación sobre LLMs locales y redacta 
    un artículo breve de 2 párrafos dirigido a desarrolladores que quieren empezar a usar Ollama.""",
    expected_output="""Un artículo claro y conciso de 2 párrafos en español.""",
    agent=writer_agent
)