"""
A Rung is a component of the ladder that represents a 
Card in Borya's hand. The rung has 2 Edges. One referring
to the color of the card and the other referring to the number
value of the card.

We are certain of a card's color and number when its
rung becomes certain.

"""


class Rung(object):
	def __init__(self, color_edge, value_edge):
		self.edges = [color_edge, value_edge]
		self.certain =  False

	def update_certainty(self):
		"""
		if both edges of the rung are exposed, then
		the rung's certain value becomes True.
		:returns: updated value of certainty
		"""
		if not self.certain:
			self.certain = self.edges[0].is_exposed and self.edges[1].is_exposed
		return self.certain

	def other_edge(self, edge):
		"""
		:param: one of the edges of the rung
		:returns: the other edge value
		"""
		if edge == self.edges[0]:
			return self.edges[1]
		elif edge == self.edges[1]:
			return self.edges[0]
		return

	def __eq__(self, other):
		return self.edges == other.edges

	def __repr__(self):
		return str([edge.value for edge in self.edges])