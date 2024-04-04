from crewai import Crew, Process

from tasks import CustomTasks
from agents import CustomAgents

tasks = CustomTasks()
agents = CustomAgents()


comic = agents.comedian()

need_jokes = tasks.tell_joke(comic)

crew = Crew(
    agents=[comic],
    tasks = [need_jokes],
    verbose=2,
    share_crew=False,
    process=Process.sequential
)

result = crew.kickoff()