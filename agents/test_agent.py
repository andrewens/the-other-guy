"""
Prototypical agent for testing purposes.
Feel free to copy-paste this module when making new agents.
"""

class Agent:
    def __init__(self, num_cards_per_suite):
        self._remaining_cards = list(range(1, num_cards_per_suite + 1)) # keep track of the cards left in our hand
        self._opponent1_cards = list(range(1, num_cards_per_suite + 1))
        self._opponent2_cards = list(range(1, num_cards_per_suite + 1))
        self._remaining_auction_cards = list(range(1, num_cards_per_suite + 1))

    def play_card(self, auctioned_card):
        return self._remaining_cards.pop() # just play the top card off our hand
    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agent to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won
        
        self._opponent1_cards.remove(left_agent_card)
        self._opponent2_cards.remove(right_agent_card)
        self._remaining_auction_cards.remove(auctioned_card)

        return

