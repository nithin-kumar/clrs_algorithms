class Queue:
	def __init__(self):
		self.a=[0]*10
		self.head=0
		self.tail=0
		self.length=len(self.a)
	
	def queue_full(self):
		if self.tail+1==self.head:
			return True
		return False

	def queue_empty(self):
		if self.head==self.tail:
			return True
		return False

	def enqueue(self,x):
		if self.queue_full():
			return "Que is Full"
		self.a[self.tail]=x
		if (self.tail==self.length-1):
			self.tail=0
		else:
			self.tail+=1

	def dequeue(self):
		if self.queue_empty():
			return "Queue is Empty"
		x=self.a[self.head]
		if self.head==self.length-1:
			self.head=0
		else:
			self.head+=1
		return x
	
	
	def display(self):
		#for i in range(self.head,self.tail+1):
			#return self.a[i]
		return self.a
q1=Queue()
q1.enqueue(4)
q1.enqueue(7)
q1.enqueue(7)
q1.enqueue(7)
q1.enqueue(7)
q1.enqueue(7)
#print q1.dequeue()
#print q1.head
print q1.tail
#print q1.queue_empty()
print q1.display()




		
