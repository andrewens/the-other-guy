"""
This is the main interface for all game simulation code.
"""

import os

agent_module_names = {}

class GameSimulation:
    def __init__(self, agent1_name, agent2_name, agent3_name):
        if agent1_name not in agent_module_names:
            raise Exception(str(agent1_name) + " is not the name of an agent module!")
        if agent2_name not in agent_module_names:
            raise Exception(str(agent2_name) + " is not the name of an agent module!")
        if agent3_name not in agent_module_names:
            raise Exception(str(agent3_name) + " is not the name of an agent module!")
            
        
def run():
    for file_name in os.listdir("agents"):
        # get python modules
        if "__" in file_name:
            continue
        
        filename_without_extension, _ = os.path.splitext(file_name)
        
        agent_module_names[filename_without_extension] = True

