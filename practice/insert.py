class Node:
	def __init__(self,value):
		self.key=value
		self.left=None
		self.right=None
		self.p=None
class BST:
	"""docstring for BST"""
	def __init__(self):
		self.root=None
	def insert(self,x,z):
		new_node=Node(z)
		if self.root==None:
			self.root=new_node
			return
		if new_node.key<x.key:
			if x.left==None:
				x.left=new_node
			else:
				self.insert(x.left,z)
		else:
			if x.right==None:
				x.right=new_node
			else:
				self.insert(x.right,z)

		
bst=BST()
arr=[2,6,5,3,1]
for i in arr:
	bst.insert(bst.root,i)
#print bst.root.right.key
#bst.insert(bst.root,10)

print bst.root.key

