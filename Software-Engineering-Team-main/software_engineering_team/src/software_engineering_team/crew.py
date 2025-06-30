from crewai import Agent, Crew, Process, Task

from crewai.project import CrewBase, agent, crew, task

from crewai.agents.agent_builder.base_agent import BaseAgent

from pathlib import Path

import os

from typing import List

from crewai_tools import FileWriterTool

import yaml

tool_functions = {
    'crewai_tools.FileWriterTool': lambda: FileWriterTool()
}

@CrewBase
class SoftwareEngineeringTeam():

    """SoftwareEngineeringTeam crew"""

    # Get the directory where this script is located
    current_dir = Path(__file__).parent
    agents_config = str(current_dir / 'config' / 'agents.yaml')
    tasks_config = str(current_dir / 'config' / 'tasks.yaml')

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

            allow_tool_use = True,

            tools=[FileWriterTool()],

            code_execution_mode= 'safe',
        
            max_execution_time = 300,

            max_retry_limit = 7
        )
    
    @agent
    def frontend_engineer(self) -> Agent:

        return Agent(

            config = self.agents_config['frontend_engineer'],

            verbose = True,

            allow_code_execution = True,

            allow_tool_use = True,

            tools=[FileWriterTool()],

            execute_locally = True,

            code_execution_mode = 'safe',

            max_execution_time = 300,

            max_retry_limit = 7

        )
    

    @agent
    def test_engineer(self) -> Agent:

        return Agent(

            config = self.agents_config['test_engineer'],
            
            verbose = True,

            allow_code_execution = True,

            allow_tool_use = True,

            tools=[FileWriterTool()],

            execute_locally = True,

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
    def qa_task(self) -> Task:

        return Task(

            config = self.tasks_config['qa_task']
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
