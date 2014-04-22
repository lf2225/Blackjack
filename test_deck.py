from Deck import *
from Hand import *

Deck1 = Deck()

Hand1 = Hand()







Hand1.DealHand(Deck1)

print 'a sample players hand', Hand1.PlayerHand

Hand1.DisplayHandValue()

print 'the value of this hand is', Hand1.TotalHandValue

#prints total hand value of two dealt cards
Hand1.AddCard(Deck1)



print 'the new hand value is', Hand1.TotalHandValue







#for i in range(1,53):
#	Deck1.DealOneCard()

print 'print the rest of the deck', Deck1.ShuffleDeck
