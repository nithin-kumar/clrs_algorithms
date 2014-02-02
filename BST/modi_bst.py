class Node:
	def __init__(self,value):
		self.key=value
		self.left=None
		self.right=None
		self.succ=None
class BST:
	def __init__(self):
		self.root=None
	def parent(self,x1):
		x=Node(x1)
		parent=None
		y=self.root
		while x!=y:
			parent=y
			if y.key>x.key:
				y=y.left
			else:
				y=y.right
		return parent
	def insert(self,z):
		node=Node(z)
		y=None
		x=self.root
		while x!=None:
			y=x
			if node.key<x.key:
				x=x.left
			else:
				x=x.right
		if y==None:
			self.root=node
		elif y.key>node.key:
			node.succ=y
			y.left=node
		else:
			y.succ=node
			y.right=node
bst =BST()
arr=[12,9,14,1,2,11,16]
for i in arr:
	bst.insert(i)
#print bst.root.right.left.succ.key
print bst.parent(9).key