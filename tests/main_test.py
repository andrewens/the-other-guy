import the_other_guy


card_values = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 } # we use ints to represent cards
agent_values = { None, 1, 2, 3 } # we use integers or None to represent agents

def run():

    # we can run a simulation and get results in a dictionary
    sim = the_other_guy.GameSimulation("test_agent", "test_agent", "random_agent")
    results = sim.run()
    
    assert isinstance(results, dict)
    
    # results include a log of each card that was played by each agent every turn
    log = results["log"]
    
    assert isinstance(log, list), f"log is not a list"
    assert len(log) == 13, f"log length is {len(log)}"
    
    agent1_score = 0
    agent2_score = 0
    agent3_score = 0
    
    for i, turn in enumerate(log):
        card_being_auctioned = turn["auctioned_card"]
        winning_agent = turn["winning_agent"]

        agent1_card = turn["agent1_card"] # will be same as agent 2
        agent2_card = turn["agent2_card"] # will be same as agent 1
        agent3_card = turn["agent3_card"] # will usually be different than agent 1 & 2, meaning it will win
        
        agent1_current_score = turn["agent1_score"] #log includes each agent's score at every turn
        agent2_current_score = turn["agent2_score"]
        agent3_current_score = turn["agent3_score"]

        assert card_being_auctioned in card_values
        assert agent1_card in card_values
        assert agent2_card in card_values
        assert agent3_card in card_values

        if agent3_card == agent2_card:
            assert winning_agent is None
        else:
            assert winning_agent is 3
            agent3_score += card_being_auctioned
            
        assert agent1_score == agent1_current_score
        assert agent2_score == agent2_current_score
        assert agent3_score == agent3_current_score

    assert results["winning_agent"] == 3 # technically it is possible for the random_agent to pick all the same cards as agents 1 & 2, but unlikely
    assert results["agent1_final_score"] == agent1_score
    assert results["agent2_final_score"] == agent2_score
    assert results["agent3_final_score"] == agent3_score
        
        
    
    
   
    
    

