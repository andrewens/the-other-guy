import the_other_guy


def run():

    # we can run a simulation and get results in a dictionary
    sim = the_other_guy.GameSimulation("test_agent", "test_agent", "test_agent")
    results = sim.run()
    
    assert isinstance(results, dict)
   
    
    

