from Deck import *
from Hand import *

Deck1 = Deck()

Hand1 = Hand()







Hand1.deal_hand(Deck1)

print 'a sample players hand', Hand1.player_hand

Hand1.display_hand_value()

print 'the value of this hand is', Hand1.total_hand_value

#prints total hand value of two dealt cards
Hand1.add_card(Deck1)



print 'the new hand value is', Hand1.total_hand_value







#for i in range(1,53):
#	Deck1.DealOneCard()

print 'print the rest of the deck', Deck1.shuffle_deck
