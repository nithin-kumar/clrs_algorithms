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
	def tree_insert(self,value):
		new_node=Node(value)
		x=self.root
		y=None
		while x!=None :
			y=x
			if x.key>new_node.key:
				x=x.left
			else:
				x=x.right
		new_node.p=y
		if y==None:
			self.root=new_node
		elif y.key>new_node.key:
			y.left=new_node
		else:
			y.right=new_node
	def recursive_insert(self,x,value):
		z=Node(value)
		if self.root==None:
			self.root=z
			return
		if z.key<x.key:
			if x.left==None:
				x.left=z
				return
			else:
				self.recursive_insert(x.left,value)
		else:
			if x.right==None:
				x.right=z
				return
			else:
				self.recursive_insert(x.right,value)
			
		
	def inorder_tree_walk(self,x):
		if x is not None:
			self.inorder_tree_walk(x.left)
			print x.key
			self.inorder_tree_walk(x.right)
			#return x.left.left.key,x.right.key
	def preorder(self,x):
		if x!=None:
			print x.key
			self.preorder(x.left)
			self.preorder(x.right)
	def search(self,x,key):
		if x==None or x.key==key:
			return x
		if key<x.key:
			return self.search(x.left,key)
		return self.search(x.right,key) 
	def iterative_search(self,key):
		x=self.root
		while x!=None and x.key!=key:
			if x.key<key:
				x=x.right
			else:
				x=x.left
		return x.key
	def tree_minimum(self):
		x=self.root
		while x.left!=None:
			x=x.left
		return x
	def recursive_tree_minimum(self,x):
		if x.left==None:
			return x
		return self.recursive_tree_minimum(x.left)
	def tree_maximum(self,x):
		#x=self.root
		while x.right!=None:
			x=x.right
		return x

	def recursive_tree_maximum(self,x):
		if x.right==None:
			return x
		return self.recursive_tree_maximum(x.right)
	def transplant(self,u,v):
		if u.p==None:
			self.root=v
		elif u==u.p.left:
			u.p.left=v
		else:
			u.p.right=v
		if v!=None:
			v.p=u.p
	def predecessor(self,x):
		if x.left!=None:
			return self.tree_maximum(x.left)
		else:
			y=x.p
			while y!=None and y.key>x.key:
				y=y.p
			return y
	def successor(self,x):
		if x.right!=None:
			return self.tree_minimum(x.right)
		else:
			y=x.p
			while y!=None and y.key<x.key:
				y=y.p
			return y
	def delete(self,key):
		z=self.search(self.root,key)
		#print z.key
		if z.left==None and z.right==None:
			return self.transplant(z,None)
		if z.left==None:
			return self.transplant(z,z.right)
		elif z.right==None:
			return self.transplant(z,z.left)
		else:
			y=self.predecessor(z)
			y.key,z.key=z.key,y.key
			return self.transplant(y,y.left)
	def height(self,x):
		if x==None:
			return 0
		return 1+max(self.height(x.left),self.height(x.right))
	def parent(self,x1):
		x=Node(x1)
		parent=None
		y=self.root
		#return x.key, y.key
		while(y.key!=x.key and y!=None):
			parent=y
			if y.key>x.key:
				y=y.left
			else:
				y=y.right
		return parent.key
	def diameter(self,x):
		if x==None:
			return 0
		leftD=self.diameter(x.left)
		rightD=self.diameter(x.right)
		rootD=self.height(x.left)+self.height(x.right)+1
		return max(leftD,max(rightD,rootD))

bst=BST()
#bst.tree_insert(5)
#print bst.root.key
#bst.tree_insert(15)

#bst.tree_insert(15)
#bst.recursive_insert(bst.root,115)
#bst.recursive_insert(bst.root,15)
#
#print bst.root.right.key
#print bst.root.left
arr = [20,2,1,0,3,4,5,6,7,8,9,10,11,25,26,27,28]
for i in arr:
    bst.recursive_insert(bst.root,i)
height=bst.height(bst.root)
print bst.diameter(bst.root)
print height

#print bst.parent(5)
#print bst.root.key
#bst.tree_insert(10)
#bst.tree_insert(16)
#
#print "--------"
#bst.preorder(bst.root)
#print bst.search(bst.root,161)
#print bst.iterative_search(101)
#print bst.recursive_tree_maximum(bst.root)
#y=bst.recursive_tree_minimum(bst.root)
#print y
#for i in range(9):
	#y=successor(y)
	#print y

#print bst.root.right.right.key
#bst.delete(8)

#print bst.tree_maximum(bst.root)
#print bst.root.key
#print bst.root.left.key





