import os

# Desactivar requerimiento de API Key asignando un valor ficticio
os.environ["OPENAI_API_KEY"] = "NA"

from crewai import Crew, Process
from agents import investigator_agent, writer_agent
from tasks import research_task, write_task

def main():
    crew = Crew(
        agents=[investigator_agent, writer_agent],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )

    print("### Iniciando la ejecución con Gemma 4:e2b y Mistral mediante Ollama ###\n")
    result = crew.kickoff()
    
    print("\n### Resultado Final ###\n")
    print(result)

if __name__ == "__main__":
    main()