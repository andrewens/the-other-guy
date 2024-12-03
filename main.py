import test_runner
import the_other_guy


turn_log_first_column = [ "auctioned_card", "agent1_card", "agent2_card", "agent3_card" ]
turn_log_second_column = [ "winning_agent", "agent1_score", "agent2_score", "agent3_score" ]
final_results = [ "agent1_final_score", "agent2_final_score", "agent3_final_score", "winning_agent"]


def pad_string(string, min_chars):
    string = str(string)
    return string + " " * (min_chars - len(string))


def pretty_print_dict(results):
    print()
    for k, v in results.items():
        print(k, v)
    print()


def pretty_print_single_game_results(results):
    print()
    j = 0
    for turn_log in results["log"]:
        j += 1
        print(f"Turn #{j}")
        
        for i in range(len(turn_log_first_column)):
            key1 = turn_log_first_column[i]
            key2 = turn_log_second_column[i]

            print(f"\t{key1}: {turn_log[key1]}   \t{key2}: {turn_log[key2]}")
            

    print()
    for key in final_results:
        print(f"{key}: {results[key]}")

    print()
    
    
def pretty_print_round_robin_results(results):
    print()
    for i in range(len(results)):
        agent1 = results[i][0]
        agent2 = results[i][2]
        agent3 = results[i][4]
        
        score1 = results[i][1]
        score2 = results[i][3]
        score3 = results[i][5]
        
        no_cheating = results[i][6]
        winning_agent = results[i][7]
        winning_agent = results[i][2 * winning_agent - 2] if winning_agent != 0 else "None"
        
        print(
            pad_string(f"#{i}: ", 6),
            pad_string(f"{winning_agent}", 21),
            pad_string(f"{agent1}:", 22),
            pad_string(score1, 5),
            pad_string(f"{agent2}:", 22),
            pad_string(score2, 5),
            pad_string(f"{agent3}:", 22),
            pad_string(score3, 5),
            f"no cheating: {no_cheating}"
        )
    print()


def pretty_print_any_result(results):
    if "log" in results:
        pretty_print_single_game_results(results)
        return
    
    if isinstance(results, list):
        pretty_print_round_robin_results(results)
        return
    
    pretty_print_dict(results)


def main():
    the_other_guy.run() # this just initializes the main simulation module
    test_runner.run() # comment this out if you don't want to run the system tests

    """
    results = the_other_guy.run_simulation(
        agents=["burts_heuristic_agent", "random_agent", "ditto_agent"], 
        n=1000 # this is the total number of games we're willing to run, *NOT* the number of games per permutation
    )
    pretty_print_any_result(results)
    """

    results = the_other_guy.run_simulation(
        agent1 = "burts_heuristic_agent",
        agent2 = "random_agent",
        agent3 = "ditto_agent",
        n = 1000,
        c = 5
    )
    pretty_print_any_result(results)


main()
