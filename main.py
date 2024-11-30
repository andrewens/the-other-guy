import test_runner
import the_other_guy

turn_log_first_column = [ "auctioned_card", "agent1_card", "agent2_card", "agent3_card" ]
turn_log_second_column = [ "winning_agent", "agent1_score", "agent2_score", "agent3_score" ]
final_results = [ "agent1_final_score", "agent2_final_score", "agent3_final_score", "winning_agent"]

def pretty_print_results(results):
    print("\n")
    for i in range(13):
        turn_log = results["log"][i]

        print(f"Turn #{i+1}")
        
        for i in range(len(turn_log_first_column)):
            key1 = turn_log_first_column[i]
            key2 = turn_log_second_column[i]

            print(f"\t{key1}: {turn_log[key1]}   \t{key2}: {turn_log[key2]}")

    print("\n")
    for key in final_results:
        print(f"{key}: {results[key]}")

    print("\n")


def main():
    the_other_guy.run() # this just initializes the main simulation module
    test_runner.run() # comment this out if you don't want to run the system tests

    # here we specify three agent module names to test those strategies in the simulation
    results = the_other_guy.run_simulation("random_agent", "random_agent", "random_agent") 
    pretty_print_results(results)


main()
