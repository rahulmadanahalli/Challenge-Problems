"""
Rahul Madanahalli
Borya and Hanabi
08/14/14
solves the problem by going through all clue combinations
and chooses the clue combination that solves the hand using
the fewest clues.
"""
from ladder import Ladder, duplicate
import time

class BoryaSolved(object):
	def __init__(self):
		self.num_cards = raw_input()
		cards = raw_input()
		#start = time.clock()
		self.actual_hand = cards.split(' ')
		self.ladder = Ladder(self.actual_hand)
		self.construct_clues()
		#timeit = time.clock() - start
		#print timeit
		#print self.clues
		self.num_clues_needed = list()
		self.solve_ladder()
		self.pick_lowest()
		#timit = time.clock() - start
		#print timeit

	def construct_clues(self):
		"""
		constructs the total number of possible clue
		combinations that could yield us with revealing
		Borya's hand. We use the list of edges in the ladder
		to do this.
		"""
		self.clues = list()
		edges = self.ladder.edges
		#print self.ladder.edges
		for edge in edges:
			ind = edges.index(edge)
			edges.remove(edge)
			self.construct_clues_recursively([edge.value], edges)
			edges.insert(ind, edge)

	def construct_clues_recursively(self, clue_seq, edges):
		"""
		constructs combinations of clues.
		helper method for construct_clues
		"""
		if sorted(clue_seq) not in self.clues:
			self.clues.append(sorted(clue_seq))
		if len(edges) >= 1:
			for edge in edges:
				ind = edges.index(edge)
				edges.remove(edge)
				clues = [clue for clue in clue_seq]
				clues.append(edge.value)
				self.construct_clues_recursively(clues, edges)
				edges.insert(ind, edge)

	def solve_ladder(self):
		"""
		Goes through every possible combination of clues
		and checks if the Ladder (constructed by Borya's hand)
		can be solved given those clues. if it can, then we append
		the number of clues in that clue combination to the 
		num_clues_needed list.
		"""
		self.ladder.check_all_but_one()
		if not self.ladder.complete:
			for clue_seq in self.clues:
				if self.num_clues_needed:
					if len(clue_seq)<min(self.num_clues_needed):
						self.ladder = Ladder(self.actual_hand)
						for clue in clue_seq:
							self.ladder.give_clue(clue)
						if self.ladder.complete:
							#print clue_seq
							self.num_clues_needed.append(len(clue_seq))
				else:
					self.ladder = Ladder(self.actual_hand)
					for clue in clue_seq:
						self.ladder.give_clue(clue)
					if self.ladder.complete:
						self.num_clues_needed.append(len(clue_seq))
				self.ladder.clean_up()

	def pick_lowest(self):
		"""
		out of all the possible clue combinations that can
		reveal Borya's hand, the minimum number of num_clues_needed
		is printed.
		"""
		#print self.num_clues_needed
		if self.num_clues_needed:
			print min(self.num_clues_needed)
		else:
			print 0



if __name__ == "__main__":
	solve = BoryaSolved()