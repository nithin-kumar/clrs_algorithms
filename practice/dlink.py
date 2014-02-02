class node:
	def __init__(self,value):
		self.key=value
		self.next=None
		self.previous=None
class Dlink:
	def __init__(self):
		self.head=None
		self.tail=None
	def insert_first(self,x):
		new_node=node(x)
		new_node.next=self.head
		if self.head!=None:
			self.head.previous=new_node
		self.head=new_node
		new_node.previous=None
	def insert_last(self,x):
		new_node=node(x)
		if self.head==None:
			self.head=x
			self.tail=x
		if self.tai
		self.tail.next
	def search(self,k):
		x=self.head
		try:
			while x!=None and x.key!=k:
				x=x.next
			return x
		except AttributeError:
			print "No key found "
	def delete(self,y):
		x=node(y)
		try:
			if x.previous!=None:
				x.previous.next=x.next
			else:
				self.head=x.next
			if x.next!=None:
				x.next.previous=x.previous
		except AttributeError:
			print "Index out of range!!"

	def display(self):
		x=self.head
		while x!=None:
			print x.key
			x=x.next
l=Dlink()
l.insert(2)
l.insert(3)
l.insert(4)
l.display()
print "------------"
print l.head.next.next.previous.key