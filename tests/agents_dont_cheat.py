import the_other_guy

def run():
    # we can get a list of all agent module names from the_other_guy interface
    agent_module_names = the_other_guy.get_all_agent_module_names()
    
    assert isinstance(agent_module_names, list), "agent_module_names is not a list"
    
    # GameSimulation should throw an Exception if agents play the same card twice
    sim = the_other_guy.GameSimulation("test_agent", "test_agent", "cheating_agent")
    
    success = True
    try:
        sim.run()
    except Exception as e:
        success = False
        
    assert not success, "GameSimulation failed to throw error when an agent played the same card twice"
