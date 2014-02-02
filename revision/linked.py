class Node:
	def __init__(self,value):
		self.key=value
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
	def add(self,x):
		node=Node(x)
		if self.head==None:
			self.head=node
		if self.tail!=None:
			self.tail.next=node
		self.tail=node
	def removeDup1(self):
		current=self.head
		d=dict()
		while current!=None:
			if d.__contains__(current.key):
				prev.next=current.next
			else:
				d.__setitem__(current.key,True)
				prev=current
			current=current.next
	def removeDup2(self):
		current=self.head
		if current==None:
			return None
		while current!=None:
			#prev=current
			runner=current
			while runner.next!=None:
				if current.key==runner.next.key:
					runner.next=runner.next.next
				else:
					runner=runner.next
				#runner=runner.next
			current=current.next
	def removeDup(self):
		current=self.head
		if current==None:
			return None
		
		while current!=None:
			runner=current.next
			prev=current
			while runner!=None:
				if current.key==runner.key:
					prev.next=runner.next

				else:
					prev=runner
				runner=runner.next	
			current=current.next
	def display(self):
		current=self.head
		while current!=None:
			print current.key
			current=current.next
	def kthlast(self,k):
		ptr1=self.head
		ptr2=self.head
		for i in range(0,k):
			ptr2=ptr2.next
		if ptr2==None:
			return None
		while ptr2!=None:
			ptr1=ptr1.next
			ptr2=ptr2.next
		return ptr1.key
	def kthlast2(self,x,i,k):
		if x==None:
			return None
		nod=self.kthlast2(x.next,i,k)
		i+=1
		if i==k:
			return x.key
		return nod
l=LinkedList()
arr=[1,2,3,4,5,56,6,9]
for i in arr:
	l.add(i)
#l.display()
print "----------"
#l.removeDup()
#l.display()
print l.kthlast2(l.head,0,3)