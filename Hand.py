from Deck import *
Deck1 = Deck()


InitialDeck = Deck()

ValueDict = {'2':2,
			 '3':3,
			 '4':4,
			 '5':5,
			 '6':6,
			 '7':7,
			 '8':8,
			 '9':9,
			 'T':10,
			 'J':10,
			 'Q':10,
			 'K':10,
			 'A':(1,11)}

class Hand(object):
	def __init__(self):
		self.TotalHandValue = 0
		self.PlayerHand = []
		


#initial dealing of the hand, calls the AddCard method twice
	def DealHand(self):
		Card1 = Deck1.DealOneCard()
		Card2 = Deck1.DealOneCard()
		print "Deal Hand", Card1, Card2
		self.PlayerHand = [Card1, Card2]
		


#conveniently display the status of a hand
#initialize the dictionary  (J, Spades...) = (11,1...)
	def DisplayHandValue(self):
		ValueCard1 = ValueDict[Card1(0)]
		ValueCard2 = ValueDict[Card2(0)]
		self.TotalHandValue = ValueCard1 + ValueCard2
		

#keep pullng random card until you have one that hasnt been dealt using an if not equal to dealt card 
#inside a for statement running through the dictionary of cards


#add a card to a current, ie HIT, also call it twice in the original hand dealing
	def AddCard(self):
		HitCard = Deck1.DealOneCard()
		







