"""
Prototypical agent for testing purposes.
Feel free to copy-paste this module when making new agents.
"""

class Agent:
    def __init__(self):
        self._remaining_cards = list(range(1, 14)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card):
        return self._remaining_cards.pop() # just play the top card off our hand

