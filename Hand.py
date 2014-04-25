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
			 'A':11}

class Hand(object):
	def __init__(self):
		print 'I am entering the init routine of Hand'
		self.TotalHandValue = 0
		self.PlayerHand = []
		print 'I am exiting the init routine of Hand'


#initial dealing of the hand, calls the AddCard method twice
	def deal_hand(self, Deck1):
		Card1 = Deck1.deal_one_card()
		Card2 = Deck1.deal_one_card()
		print "Deal Hand for Player", i
		#remove later
		print Card1, Card2
		self.PlayerHand = [Card1, Card2]


#helper method to figure out the value of aces in hand
	def ace_count(self):
		HighAce = False
		if len(PlayerHand) <= 2:
			for card in self.PlayerHand:
				#one ace in the initial hand, always ace high
				if ValueDict[PlayerHand[0][0]] == 11 or ValueDict[PlayerHand[1][0]] == 11:
					HighAce = True
					if ValueDict[PlayerHand[0][0]] == 11 and ValueDict[PlayerHand[1][0]] == 11:
						#set one to 11, set the other to 1, no order required
						ValueDict[Ok]
		else:
			#if total is more than 21, reduce all aces to 1
			for card in self.PlayerHand:
				if self.TotalHandValue > 21:
					for card in self.PlayerHand:
						if ValueDict[card] == 11:
							HighAce = False
							self.TotalHandValue = self.TotalHandValue - 10
							print 'Aces have been reduced from 11 to 1'

							if ((self.TotalHandValue - 10) < 10):
								HighAce = True
								self.TotalhandValue = self.TotalHandValue + 10
								print 'It made sense to up one ace to 11'

#conveniently display the status of a hand
#initialize the dictionary  (J, Spades...) = (11,1...)
	def display_hand_value(self):
		TotalHandValue = 0
		for card in self.PlayerHand:
			ValueCard = ValueDict[self.PlayerHand[0]
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
		self.ace_count()
		self.TotalHandValue = ValueCard1 + ValueCard2

#keep pullng random card until you have one that hasnt been dealt using an if not equal to dealt card
#inside a for statement running through the dictionary of cards


#add a card to a current, ie HIT, also call it twice in the original hand dealing
	def add_card(self, Deck1):
		while self.TotalHandValue <= 16:
			HitCard = Deck1.DealOneCard()
			ValueHitCard = ValueDict[HitCard[0]]
			print ValueHitCard
			self.PlayerHand.append(HitCard)
			if HitCard[0] == 'A':

				ValueHitCard = ValueHitCard[1]
			self.ace_count()
			self.TotalHandValue = self.TotalHandValue + ValueHitCard


			if self.TotalHandValue == 21:
				print "Perfect"
		#HitCard = Deck1.DealOneCard()
