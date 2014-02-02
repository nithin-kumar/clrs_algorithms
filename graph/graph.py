class vertex:
	def __init__(self,value):
		self.id=value
		self.connectedTo={}
	def getId(self):
		return self.id
	def addNeighbour(self,nbr,weight=0):
		self.connectedTo[nbr]=weight
	def getConnection(self):
		return self.connectedTo.keys()
	def getWieight(self,nbr):
		return self.connectedTo[nbr]
	def removeNighbour(self,nbr):
		self.connectedTo[nbr]=None
class Graph:
	def __init__(self):
		self.adjList={}
		self.vertices=0
	def addVertex(self,key):
		newvertex=vertex(key)
		self.adjList[key]=newvertex
		self.vertices+=1
	def getVertex(self,n):
		if n in adjList:
			return adjList[n]
		return None
	def __contains__(self,n):
		return n in adjList

	def getAllVertices(self):
		return self.adjList.keys()
	def countVertices(self):
		return self.vertices
	def addEdge(self,src,targ,cost):
		if src not in self.adjList:
			self.addVertex(src)
		if targ not in self.adjList:
			self.addVertex(targ)
		self.adjList[src].addNeighbour(targ,cost)
	def printGraph(self):
		for i in self.adjList:
			for j in self.adjList[i]:
				print i,j


g=Graph()
for i in range(4):
	g.addVertex(i)
#g.addEdge(0,1,5)
print g

print g.adjList[0].id

