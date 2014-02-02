class Stack:
	def __init__(self):
		self.top=-1
		self.a=[]
		#self.min=9999
	
	def push_(self,x):
		self.a.append(x)
		#if x<self.min:
			#self.min=x
		self.top=self.top+1
	def print_stack(self):
		return self.a
	def pop_(self):
		if self.isEmpty():
			return "Underflow"
		self.top=self.top-1
		return self.a.pop()
		
	def isEmpty(self):
		if self.top==-1:
			return True
		return False
	def min_(self):
		return self.min
	def peek(self):
		return self.a[self.top]

class stackmin:
	def __init__(self):
		self.s1=Stack()
		self.s2=Stack()
		self.min_=10000
	def push__(self,x):
		if x<self.min_:
			self.min_=x
			self.s2.push_(x)
		self.s1.push_(x)
	def pop__(self):
		x=self.s1.pop_()
		if x==self.s2.peek():
			self.s2.pop_()
		return x
	def peek_(self):
		return self.s1.peek()
	def minimum(self):
		return self.s2.peek()

s=stackmin()
s.push__(2)
s.push__(1)
s.push__(10)
s.push__(5)
#print s.minimum()
print s.pop__()

print s.pop__()
print s.pop__()
print s.minimum()
#print s.pop__()
#print s.pop__()
#s1=Stack()
#s1.push_(3)
#s2=Stack()
#s1.push_(1)
#s1.push_(0)
#s1.push_(7)
#print s1.peek()
#print s1.pop_()
#print s1.pop_()
#print s1.top
#print s1.isEmpty()