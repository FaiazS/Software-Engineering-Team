from crewai import Agent, Crew, Process, Task

from crewai.project import CrewBase, agent, crew, task

from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

@CrewBase
class SoftwareEngineeringTeam():

    """SoftwareEngineeringTeam crew"""

    agents_config = 'agents/yaml'

    tasks_config = 'tasks/yaml'

    
    @agent
    def engineering_lead(self) -> Agent:

        return Agent(

            config=self.agents_config['engineering_lead'],
            
            verbose=True
        )
    
    @agent
    def backend_engineer(self) -> Agent:

        return Agent(

            config = self.agents_config['backend_engineer'],

            verbose = True,

            allow_code_execution = True,

            code_execution_mode= 'safe',
        
            max_execution_time = 300,

            max_retry_limit = 7
        )
    
    @agent
    def frontend_engineer(self) -> Agent:

        return Agent(

            config = self.agents_config['frontend_engineer'],

            verbose = True

        )
    

    @agent
    def test_engineer(self) -> Agent:

        return Agent(

            config = self.agents_config['test_engineer'],
            
            verbose = True,

            allow_code_execution = True,

            code_execution_mode = 'safe',

            max_execution_time = 300,

            max_retry_limit = 7
        )


   
    @task
    def software_design_task(self) -> Task:

        return Task(

            config=self.tasks_config['software_design_task'] 
        )

    @task
    def backend_code_task(self) -> Task:

        return Task(

            config=self.tasks_config['backend_code_task']
            
        )
    
    @task
    def frontend_code_task(self) -> Task:

        return Task(

            config = self.tasks_config['frontend_code_task']
        )

    @task
    def unit_testing_task(self) -> Task:

        return Task(

            config = self.tasks_config['unit_testing_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SoftwareEngineeringTeam crew"""
        
        return Crew(

            agents=self.agents, 

            tasks=self.tasks, 

            process=Process.sequential,

            verbose=True
           
        )
