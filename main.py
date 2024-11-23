import test_runner
import the_other_guy

def pretty_print_log(log):
    for i in range(13):
        turn_log = log[i]

        print(f"Turn #{i+1}")
        for key, value in turn_log.items():
            print(f"\t{key}: {value}")
        

def main():
    the_other_guy.run() # this just initializes the main simulation module
    test_runner.run() # comment this out if you don't want to run the system tests

    sim = the_other_guy.GameSimulation("test_agent", "test_agent", "test_agent") 
    # here we specify three agent module names to test those strategies in the simulation
    
    results = sim.run()
    # pretty_print_log(results["log"])


main()
