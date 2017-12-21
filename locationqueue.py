class LocationQueue(object):
	def __init__(self):
		self.items = []
	
	def is_empty(self):
		return (self.items == [])
		
	def peek(self):
		if not self.is_empty():
			return self.items[self.size() - 1]
	
	def item_enqueued(self, item):
		return (item in self.items)
		
	def enqueue(self, item):
		if not self.item_enqueued(item) and item.not_default():
			self.items.insert(0, item)
	
	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()
			
	def size(self):
		return len(self.items)
	
	def display(self):
		print('***')
		
		for item in self.items:
			print(item)
		print('***')
