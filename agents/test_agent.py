"""
Prototypical agent for testing purposes.
Feel free to copy-paste this module when making new agents.
"""

class Agent:
    def __init__(self):
        self._remaining_cards = list(range(1, 14)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card):
        return self._remaining_cards.pop() # just play the top card off our hand
    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agenet to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won

        return

