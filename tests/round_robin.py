import the_other_guy

NUM_GAMES_PER_PERMUTATION = 10

def permutation(outcome, agent1, agent2, agent3, cheater_involved=False):
    if not isinstance(outcome, tuple):
        return False, f"Result for {agent1}, {agent2}, {agent3} is not a tuple"
    
    score1 = outcome[1]
    score2 = outcome[3]
    score3 = outcome[5]
    
    if not outcome[0] == agent1:
        return False, f"Outcome[0] is not '{agent1}'"
    if not outcome[2] == agent2:
        return False, f"Outcome[2] is not '{agent2}'"
    if not outcome[4] == agent3:
        return False, f"Outcome[4] is not '{agent3}'"
    
    if not isinstance(score1, int):
        return False, f"Outcome[1] is not an integer"
    if not isinstance(score2, int):
        return False, f"Outcome[3] is not an integer"
    if not isinstance(score3, int):
        return False, f"Outcome[5] is not an integer"
    
    if not 0 <= score1 <= NUM_GAMES_PER_PERMUTATION:
        return False, f"Outcome[1] is {score1}, which is not between 0 and {NUM_GAMES_PER_PERMUTATION}"
    if not 0 <= score2 <= NUM_GAMES_PER_PERMUTATION:
        return False, f"Outcome[3] is {score2}, which is not between 0 and {NUM_GAMES_PER_PERMUTATION}"
    if not 0 <= score3 <= NUM_GAMES_PER_PERMUTATION:
        return False, f"Outcome[5] is {score3}, which is not between 0 and {NUM_GAMES_PER_PERMUTATION}"
    
    should_be_successful = not cheater_involved
    if not outcome[6] == should_be_successful:
        return False, f"Outcome[6] is {outcome[6]}, which is not {should_be_successful}"

    if not isinstance(outcome[7], int):
        return False, f"Outcome[7] is not an integer"
    
    winner = 0
    if score1 > max(score2, score3):
        winner = 1
    if score2 > max(score3, score1):
        winner = 2
    if score3 > max(score1, score2):
        winner = 3
        
    if not outcome[7] == winner:
        return False, f"Outcome[7] is {outcome[7]}, which is not the winner ({winner})"
    
    return True


def run():

    # we can run games for every possible combination of given agents
    num_permutations = 27 # 3^3 = 27; all possible combinations of 3 agents
    results = the_other_guy.run_simulation(
        # you specify the TOTAL number of games to play so you don't accidentally crash your computer
        n = NUM_GAMES_PER_PERMUTATION * num_permutations,
        agents = ["test_agent", "random_agent", "cheating_agent"]
    )
    
    assert isinstance(results, list)
    assert len(results) == num_permutations 

    assert permutation(results[0], "test_agent", "test_agent", "test_agent")
    assert permutation(results[1], "test_agent", "test_agent", "random_agent")
    assert permutation(results[2], "test_agent", "test_agent", "cheating_agent", True) # note that there are duplicates of this just with different ordering
    assert permutation(results[3], "test_agent", "random_agent", "test_agent")
    assert permutation(results[4], "test_agent", "random_agent", "random_agent")
    assert permutation(results[5], "test_agent", "random_agent", "cheating_agent", True)
    assert permutation(results[6], "test_agent", "cheating_agent", "test_agent", True) # for example: this is duplicate! ^
    assert permutation(results[7], "test_agent", "cheating_agent", "random_agent", True)
    assert permutation(results[8], "test_agent", "cheating_agent", "cheating_agent", True)
    assert permutation(results[9], "random_agent", "test_agent", "test_agent")
    assert permutation(results[10], "random_agent", "test_agent", "random_agent")
    assert permutation(results[11], "random_agent", "test_agent", "cheating_agent", True)
    assert permutation(results[12], "random_agent", "random_agent", "test_agent")
    assert permutation(results[13], "random_agent", "random_agent", "random_agent")
    assert permutation(results[14], "random_agent", "random_agent", "cheating_agent", True)
    assert permutation(results[15], "random_agent", "cheating_agent", "test_agent", True)
    assert permutation(results[16], "random_agent", "cheating_agent", "random_agent", True)
    assert permutation(results[17], "random_agent", "cheating_agent", "cheating_agent", True)
    assert permutation(results[18], "cheating_agent", "test_agent", "test_agent", True)
    assert permutation(results[19], "cheating_agent", "test_agent", "random_agent", True)
    assert permutation(results[20], "cheating_agent", "test_agent", "cheating_agent", True)
    assert permutation(results[21], "cheating_agent", "random_agent", "test_agent", True)
    assert permutation(results[22], "cheating_agent", "random_agent", "random_agent", True)
    assert permutation(results[23], "cheating_agent", "random_agent", "cheating_agent", True)
    assert permutation(results[24], "cheating_agent", "cheating_agent", "test_agent", True)
    assert permutation(results[25], "cheating_agent", "cheating_agent", "random_agent", True)
    assert permutation(results[26], "cheating_agent", "cheating_agent", "cheating_agent", True)
