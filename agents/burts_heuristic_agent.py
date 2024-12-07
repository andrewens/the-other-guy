"""
Calculate expected value of each card in your hand and play the card with the highest expected value.

The expected value of a card in your hand is defined as:

    (auctioned card's value) 
    * (probability that this card will win against any card in the others' hands) 
    - (value of the card you played)
"""

import math


PRINT_PLS = False


def _print(*args):
    if not PRINT_PLS:
        return
    print(*args)


def trunc(n):
    return math.floor(n * 1E3)


def does_my_card_win(my_card, agent2_card, agent3_card):
    return (agent2_card == agent3_card and agent3_card != my_card) or (my_card > max(agent2_card, agent3_card))


def probability_card_will_win(my_card, opponent1_cards, opponent2_cards):
    wins = 0
    total = len(opponent1_cards) ** 2
    
    for opponent1_card in opponent1_cards:
        for opponent2_card in opponent2_cards:
            if does_my_card_win(my_card, opponent1_card, opponent2_card):
                wins += 1
    
    return wins / total


class Agent:
    def __init__(self, num_cards_per_suite):
        self._remaining_cards = list(range(1, num_cards_per_suite + 1)) # keep track of the cards left in our hand
        self._opponent1_cards = list(range(1, num_cards_per_suite + 1))
        self._opponent2_cards = list(range(1, num_cards_per_suite + 1))
        self._round_number = 1


    def play_card(self, auctioned_card):
        max_expected_value = -math.inf
        chosen_card = None

        _print("\nAUCTIONED CARD", auctioned_card)
        for my_card in self._remaining_cards:
            probability_this_card_wins = probability_card_will_win(my_card, self._opponent1_cards, self._opponent2_cards)
            expected_value =  auctioned_card * probability_this_card_wins - (self._round_number * my_card)
            
            _print("\t", my_card, "expected value", trunc(expected_value), "prob", trunc(probability_this_card_wins))
            
            if expected_value >= max_expected_value:
                max_expected_value = expected_value
                chosen_card = my_card

        self._remaining_cards.remove(chosen_card)
        
        _print("\t --> chosen_card", chosen_card)

        return chosen_card

    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agent to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won
        
        self._opponent1_cards.remove(left_agent_card)
        self._opponent2_cards.remove(right_agent_card)
        self._round_number += 1

