"""
An agent that knows the value of things
"""

class Agent:

    def __init__(self, num_cards_per_suite):

        self._auction_cards_left = list(range(1, num_cards_per_suite + 1))

        self._remaining_cards = list(range(1, num_cards_per_suite + 1))

        self._left_player_cards = list(range(1, num_cards_per_suite + 1))
        self._right_player_cards = list(range(1, num_cards_per_suite + 1))

    def play_card(self, auctioned_card):

        max_card = 0
        for card in self._remaining_cards:
            max_card = max(max_card, card)
            if max_card > auctioned_card:
                break

        self._remaining_cards.remove(max_card)
        
        return max_card

    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        
        self._auction_cards_left.remove(auctioned_card)

        # left_agent_card is the card the agent to your left played
        self._left_player_cards.remove(left_agent_card)

        # right_agent_card is the card the agent to your right played
        self._right_player_cards.remove(right_agent_card)

        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won


        return
