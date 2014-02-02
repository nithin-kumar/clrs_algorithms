class array(object):
	"""docstring for array"""
	def __init__(self, arr):
		self.a=arr
	def insertion_sort(self):
		for j in range(1,len(self.a)):
			key=self.a[j]
			i=j-1
			while i>=0 and self.a[i]>key:
				self.a[i+1]=self.a[i]
				i=i-1
			self.a[i+1]=key
		return self.a
arr=[4,3,2,8,0]
a1=array(arr)
print a1.insertion_sort()