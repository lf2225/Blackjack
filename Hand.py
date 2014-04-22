from Deck import *


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
		print 'I am entering the init routine of Hand'
		self.TotalHandValue = 0
		self.PlayerHand = []
		print 'I am exiting the init routine of Hand'


#initial dealing of the hand, calls the AddCard method twice
	def DealHand(self, Deck1):
		Card1 = Deck1.DealOneCard()
		Card2 = Deck1.DealOneCard()
		print "Deal Hand", Card1, Card2
		self.PlayerHand = [Card1, Card2]



#conveniently display the status of a hand
#initialize the dictionary  (J, Spades...) = (11,1...)
	def DisplayHandValue(self):
		HandValue = 0


		for card in self.PlayerHand:
			if card == 'A':
				#concept of high ace test, when it is true, every other ace in the hand will be counted as 1.
				#set it to true if there is at least one ace in hand
				#maybe put another test in there which will control if the high ace will make you bust, then dont set highace to true
				HighAce = True
					#then if you get a bust and the test of high ace is true, then set high ace to false, then recalculate the value of the hand
					#without hard coding the ace in every time
					#encode in the test if the handvalue +10(difference between 1 and 11) is less than 21, then set high ace to true
				ValueCard1 = ValueDict[Card1[0]][1]
			elif self.TotalHandValue <= 16 and Card2[0] == 'A':
				ValueCard2 = ValueDict[Card2[0]][1]
			elif self.TotalHandValue > 16 and Card1[0] == 'A':
				ValueCard1 = ValueDict[Card1[0]][0]
			elif self.TotalHandValue > 16 and Card2[0] == 'A':
				ValueCard2 = ValueDict[Card2[0]][0]

				HandValue = HandValue + ValueNewCard
				if card = 'A' and HandValue < 10:
					ValueNewCard = ValueDict[card[1]]



		Card1 = self.PlayerHand[0]
		Card2 = self.PlayerHand[1]

		ValueCard1 = ValueDict[Card1[0]]
		ValueCard2 = ValueDict[Card2[0]]

		'''if self.TotalHandValue <= 16 and Card1[0] == 'A':
			ValueCard1 = ValueDict[Card1[0]][1]
		elif self.TotalHandValue <= 16 and Card2[0] == 'A':
			ValueCard2 = ValueDict[Card2[0]][1]
		elif self.TotalHandValue > 16 and Card1[0] == 'A':
			ValueCard1 = ValueDict[Card1[0]][0]
		elif self.TotalHandValue > 16 and Card2[0] == 'A':
			ValueCard2 = ValueDict[Card2[0]][0]'''

		self.TotalHandValue = ValueCard1 + ValueCard2


#keep pullng random card until you have one that hasnt been dealt using an if not equal to dealt card
#inside a for statement running through the dictionary of cards


#add a card to a current, ie HIT, also call it twice in the original hand dealing
	def AddCard(self, Deck1):
		while self.TotalHandValue <= 16:
			HitCard = Deck1.DealOneCard()
			ValueHitCard = ValueDict[HitCard[0]]
			print ValueHitCard
			self.PlayerHand.append(HitCard)
			if HitCard[0] == 'A':

				ValueHitCard = ValueHitCard[1]

			self.TotalHandValue = self.TotalHandValue + ValueHitCard


			if self.TotalHandValue > 21:
				if HitCard[0] == 'A':
				print "BUST"
			elif self.TotalHandValue == 21:
				print "Perfect"
		#HitCard = Deck1.DealOneCard()
