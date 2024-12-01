import the_other_guy

card_values = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 } # we use ints to represent cards
agent_values = { None, 1, 2, 3 } # we use integers or None to represent agents

def run():

    # we can run multiple games, which gives us more wins/losses, but cuts out the log
    results = the_other_guy.run_simulation("test_agent", "test_agent", "random_agent", n=10)
    
    agent1_wins = results["agent1_wins"]
    agent2_wins = results["agent2_wins"]
    agent3_wins = results["agent3_wins"]
    winning_agent = results["winning_agent"]
    
    assert isinstance(results, dict)
    assert isinstance(agent1_wins, int)
    assert isinstance(agent2_wins, int)
    assert isinstance(agent3_wins, int)
    assert isinstance(winning_agent, str)
    
    assert agent1_wins == 0
    assert agent2_wins == 0
    assert agent3_wins == 10
    assert winning_agent == "random_agent"
