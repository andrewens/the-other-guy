"""
This is the main interface for all game simulation code.
"""

import os
import importlib

agents_directory_name = "agents"
agent_modules = {} # string agent_name --> <Module>

class GameSimulation:
    def __init__(self, agent1_name, agent2_name, agent3_name):
        if agent1_name not in agent_modules:
            raise Exception(str(agent1_name) + " is not the name of an agent module!")
        if agent2_name not in agent_modules:
            raise Exception(str(agent2_name) + " is not the name of an agent module!")
        if agent3_name not in agent_modules:
            raise Exception(str(agent3_name) + " is not the name of an agent module!")
        
        self._agent1 = agent_modules[agent1_name].Agent()
        self._agent2 = agent_modules[agent2_name].Agent()
        self._agent3 = agent_modules[agent3_name].Agent()
        
    def run(self):
        cards_left = list(range(1, 14)) # TODO randomize this list of cards
        log = []
        
        agent1_cards_left = set(range(1, 14))
        agent2_cards_left = set(range(1, 14))
        agent3_cards_left = set(range(1, 14))
        
        agent1_score = 0
        agent2_score = 0
        agent3_score = 0

        while len(cards_left) > 0:
            auctioned_card = cards_left.pop()

            agent1_card = self._agent1.play_card(auctioned_card)
            agent2_card = self._agent2.play_card(auctioned_card)
            agent3_card = self._agent3.play_card(auctioned_card)
            
            # make sure agents are being honest
            if agent1_card not in agent1_cards_left:
                raise Exception(f"Agent1 played a {agent1_card} twice!")
            if agent2_card not in agent2_cards_left:
                raise Exception(f"Agent2 played a {agent1_card} twice!")
            if agent3_card not in agent3_cards_left:
                raise Exception(f"Agent3 played a {agent1_card} twice!")

            agent1_cards_left.remove(agent1_card)
            agent2_cards_left.remove(agent2_card)
            agent3_cards_left.remove(agent3_card)
            
            # if two agents play the same card, the other agent wins the round.
            # otherwise no one wins
            winning_agent = None
            if agent2_card == agent3_card and agent3_card != agent1_card:
                winning_agent = 1
                agent1_score += auctioned_card
            elif agent3_card == agent1_card and agent1_card != agent2_card:
                winning_agent = 2
                agent2_score += auctioned_card
            elif agent1_card == agent2_card and agent2_card != agent3_card:
                winning_agent = 3         
                agent3_score += auctioned_card
            
            # results
            turn_log = {
                "auctioned_card": auctioned_card,
                "winning_agent": winning_agent,
                "agent1_card": agent1_card,
                "agent2_card": agent2_card,
                "agent3_card": agent3_card,
                "agent1_score": agent1_score,
                "agent2_score": agent2_score,
                "agent3_score": agent3_score,
            }
            log.append(turn_log)

        # calculate winning agent
        winning_agent = None
        if agent1_score > max(agent2_score, agent3_score):
            winning_agent = 1
        elif agent2_score > max(agent3_score, agent1_score):
            winning_agent = 2
        elif agent3_score > max(agent1_score, agent2_score):
            winning_agent = 3            

        return {
            "log": log,
            "agent1_final_score": agent1_score,
            "agent2_final_score": agent2_score,
            "agent3_final_score": agent3_score,
            "winning_agent": winning_agent
        }


def get_all_agent_module_names():
    return list(agent_modules.keys())

        
def run():
    for file_name in os.listdir(agents_directory_name):
        # get python modules
        if "__" in file_name:
            continue
        
        filename_without_extension, _ = os.path.splitext(file_name)
        module = importlib.import_module(agents_directory_name + "." + filename_without_extension)
        
        agent_modules[filename_without_extension] = module

