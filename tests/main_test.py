import the_other_guy


card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # we use ints to represent cards
agent_values = [None, 1, 2, 3] # we use integers or None to represent agents

def run():

    # we can run a simulation and get results in a dictionary
    sim = the_other_guy.GameSimulation("test_agent", "test_agent", "test_agent")
    results = sim.run()
    
    assert isinstance(results, dict)
    
    # results include a log of each card that was played by each agent every turn
    log = results["log"]
    
    assert isinstance(log, list), f"log is not a list"
    assert len(log) == 13, f"log length is {len(log)}"
    
    for i, turn in enumerate(log):
        card_being_auctioned = turn["auctioned_card"]
        agent1_card = turn["agent1_card"]
        agent2_card = turn["agent2_card"]
        agent3_card = turn["agent3_card"]
        winning_agent = turn["winning_agent"]
        
        assert card_being_auctioned in card_values
        assert agent1_card in card_values
        assert agent2_card in card_values
        assert agent3_card in card_values
        assert winning_agent in agent_values
        
    
    
   
    
    

