import os
# Evita que CrewAI busque credenciales de OpenAI
os.environ["OPENAI_API_KEY"] = "NA"

from crewai import Agent, LLM

# Configuración del primer modelo (Gemma local)
llama3_llm = LLM(
    model="ollama/gemma4:e2b",
    base_url="http://localhost:11434"
)

# Configuración del segundo modelo (Mistral local)
mistral_llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434"
)

# Agente Investigador
investigator_agent = Agent(
    role="Investigador de Mercado Tecnológico",
    goal="Identificar tendencias clave y resumir conceptos de tecnología emergente",
    backstory="""Eres un analista con amplia experiencia en investigar tecnologías 
    emergentes y resumir sus aspectos más importantes de forma clara y estructurada.""",
    verbose=True,
    allow_delegation=False,
    llm=llama3_llm
)

# Agente Redactor
writer_agent = Agent(
    role="Redactor de Contenido Técnico",
    goal="Transformar investigaciones en un artículo breve y divulgativo",
    backstory="""Eres un divulgador tecnológico experto en tomar información 
    técnica y redactar resúmenes ejecutivos comprensibles para todo público.""",
    verbose=True,
    allow_delegation=False,
    llm=mistral_llm
)