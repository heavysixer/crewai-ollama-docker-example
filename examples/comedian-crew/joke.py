from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv
load_dotenv() 


from langchain_community.llms import Ollama
ollama = Ollama(model=os.getenv("LLM_MODEL_NAME"),
                base_url=os.getenv("LLM_BASE_URL")
)

comic = Agent(
    role='comedian',
    goal='tell me a joke',
    backstory='You are an AI comedian',
    tools=[],
    verbose=True,
    llm=ollama, # Ollama model passed here
    allow_delegation=False
)

need_jokes = Task(description='tell me a joke',
                  expected_output='a joke',
                  agent=comic
                  )

crew = Crew(
    agents=[comic],
    tasks = [need_jokes],
    verbose=2,
    share_crew=False,
    process=Process.sequential
)

result = crew.kickoff()