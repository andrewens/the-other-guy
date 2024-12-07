"""
Calculate exact odds that each card will win, assign those odds as weights and randomly pick one of the cards.
"""

import the_other_guy

MAX_ALLOWED_CARDS_PER_SUITE = 4

class Agent:
    def __init__(self, num_cards_per_suite):
        if num_cards_per_suite > MAX_ALLOWED_CARDS_PER_SUITE:
            raise Exception(f"analytic_agent can't be used with {num_cards_per_suite} because it will fry your computer (MAX_ALLOWED_CARDS_PER_SUITE={MAX_ALLOWED_CARDS_PER_SUITE})")

        self._remaining_cards = set(range(1, num_cards_per_suite + 1)) # keep track of the cards left in our hand
        self._opponent1_cards = set(range(1, num_cards_per_suite + 1))
        self._opponent2_cards = set(range(1, num_cards_per_suite + 1))
        self._remaining_auction_cards = set(range(1, num_cards_per_suite + 1))
        self._score = [0, 0, 0]


    def play_card(self, auctioned_card):
        self._remaining_auction_cards.remove(auctioned_card)

        card_win_chances = the_other_guy.calculate_card_win_chances(
            auctioned_card, 
            self._remaining_auction_cards, 
            self._remaining_cards, 
            self._opponent1_cards, 
            self._opponent2_cards, 
            self._score
        )
        
        # print("\nAuctioned card", auctioned_card)
        # print(card_win_chances)

        card = the_other_guy.pick_weighted_item(card_win_chances)
        self._remaining_cards.remove(card)
        
        return card


    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agent to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won
        
        self._opponent1_cards.remove(left_agent_card)
        self._opponent2_cards.remove(right_agent_card)
        
        if not winning_agent is None:
            self._score[winning_agent - 1] += auctioned_card

