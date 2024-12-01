import the_other_guy

def run():
    # running a simulation throws an error if you pass an invalid agent module name
    success = True
    try:
        the_other_guy.run_simulation("test_agent", "test_agent", "this_isnt_an_agent_name")
    except:
        success = False
        
    if success:
        raise Exception("GameSimulation failed to error when given a bad agent name")
    