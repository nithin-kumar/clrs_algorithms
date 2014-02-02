class parent:
	def __init__(self):
		self.hai=0
	def sayhai(self,name):
		print "hai",name
class child(parent):
	def __init__(self):
		self.p=parent()
		self.sayhai('Nithin')
		self.p.sayhai('Jithin')
		print self.p.hai
c=child()