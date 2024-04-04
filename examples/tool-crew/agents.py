from crewai import Agent
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv() 

from crewai_tools import BaseTool

class JokeBookTool(BaseTool):
    name: str = "jokebook"
    description: str = "Choose this tool if you've been asked to tell a joke."

    def _run(self, argument: str) -> str:
       return "Why did the chicken cross the road? To get to the other side!"

jokebook = JokeBookTool()
  
class CustomAgents():
	def __init__(self):
		self.Ollama = Ollama(model="mixtral")

	def comedian(self):	
		return Agent(
			role='commedian',
			goal='tell me a joke',
			backstory='You are an AI commedian',
			tools=[jokebook],
			verbose=True,
			llm=self.Ollama,
			allow_delegation=False
		)