"""
This agent is to test that the GameSimulation throws an Exception
if an agent plays the same card twice.
"""

class Agent:
    def __init__(self):
        self._remaining_cards = list(range(1, 14)) # keep track of the cards left in our hand

    def play_card(self, auctioned_card):
        # sneakily play the same card twice, which is illegal (for testing purposes)
        if auctioned_card == 3 or auctioned_card == 13:
            return 3

        return self._remaining_cards.pop()
    
    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):
        # left_agent_card is the card the agent to your left played
        # right_agent_card is the card the agent to your right played
        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won

        return

