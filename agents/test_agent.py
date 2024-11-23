class Agent:
    def __init__(self):
        self._remaining_cards = list(range(1, 14))

    def play_card(self, auctioned_card):
        return self._remaining_cards.pop()

