"""
More nuanced, but tried to bid two higher than the auctioned card when possible.
Bids based on closest distance to two higher, if there is a distance tie, 
opts for the higher bid
"""

class Agent:

    def __init__(self):

        self._remaining_cards = list(range(1, 14)) # keep track of the cards left in our hand



    def play_card(self, auctioned_card):

        # list rank the cards by their distance from autioned_card + 2

        ranking = [abs(auctioned_card + 2 - card) for card in self._remaining_cards]

        

        # Looking for the number closest to two greater than the auction card
        min_num = min(ranking)
        
        # Erring on the largest in case of ties
        max_index = -1 
        for i in range(len(self._remaining_cards) -1, -1, -1):
            if ranking[i] == min_num:
                max_index = i
                break
            

        return self._remaining_cards.pop(max_index)

    

    def round_ended(self, auctioned_card, card_you_played, left_agent_card, right_agent_card, winning_agent):

        # left_agent_card is the card the agent to your left played

        # right_agent_card is the card the agenet to your right played

        # winning_agent is 1 if we won the round, 2 if left_agent won, 3 if right_agent won, or None if no one won



        return
    

