def recursive_insert(self,x,value):
	z=Node(value)
	if self.root==None:
		self.root=z
		return
	y=None
	if x==None:
		z.p=y
		elif y.key<z.key:
			y.right=z
		else:
			y.left=z
		return
	y=x
	if x.value<z.value:
		return recursive_insert(x.right,value)
	return recursive_insert(x.left,value)
