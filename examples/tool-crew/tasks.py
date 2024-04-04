from crewai import Task

class CustomTasks():
	def tell_joke(self, agent):
		return Task(description='tell me a joke',
			  expected_output='a joke',
			  agent=agent
			)
		