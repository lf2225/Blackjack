from Deck import *
from Hand import *

Deck1 = Deck()

Hand1 = Hand()
Hand2 = Hand()
# DealerHand = Hand






#Player1

Hand1.deal_hand(Deck1)

print 'a sample player (1) hand', Hand1.PlayerHand

Hand1.display_hand_value()

print 'the value of (1) hand is', Hand1.TotalHandValue

#prints total hand value of two dealt cards
Hand1.add_card(Deck1)



print 'the new (1) hand value is', Hand1.TotalHandValue



#for i in range(1,53):
#	Deck1.DealOneCard()

print 'print the rest of the deck', Deck1.ShuffledDeck

#Player2

Hand2.deal_hand(Deck1)

print 'a sample players (2) hand', Hand2.PlayerHand

Hand2.display_hand_value()

print 'the value of (2) hand is', Hand2.TotalHandValue

#prints total hand value of two dealt cards
Hand2.add_card(Deck1)



print 'the new (2) hand value is', Hand2.TotalHandValue



#for i in range(1,53):
#	Deck1.DealOneCard()

print 'print the rest of the deck', Deck1.ShuffledDeck
