"""
A Ladder has Rungs and Edges that
represent Borya's entire Hand.

A ladder is complete (we know which card
is which) when all of its
Rungs are certain.
"""

from rung import Rung
from edge import Edge

class Ladder(object):
	def __init__(self, cards):
		self.rungs = list()
		self.edges = list()
		self.create_ladder(cards)
		self.complete = False

	def create_ladder(self, cards):
		"""
		constructs the Ladder using the
		information from the list of cards passed in

		:param: list of cards (ie. ['W1', 'W2']
		"""
		edges = dict()
		for card in cards:
			if card[0] not in edges.keys():
				edges[card[0]] = Edge(card[0])
			if card[1] not in edges.keys():
				edges[card[1]] = Edge(card[1])
			rung = Rung(edges[card[0]], edges[card[1]])
			if rung not in self.rungs:
				edges[card[0]].rungs.append(rung)
				edges[card[1]].rungs.append(rung)
				self.rungs.append(rung)
		self.edges = [edge for edge in edges.values()]

	def give_clue(self, clue):
		"""
		given the clue, the ladder will expose that edge.

		:param: the value of the edge that we will
		"""
		for edge in self.edges:
			if edge.value == clue:
				edge.expose()
		self.check_all_but_one()

	def check_all_but_one(self):
		"""
		if all rungs are certain except for one,
		we can know the certainty of that rung
		by process of elimination, so we set
		that rung equal to True.
		"""
		uncertain = [rung for rung in self.rungs if not rung.certain]
		if len(uncertain) == 1:
			uncertain[0].certain = True
			self.complete = True
		elif len(uncertain) == 0:
			self.complete = True

	def check_all_certain(self):
		"""
		if all rungs are certain, then the ladder
		is complete
		"""
		for rung in self.rungs:
			if not rung.certain:
				return
		self.complete = True

	def clean_up(self):
		"""
		clears the ladder. making all rungs
		uncertain and all edges unexposed.
		"""
		for rung in self.rungs:
			rung.certain = False
		for edge in self.edges:
			edge.is_exposed = False

def duplicate(cards, ladder):
	"""
	creates copy of current Ladder instance
	and returns that copy

	:returns: new instance of Ladder
	"""
	lad = Ladder(cards)
	for clue in ladder.clues:
		lad.give_clue(clue)
	return lad