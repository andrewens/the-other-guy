"""
This is the main interface for all game simulation code.
"""


import os
import math
import random
import importlib


AGENTS_DIRECTORY_NAME = "agents"
AGENT_MODULES = {} # string agent_name --> <Module>


# private
def calculate_winning_agent(agent1_card, agent2_card, agent3_card):
    # if two players play the same card, the other player wins
    if agent2_card == agent3_card and agent3_card != agent1_card:
        return 1
    if agent3_card == agent1_card and agent1_card != agent2_card:
        return 2
    if agent1_card == agent2_card and agent2_card != agent3_card:
        return 3
    
    # otherwise, the player with the max card wins
    if agent1_card > max(agent2_card, agent3_card):
        return 1
    if agent2_card > max(agent3_card, agent1_card):
        return 2
    if agent3_card > max(agent1_card, agent2_card):
        return 3
    
    # if all players play the same card, no one wins
    return None


def decrement_winning_agent_index(winning_agent):
    winning_agent -= 1
    if winning_agent <= 0:
        winning_agent = 3

    return winning_agent


def get_winning_agent_name(score1, score2, score3, name1, name2, name3):
    if score1 > max(score2, score3):
        return name1
    if score2 > max(score3, score1):
        return name2
    if score3 > max(score1, score2):
        return name3

    if score1 == score2 == score3:
        return name1 + ", " + name2 + ", " + name3

    if score1 == score2:
        return name1 + ", " + name2
    if score2 == score3:
        return name2 + ", " + name3
    if score3 == score1:
        return name3 + ", " + name1


def new_agent(agent_name, num_cards_per_suite):
    return AGENT_MODULES[agent_name].Agent(num_cards_per_suite)


def all_list_values_less_than_value(list, value):
    for v in list:
        if v >= value:
            return False
    
    return True


def verify_agents_are_honest(agent1_card, agent2_card, agent3_card, agent1_cards_left, agent2_cards_left, agent3_cards_left, c):
    if agent1_card not in agent1_cards_left:
        reason = " twice!" if 1 <= agent1_card <= c else f", which is not in a suite of c={c} cards"
        raise Exception(f"Agent1 played a {agent1_card}{reason}")
    if agent2_card not in agent2_cards_left:
        reason = " twice!" if 1 <= agent2_card <= c else f", which is not in a suite of c={c} cards"
        raise Exception(f"Agent2 played a {agent2_card}{reason}")
    if agent3_card not in agent3_cards_left:
        reason = " twice!" if 1 <= agent3_card <= c else f", which is not in a suite of c={c} cards"
        raise Exception(f"Agent3 played a {agent3_card}{reason}")
    
    agent1_cards_left.remove(agent1_card)
    agent2_cards_left.remove(agent2_card)
    agent3_cards_left.remove(agent3_card)


def run_simulation_with_log(agent1_name, agent2_name, agent3_name, c):
    agent1 = new_agent(agent1_name, c)
    agent2 = new_agent(agent2_name, c)
    agent3 = new_agent(agent3_name, c)
    
    cards_range = range(1, c + 1)
    cards_left = list(cards_range)
    log = []
    
    agent1_cards_left = set(cards_range)
    agent2_cards_left = set(cards_range)
    agent3_cards_left = set(cards_range)
    
    agent1_score = 0
    agent2_score = 0
    agent3_score = 0

    while len(cards_left) > 0:
        random_index = random.randint(0, len(cards_left) - 1)
        auctioned_card = cards_left.pop(random_index)

        agent1_card = agent1.play_card(auctioned_card)
        agent2_card = agent2.play_card(auctioned_card)
        agent3_card = agent3.play_card(auctioned_card)
        
        # make sure agents are being honest
        verify_agents_are_honest(agent1_card, agent2_card, agent3_card, agent1_cards_left, agent2_cards_left, agent3_cards_left, c)
        
        # who won?
        winning_agent = calculate_winning_agent(agent1_card, agent2_card, agent3_card)
        if winning_agent == 1:
            agent1_score += auctioned_card
        elif winning_agent == 2:
            agent2_score += auctioned_card
        elif winning_agent == 3:
            agent3_score += auctioned_card
            
        # tell agents who won
        winning_agent_relative_to_agent1 = winning_agent
        winning_agent_relative_to_agent2 = winning_agent
        winning_agent_relative_to_agent3 = winning_agent

        if not winning_agent is None: # there's a more elegant way to do this but I am tired as of writing this
            winning_agent_relative_to_agent2 = decrement_winning_agent_index(winning_agent_relative_to_agent2)
            winning_agent_relative_to_agent3 = decrement_winning_agent_index(winning_agent_relative_to_agent3)
            winning_agent_relative_to_agent3 = decrement_winning_agent_index(winning_agent_relative_to_agent3)
            
        agent1.round_ended(auctioned_card, agent1_card, agent2_card, agent3_card, winning_agent_relative_to_agent1)
        agent2.round_ended(auctioned_card, agent2_card, agent3_card, agent1_card, winning_agent_relative_to_agent2)
        agent3.round_ended(auctioned_card, agent3_card, agent1_card, agent2_card, winning_agent_relative_to_agent3)
        
        # results
        turn_log = {
            "auctioned_card": auctioned_card,
            "winning_agent": winning_agent,
            "agent1_card": agent1_card,
            "agent2_card": agent2_card,
            "agent3_card": agent3_card,
            "agent1_score": agent1_score,
            "agent2_score": agent2_score,
            "agent3_score": agent3_score,
        }
        log.append(turn_log)

    # calculate winning agent
    winning_agent = get_winning_agent_name(agent1_score, agent2_score, agent3_score, agent1_name, agent2_name, agent3_name)       

    return {
        "log": log,
        "agent1_final_score": agent1_score,
        "agent2_final_score": agent2_score,
        "agent3_final_score": agent3_score,
        "winning_agent": winning_agent
    }


def run_simulation_without_log(agent1_name, agent2_name, agent3_name, c):
    agent1 = new_agent(agent1_name, c)
    agent2 = new_agent(agent2_name, c)
    agent3 = new_agent(agent3_name, c)
    
    cards_range = range(1, c + 1)
    cards_left = list(cards_range)
    
    agent1_cards_left = set(cards_range)
    agent2_cards_left = set(cards_range)
    agent3_cards_left = set(cards_range)
    
    agent1_score = 0
    agent2_score = 0
    agent3_score = 0

    while len(cards_left) > 0:
        random_index = random.randint(0, len(cards_left) - 1)
        auctioned_card = cards_left.pop(random_index)

        agent1_card = agent1.play_card(auctioned_card)
        agent2_card = agent2.play_card(auctioned_card)
        agent3_card = agent3.play_card(auctioned_card)
        
        # make sure agents are being honest
        verify_agents_are_honest(agent1_card, agent2_card, agent3_card, agent1_cards_left, agent2_cards_left, agent3_cards_left, c)
        
        # who won?
        winning_agent = calculate_winning_agent(agent1_card, agent2_card, agent3_card)
        if winning_agent == 1:
            agent1_score += auctioned_card
        elif winning_agent == 2:
            agent2_score += auctioned_card
        elif winning_agent == 3:
            agent3_score += auctioned_card
            
        # tell agents who won
        winning_agent_relative_to_agent1 = winning_agent
        winning_agent_relative_to_agent2 = winning_agent
        winning_agent_relative_to_agent3 = winning_agent

        if not winning_agent is None: # there's a more elegant way to do this but I am tired as of writing this
            winning_agent_relative_to_agent2 = decrement_winning_agent_index(winning_agent_relative_to_agent2)
            winning_agent_relative_to_agent3 = decrement_winning_agent_index(winning_agent_relative_to_agent3)
            winning_agent_relative_to_agent3 = decrement_winning_agent_index(winning_agent_relative_to_agent3)
            
        agent1.round_ended(auctioned_card, agent1_card, agent2_card, agent3_card, winning_agent_relative_to_agent1)
        agent2.round_ended(auctioned_card, agent2_card, agent3_card, agent1_card, winning_agent_relative_to_agent2)
        agent3.round_ended(auctioned_card, agent3_card, agent1_card, agent2_card, winning_agent_relative_to_agent3)
        
    # calculate winning agent
    if agent1_score > max(agent2_score, agent3_score):
        return 1, 0, 0
    if agent2_score > max(agent3_score, agent1_score):
        return 0, 1, 0
    if agent3_score > max(agent1_score, agent2_score):
        return 0, 0, 1

    if agent1_score == agent2_score == agent3_score:
        return 0, 0, 0 # you could return 1/3, but it makes the output messy and this is functionally the same outcome
    
    if agent1_score == agent2_score:
        return 0.5, 0.5, 0
    if agent2_score == agent3_score:
        return 0, 0.5, 0.5
    if agent3_score == agent1_score:
        return 0.5, 0, 0.5


def run_all_possible_combinations_of_agents(agents, n, c):
    if not isinstance(n, int):
        raise Exception(str(n) + " is not an integer!")
    if not isinstance(agents, list):
        raise Exception(str(agents) + " is not a list!")
    
    unique_agents = []
    for agent_name in agents:
        if agent_name in unique_agents: # don't count duplicate agents twice
            continue
        
        if agent_name in AGENT_MODULES:
            unique_agents.append(agent_name)
            continue
        
        raise Exception(str(agent_name) + " is not the name of an agent module!")
    
    agents = unique_agents
    num_agents = len(agents)
    num_permutations = num_agents ** num_agents
    tests_per_permutation = math.floor(n / num_permutations)
    
    if n < num_permutations:
        raise Exception(f"There are {num_permutations} permutations for {num_agents} agents, but n={n} is less than the number of permutations.")
    
    results = []

    for i in range(num_agents): # TODO this method of generating permutations creates duplicates we don't want because order doesn't matter
        for j in range(num_agents):
            for k in range(num_agents):
                agent1 = agents[i]
                agent2 = agents[j]
                agent3 = agents[k]

                agent1_score = 0
                agent2_score = 0
                agent3_score = 0

                no_cheating = True
                winning_agent = 0
                
                for _ in range(tests_per_permutation):
                    try:
                        score1, score2, score3 = run_simulation_without_log(agent1, agent2, agent3, c)
                        
                        agent1_score += score1
                        agent2_score += score2
                        agent3_score += score3
                    except:
                        no_cheating = False
                        break

                winning_agent = 0
                if agent1_score > max(agent2_score, agent3_score):
                    winning_agent = 1
                elif agent2_score > max(agent3_score, agent1_score):
                    winning_agent = 2
                elif agent3_score > max(agent1_score, agent2_score):
                    winning_agent = 3
                
                results.append((agent1, agent1_score, agent2, agent2_score, agent3, agent3_score, no_cheating, winning_agent))

    return results


def do_i_win_this_game(auctioned_cards, my_cards, player2_cards, player3_cards, score):
    # each arg is a tuple or list of cards that were played by each player (+ auction pile) per turn
    # and score is the preexisting score of each player (optional)

    num_turns = len(auctioned_cards)
    score = [0, 0, 0] if score is None else list(score) # int (player_index - 1) --> int score (sum of won auctioned cards)

    for i in range(num_turns):
        winning_agent = calculate_winning_agent(my_cards[i], player2_cards[i], player3_cards[i])
        if winning_agent is None:
            continue
        
        score[winning_agent - 1] += auctioned_cards[i]
    
    return score[0] > max(score[1], score[2])


# public
def pick_weighted_item(items):
    if not isinstance(items, dict):
        raise Exception(f"{items} is not a dictionary!")
    
    first_key, first_value = next(iter(items.items()))
    if first_key is None:
        return None
    
    if not (isinstance(first_value, int) or isinstance(first_value, float)):
        raise Exception(f"Items' values must be numbers, not whatever this is: {first_value}")
    
    sum = 0
    items_ordered = [] # [ (item, number weight + prev_weights) ] 

    for item_to_pick, item_probability in items.items():
        items_ordered.append((item_to_pick, item_probability + sum))
        sum += item_probability
        
    random_float = random.random() * sum
    
    for item in items_ordered:
        if random_float <= item[1]:
            return item[0]
        
    # it should never get down here


def list_permutations(items):
    if not isinstance(items, set):
        raise Exception(f"{items} is not a set!")
    
    num_items = len(items)

    pointers = [] # [ num_items - 1, num_items - 2, ... 1, 0 ]
    for i in range(num_items):
        pointers.append(num_items - i - 1)

    permutations = set() # { (item1, item2, ...,  item_n), (item2, item1, ..., item_n), ..., (item_n, item_n-1, ..., item1) }
    
    while True:
        # copy set of items
        items_clone = list(items)
        
        # build a list of selected items
        perm = []
        for pointer in pointers:
            perm.append(items_clone.pop(pointer))

        # convert list to tuple (vomit) and save it
        permutations.add(tuple(perm))
        
        # are we done? x_x
        if sum(pointers) <= 0:
            break
        
        # increment pointers
        for i in range(num_items - 1, -1, -1):
            pointers[i] -= 1
            if pointers[i] >= 0:
                break
            
            pointers[i] = num_items - i - 1

    return permutations


def calculate_card_win_chances(auctioned_card, auction_pile, your_cards, player2_cards, player3_cards, initial_score):
    if not (isinstance(auctioned_card, int) and auctioned_card > 0):
        raise Exception(f"{auctioned_card} is not a whole number!")
    if not isinstance(auction_pile, set):
        raise Exception(f"{auction_pile} is not a set!")
    if not isinstance(your_cards, set):
        raise Exception(f"{your_cards} is not a set!")
    if not isinstance(player2_cards, set):
        raise Exception(f"{player2_cards} is not a set!")
    if not isinstance(player3_cards, set):
        raise Exception(f"{player3_cards} is not a set!")
    if not (initial_score is None or isinstance(initial_score, list)):
        raise Exception(f"{initial_score} is not a list! (it can also be None)")
    
    auction_perms = list_permutations(auction_pile)
    player1_perms = list_permutations(your_cards)
    player2_perms = list_permutations(player2_cards)
    player3_perms = list_permutations(player3_cards)
    
    games_played_per_card_in_hand = dict() # int card_in_my_hand --> int games_played (doing this because i don't trust myself to do it with a formula)
    win_chances = dict() # int card_in_my_hand --> float percent_possible_games_it_wins

    for card in your_cards:
        win_chances[card] = 0
        games_played_per_card_in_hand[card] = 0
    
    for P in auction_perms:
        for X in player1_perms:
            for Y in player2_perms:
                for Z in player3_perms:
                    card_i_played = X[0]
                    games_played_per_card_in_hand[card_i_played] += 1
                    i_won = do_i_win_this_game((auctioned_card,) + P, X, Y, Z, initial_score)
                    
                    if i_won:
                        win_chances[card_i_played] += 1

    for card in your_cards:
        win_chances[card] = win_chances[card] / games_played_per_card_in_hand[card]

    return win_chances


def run_simulation(agent1="random_agent", agent2="random_agent", agent3="random_agent", n=1, c=13, generate_log=True, agents=None):
    # c is the number of cards in a suite / hand. default is 13 because ... 10, jack, queen, king --> 10, 11, 12, 13 cards in a suite (normally)
    if not isinstance(c, int):
        raise Exception(f"c={c} is not an integer!")
    if not c >= 1:
        raise Exception(f"c={c} is not greater than or equal to 1!")
    
    # n is the number of games you want to run
    if not isinstance(n, int):
        raise Exception(f"n={n} is not an integer!")
    if not n >= 1:
        raise Exception(f"n={n} is not greater than or equal to 1!")

    # run through every permutation of a set of agents
    if not agents is None:
        return run_all_possible_combinations_of_agents(agents, n, c)
    
    # run some number of games with three specific agents
    if agent1 not in AGENT_MODULES:
        raise Exception(str(agent1) + " is not the name of an agent module!")
    if agent2 not in AGENT_MODULES:
        raise Exception(str(agent2) + " is not the name of an agent module!")
    if agent3 not in AGENT_MODULES:
        raise Exception(str(agent3) + " is not the name of an agent module!")

    # run one game and keep a log of what happened each turn
    if n == 1 and generate_log:
        return run_simulation_with_log(agent1, agent2, agent3, c)

    # run 1 or more games, only keeping track of score
    agent1_wins = 0
    agent2_wins = 0
    agent3_wins = 0

    for i in range(n):
        w1, w2, w3 = run_simulation_without_log(agent1, agent2, agent3, c)
        agent1_wins += w1
        agent2_wins += w2
        agent3_wins += w3

    winning_agent = get_winning_agent_name(agent1_wins, agent2_wins, agent3_wins, agent1, agent2, agent3)

    return {
        "agent1_wins": agent1_wins,
        "agent2_wins": agent2_wins,
        "agent3_wins": agent3_wins,
        "winning_agent": winning_agent,
    }


def get_all_agent_module_names():
    return list(AGENT_MODULES.keys())

        
def run():
    for file_name in os.listdir(AGENTS_DIRECTORY_NAME):
        # get python modules
        if "__" in file_name:
            continue
        
        filename_without_extension, _ = os.path.splitext(file_name)
        module = importlib.import_module(AGENTS_DIRECTORY_NAME + "." + filename_without_extension)
        
        AGENT_MODULES[filename_without_extension] = module

