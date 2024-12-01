import the_other_guy

def run():
    # we can get a list of all agent module names from the_other_guy interface
    agent_module_names = the_other_guy.get_all_agent_module_names()
    
    assert isinstance(agent_module_names, list), "agent_module_names is not a list"
    
    # GameSimulation should throw an Exception if agents play the same card twice    
    success = True
    try:
        the_other_guy.run_simulation("test_agent", "test_agent", "cheating_agent")
    except Exception as e:
        success = False
        
    assert not success, "GameSimulation failed to throw error when an agent played the same card twice"
    
    # (same thing, but with n > 1)
    success = True
    try:
        the_other_guy.run_simulation("test_agent", "test_agent", "cheating_agent", n=10)
    except Exception as e:
        success = False
        
    assert not success, "GameSimulation failed to throw error when an agent played the same card twice, for n=10"
