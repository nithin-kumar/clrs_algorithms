class Node:
	def __init__(self,value):
		self.key=value
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
	def add(self,x):
		new_node=Node(x)
		x=self.head
		if x==None:
			self.head=new_node
		if self.tail!=None:
			self.tail.next=new_node
		self.tail=new_node
	def display(self):
		x=self.head
		while(x!=None):
			print x.key
			x=x.next
	def search(self,k):
		x=self.head
		try:
			while x!=None and x.key!=k:
				x=x.next
			return x.key
		except AttributeError:
			"Key not found"
	def remove(self,index):
		prev=None
		i=0
		node=self.head
		while(node!=None and i<index):
			prev=node
			node=node.next
			i+=1
		if prev==None:
			self.head=node.next
		else:
			prev.next=node.next
		if node.next==None:
			self.tail=prev
	def remove_key(self,k):
		prev=None
		node=self.head
		try:
			while node!=None and node.key!=k:
				prev=node
				node=node.next
			if prev==None:
				self.head=node.next
			else:
				prev.next=node.next
			if node.next==None:
				self.tail=prev
		except AttributeError:
			print k ," not found"
	def reverse(self):
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
	def delDuplicate(self):
		dict_={}
		x=self.head
		#dict_[x.key]=True
		while x!=None:
			#prev=x
			#x=x.next
			if x.key in dict_:
				prev.next=x.next
			else:
				dict_[x.key]=True
				prev=x
			x=x.next
	def delDup(self):
		main=self.head
		while main!=None:
			prev=main
			nextNode=main.next
			while nextNode!=None:
				if nextNode.key==main.key:
					prev.next=nextNode.next
				#prev=nextNode
				nextNode=nextNode.next
			main=main.next
	def kthToLast(self,k):
		ptr1=self.head
		ptr2=self.head
		for i in range(1,k):
			ptr2=ptr2.next
		if ptr2==None:# if k>size of the linked list
			return 
		while ptr2.next!=None:
			ptr2=ptr2.next
			ptr1=ptr1.next
		return ptr1.key
	def check(self,nod):
		x=Node(nod)
		print x.key
		print x.next.key
	def partition(self,k):
		x=self.head
		while x!=None and x.key!=k:
			x=x.next
		x.key,self.head.key=self.head.key,x.key
		pivot=self.head.key
		i=self.head.next
		j=self.head.next
		while j!=None:
			if j.key<pivot:
				j.key,i.key=i.key,j.key
				prev=i
				i=i.next
			j=j.next
		prev.key,l.head.key=l.head.key,prev.key

	def partition2(self,x):
		node=self.head
		beforStart=None
		beforeEnd=None
		afterStart=None
		afterEnd=None
		while(node!=None):
			next=node.next
			node.next=None
			if node.key<x:# Put the node in the beforlist
				if beforStart==None:
					beforStart=node
					beforeEnd=beforStart
				else:
					beforeEnd.next=node
					beforeEnd=node
			else:# Put the node into the after list
				if afterStart==None:
					afterStart=node
					afterEnd=afterStart
				else:
					afterEnd.next=node
					afterEnd=node
			node=next
		if beforStart==None:
			return afterStart
		#Merge the two list
		beforeEnd.next=afterStart
		return beforStart
	def add_lists(self,x,y,carry):
		if x==None and y==None and carry==0:
			return None
		value=carry
		result=Node(carry)
		#
		if x!=None:
			value+=x.key
		if y!=None:
			value+=y.key
		result.key=value%10
		self.add(result)
		if x!=None or y!=None:
			more=self.add_lists(None if x==None else x.next,None if y==None else y.next,1 if value>10 else 0)
		
		#result.next=more
		self.add(more)
		#return result
	def isPalindrom(self,size):#Size is known
		running=self.head
		l=[]#stack for carrying the first half of the linked list
		for i in range(0,size/2):
			l.append(running.key)
			running=running.next
		if size%2!=0:
			running=running.next
		while running!=None:
			x=l.pop()
			if x!=running.key:
				return "Not Palindrome!!"
			running=running.next
		return "Palindrome!!!"
	def isPalindrom2(self):
		slow=self.head
		fast=self.head
		l=[]
		while fast!=None and fast.next!=None:
			l.append(slow.key)
			slow=slow.next
			fast=fast.next.next
		if fast!=None:
			slow=slow.next
		while slow!=None:
			x=l.pop()
			if x!=slow.key:
				return False
			slow=slow.next
		return True


#l=LinkedList()
#arr=[1,2,2,21,3,2,2,2,1]
#for i in arr:
#	l.add(i)
#print l.isPalindrom2()
l=LinkedList()
arr=[1,2,2,2,2,2,1,1,1,1,1]
for i in arr:
	l.add(i)
l.display()
print "----------"
l.delDuplicate()
l.display()
#l=LinkedList()
#arr=[12,27,13,2,3,4,5,24]
#for i in arr:
#	l.add(i)
#l.display()
print "--------------"
#l.check(4)
#l.remove_key(101)
#l.reverse()
#l.display()
#print l.search(71)
#l.delDup()
#print l.kthToLast(6)
#r=l.partition2(5)
#while r!=None:
#	print r.key
#	r=r.next
#l1=LinkedList()
#arr1=[1,2,3]
#for i in arr1:
#	l1.add(i)
#l2=LinkedList()
#arr2=[4,5,6]
#for i in arr2:
#	l2.add(i)
#l3=LinkedList()
#l3.add_lists(l1.head,l2.head,0)
#l3.display()



