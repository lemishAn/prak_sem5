
class Node: 
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

class MyList(object):
	def __init__(self):
		self.length = 0
		self.first = None
		self.last = None

	def __str__(self):
		if self.first != None:
			current = self.first
			out = 'LinkedList [' + str(current.value) 
			while current.next != None:
				current = current.next
				out += ',' + str(current.value)
			return out + ']'
		return 'LinkedList []'

	def clear(self):
		self.__init__()
		
	def add(self, x):
		self.length += 1
		if self.first == None:
			self.last = self.first = Node(x, None)
		else:
			self.last.next = self.last = Node(x, None)

	def find (self, key):
		current = None
		if self.first != None:
			current = self.first
			while key != current.value or current.next != None:
				current = current.next
			if key != current.value: 
				current = None
		return current

	def deletekey(self, key):
		self.length -=1
		if self.first != None:
			current = self.first
			while key != current.value or current.next != None:
				previous = current
				current = current.next
			if key == current.value:
				previous.next = current.next
			return

	def deletelast(self):
		self.length -= 1
		if self.first != None:
			self.last = None
		return

def Transformation(num):
	lst = MyList()
	while num != 0:
		key = num % 10
		num //= 10
		lst.add(key)
	return lst

# if __name__ == '__main__':
# 	number = input()
# 	lst = Transformation(number)
# 	print(lst.__str__())
