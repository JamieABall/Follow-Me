class Location:
	def __init__(self, x=0, y=0):
		self.xc = x if x is not None else 0
		self.yc = y if y is not None else 0
	
	def __eq__(self, other):
		return self.xc == other.xc and self.yc == other.yc
	
	def __ne__(self, other):
		return self.xc != other.xc or self.yc != other.yc
	
	def __str__(self):
		return '(' + str(self.xc) + ', ' + str(self.yc) + ')'
		
	def x_lt(self, other):
		return self.xc < other.xc
	
	def x_ge(self, other):
		return not self.x_lt(other)
	
	def x_gr(self, other):
		return self.xc > other.xc
	
	def x_le(self, other):
		return not self.x_gr(other)
	
	def y_lt(self, other):
		return self.yc < other.yc
	
	def y_ge(self, other):
		return not self.y_lt(other)
	
	def y_gr(self, other):
		return self.yc > other.yc
		
	def y_le(self, other):
		return not self.y_gr(other)
		
	def setx(self, x):
		self.xc = x
	
	def sety(self, y):
		self.yc = y
	
	def make_copy(self):
		return Location(self.xc, self.yc)
	
	def not_default(self):
		temp = Location(0, 0)
		
		return self != temp
