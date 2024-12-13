#Note: This is the replacement code from Claude app. Remember to remove
#the original code from each file (crew.py, tasks.yaml, agents.yaml & pyproject.toml) and
#use the replacement code.

# crew.py
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

# main.py
#!/usr/bin/env python
import sys
import warnings
from smartphone_comparison.crew import SmartphoneComparison

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_smartphone_inputs():
    """Get smartphone inputs from user"""
    smartphones = []
    print("Enter three smartphones to compare (e.g., 'iPhone 15 Pro Max'):")
    for i in range(3):
        smartphone = input(f"Smartphone {i+1}: ")
        smartphones.append(smartphone)
    return smartphones

def run():
    """Run the crew."""
    smartphones = get_smartphone_inputs()
    inputs = {
        'smartphones': smartphones
    }
    SmartphoneComparison().crew().kickoff(inputs=inputs)

def train():
    """Train the crew for a given number of iterations."""
    smartphones = get_smartphone_inputs()
    inputs = {
        'smartphones': smartphones
    }
    try:
        SmartphoneComparison().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """Replay the crew execution from a specific task."""
    try:
        SmartphoneComparison().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """Test the crew execution and returns the results."""
    smartphones = get_smartphone_inputs()
    inputs = {
        'smartphones': smartphones
    }
    try:
        SmartphoneComparison().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()

# config/agents.yaml
data_collector:
  role: >
    Smartphone Specifications Expert
  goal: >
    Gather detailed technical specifications and features for the requested smartphones
  backstory: >
    You're a technical expert specializing in smartphone specifications and features.
    You have extensive knowledge of various smartphone models and their technical details.
    Your strength lies in collecting and organizing comprehensive device information.

comparison_analyst:
  role: >
    Smartphone Comparison Specialist
  goal: >
    Analyze and compare different smartphone models based on their specifications and features
  backstory: >
    You're an experienced analyst who excels at comparing different smartphone models.
    You understand what features matter most to users and can provide meaningful
    comparisons that help people make informed decisions.

price_analyst:
  role: >
    Smartphone Market and Pricing Expert
  goal: >
    Analyze pricing trends and provide detailed price comparisons across different markets
  backstory: >
    You're a market analyst specializing in smartphone pricing and value analysis.
    You have deep knowledge of smartphone pricing across different regions and retailers,
    and can provide comprehensive price comparisons and value assessments.

# config/tasks.yaml
collect_specs_task:
  description: >
    Collect detailed specifications and features for the smartphones: {smartphones}.
    Include key specifications like:
    - Display (size, technology, resolution)
    - Processor
    - RAM and Storage options
    - Camera specifications
    - Battery capacity
    - Special features
  expected_output: >
    A comprehensive list of specifications and features for each smartphone
  agent: data_collector

compare_phones_task:
  description: >
    Using the collected specifications, create a detailed comparison between {smartphones}.
    Focus on:
    - Key differentiating features
    - Performance comparisons
    - Camera capabilities
    - Battery life expectations
    - Build quality and design
    - Unique selling points
  expected_output: >
    A detailed comparison highlighting the strengths and weaknesses of each smartphone
  agent: comparison_analyst

analyze_prices_task:
  description: >
    Analyze and compare the prices of {smartphones}.
    Include:
    - Current market prices
    - Price variations across different storage options
    - Regional price differences (if applicable)
    - Value for money assessment
    - Available deals or discounts
    - Price history and trends
  expected_output: >
    A comprehensive price analysis and value assessment for each smartphone, formatted in markdown
  agent: price_analyst
