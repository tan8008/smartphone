# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task

# # Uncomment the following line to use an example of a custom tool
# # from my_smartphone.tools.custom_tool import MyCustomTool

# # Check our tools documentations for more information on how to use them
# # from crewai_tools import SerperDevTool

# @CrewBase
# class MySmartphone():
# 	"""MySmartphone crew"""

# 	agents_config = 'config/agents.yaml'
# 	tasks_config = 'config/tasks.yaml'

# 	@agent
# 	def researcher(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['researcher'],
# 			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
# 			verbose=True
# 		)

# 	@agent
# 	def reporting_analyst(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['reporting_analyst'],
# 			verbose=True
# 		)

# 	@task
# 	def research_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['research_task'],
# 		)

# 	@task
# 	def reporting_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['reporting_task'],
# 			output_file='report.md'
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the MySmartphone crew"""
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			process=Process.sequential,
# 			verbose=True,
# 			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
# 		)

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class SmartphoneComparison():
    """Smartphone Comparison crew for analyzing and comparing smartphones"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['data_collector'],
            verbose=True
        )

    @agent
    def comparison_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['comparison_analyst'],
            verbose=True
        )

    @agent
    def price_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['price_analyst'],
            verbose=True
        )

    @task
    def collect_specs_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_specs_task'],
        )

    @task
    def compare_phones_task(self) -> Task:
        return Task(
            config=self.tasks_config['compare_phones_task'],
        )

    @task
    def analyze_prices_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_prices_task'],
            output_file='smartphone_comparison.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Smartphone Comparison crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
