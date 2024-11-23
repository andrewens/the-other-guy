import config
import test_runner
import the_other_guy


def main():
    the_other_guy.run()

    if config.testing_mode:
        test_runner.run()

    # insert code for the main experiment here
    #Experiment = GameSimulation(test_agent, test_agent, test_agent)
    #Experiment.run() # --> dictionary { int winner, List score[agent_index] }




main()
