"""
There is an Edge for each unique color
and number value in Borya's hand.

An edge becomes exposed when the clue that corresponds
to that edge's value is given.

An edge has a list of Rungs that connect
it to other edges.
"""

from rung import Rung

class Edge(object):
	

	def __init__(self, value):
		self.rungs = list()
		self.value = value
		self.is_exposed = False

	def expose(self):
		"""
		it will set the exposed value of this
		Edge to True. Then it parses through
		every Rung that is connected to this Edge
		and if both of the Edges for that rung
		are exposed, then that Rung is now certain.
		"""
		self.is_exposed = True
		for rung in self.rungs:
			if rung.update_certainty() and rung.other_edge(self).is_exposed:
				rung.other_edge(self).check_all_but_one()
		self.check_all_but_one()

	def check_all_but_one(self):
		"""
		when every rung from an exposed edge is certain except for one,
		then you make last one certain too by process of elimination. 
		"""
		uncertain = [rung for rung in self.rungs if not rung.certain]
		if len(uncertain) == 1:
			uncertain[0].certain = True

	def __repr__(self):
		return self.value

	def __eq__(self, other):
		return self.value == other.value
