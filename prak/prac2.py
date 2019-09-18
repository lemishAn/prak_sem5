
# class Node: 
# 	def __init__(self, value = None, next = None):
# 		self.value = value
# 		self.next = next

# class MyList(object):
# 	def __init__(self):
# 		self.length = 0
# 		self.first = None
# 		self.last = None

# 	def __str__(self):
# 		if self.first != None:
# 			current = self.first
# 			out = 'LinkedList [' + str(current.value) 
# 			while current.next != None:
# 				current = current.next
# 				out += ',' + str(current.value)
# 			return out + ']'
# 		return 'LinkedList []'

# 	def clear(self):
# 		self.__init__()
		
# 	def add(self, x):
# 		self.length += 1
# 		if self.first == None:
# 			self.last = self.first = Node(x, None)
# 		else:
# 			self.last.next = self.last = Node(x, None)

# 	def find (self, key):
# 		current = None
# 		if self.first != None:
# 			current = self.first
# 			while key != current.value or current.next != None:
# 				current = current.next
# 			if key != current.value: 
# 				current = None
# 		return current

# 	def deletekey(self, key):
# 		self.length -=1
# 		if self.first != None:
# 			current = self.first
# 			while key != current.value or current.next != None:
# 				previous = current
# 				current = current.next
# 			if key == current.value:
# 				previous.next = current.next
# 			return

# 	def deletelast(self):
# 		self.length -= 1
# 		if self.first != None:
# 			self.last = None
# 		return

# def Transformation(num):
# 	lst = MyList()
# 	if num == 0:
# 		lst.add(0)
# 		return lst
# 	while num != 0:
# 		key = num % 10
# 		num //= 10
# 		lst.add(key)
# 	return lst

from prac1 import *

def Sum(lst1, lst2):
	lenmax = max(lst1.length, lst2.length)
	lenmin = min(lst1.length, lst2.length)
	lstsum = MyList()
	if lenmin == lst1.length:
		tmp = lst1
		lst1 = lst2
		lst2 = tmp
	lst1 = lst1.first
	lst2 = lst2.first
	key = 0
	while lenmin > 0:
		key = key + lst1.value + lst2.value
		lstsum.add(key % 10)
		key //= 10
		lst1 = lst1.next
		lst2 = lst2.next
		lenmin -= 1
		lenmax -= 1
	while lenmax > 0:
		if key == 1:
			lstsum.add(key + lst1.value)
			lst1 = lst1.next
			lenmax -= 1
			key = 0
			continue
		lstsum.add(lst1.value)
		lst1 = lst1.next
		lenmax -= 1
	if key == 1:
		lstsum.add(1)
	return lstsum

if __name__ == '__main__':
	number1 = input()
	lst1 = Transformation(number1)
	number2 = int(input())
	lst2 = Transformation(number2)
	lstsum = Sum(lst1, lst2)
	print(lstsum.__str__())
