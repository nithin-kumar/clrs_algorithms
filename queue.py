#queue

def main():
	Q=[0,0,0,0,0,0,0,0]
	items=0
	tail=0
	def enqueue(x):
		Q[tail]=x
		items=items+1
		if(tail==size):
			tail=0
		else:
			tail=tail+1	
	return Q
	print enqueue(1)
	def dequeue():
		if(queueEmpty()):
			print "Underflow"
		else:
			x=Q[head]
			items=items-1
			if(head==size):
				head=0
			else:
				head=head+1
		return x
	def queueFull():
		if items==size:
			return True
	def queueEmpty():
	 	if items==0:
	 		return True
	
	
	
	
if __name__ == '__main__':
			main()		