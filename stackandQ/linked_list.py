class Node:
	def __init__(self,value):
		self.data=value
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
	def add_node(self,data):
		new_node=Node(data)
		if self.head==None:
			self.head=new_node
		if self.tail!=None:
			self.tail.next=new_node
		self.tail=new_node
	def remove_node(self,index):
		prev=None
		i=0
		node=self.head
		while(node!=None and i<index):
			prev=node
			node=node.next
			i+=1
		if prev==None:
			self.head=node.next
		elif node.next==None:
			self.tail=prev
		else:
			prev.next=node.next
	def display_linkedlist(self):
		node=self.head
		while node!=None:
			print node.data
			node=node.next
	def search_node(self,key):
		node=self.head
		while node!=None and node.data !=key:
			node=node.next
		return node
	def remov_key(self,key):
		prev=None
		node=self.head
		while node!=None and node.data!=key:
			prev=node
			node=node.next
		if node==None:
			return "No key Found"
		if prev==None:
			self.head=node.next
		elif node.next==None:
			prev.next=None
			self.tail=prev

		else:
			prev.next=node.next
		return self.display_linkedlist()
	def reverse(self):
		if self.head==None:
			return None
		currentNode=self.head
		nextNode=self.head.next
		self.head.next=None
		self.tail=self.head
		while nextNode!=None:
			loopNode=nextNode.next
			nextNode.next=currentNode
			currentNode=nextNode
			nextNode=loopNode
		self.head=currentNode
	def concatenate(self,L2):
		self.tail.next=L2.head
		self.tail=L2.tail
L1=LinkedList()
L1.add_node(5)
L1.add_node(15)
L1.add_node(25)
#L2=LinkedList()
#L2.add_node(20)
#L2.add_node(30)
#L2.add_node(40)
#L1.concatenate(L2)
L1.display_linkedlist()
#print L1.head.data
#print L1.tail.data
#print L.search_node(252)
#print "-------------"
#print L.remov_key(25)
#print L.tail.data
#print L.head.data
#L.reverse()
#L.display_linkedlist()
#print L.tail.data
#print L.head.data
L1.remove_node(15)
L1.display_linkedlist()
