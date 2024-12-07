import the_other_guy

def run():
    # given the current auctioned card, a set of remaining cards (and the remaining cards of your opponents + the auction pile),
    # calculate the % of possible games that you win for each card in your hand if you play that card
    # TODO this needs to account for any existing score T_T

    auctioned_card = 2
    auction_pile = {1, 3}
    player1 = {1, 2, 3}
    player2 = {1, 2, 3}
    player3 = {1, 2, 3}
    initial_score = [0, 0, 0]
    
    card_win_chances = the_other_guy.calculate_card_win_chances(auctioned_card, auction_pile, player1, player2, player3, initial_score)
    
    assert isinstance(card_win_chances, dict)
    assert isinstance(card_win_chances[1], float)
    assert isinstance(card_win_chances[2], float)
    assert isinstance(card_win_chances[3], float)
