 def parent(i):
	return i/2
def left(i):
	return (2*i)+1
def right(i):
	return (2*i)+2
def max_heapify(a,i,heapsize):
	while(i<heapsize/2):
		l=left(i)
		r=right(i)
	#print r
		if l<heapsize and a[l]>a[i]:
			largest=l
		else:
			largest=i
		if r<heapsize and a[r]>a[largest]:
			largest=r
		if largest!=i:
			a[i],a[largest]=a[largest],a[i]
			#max_heapify(a,largest,heapsize)
			i=largest
		else:
			break
def build_max_heap(a,n):
	for i in reversed(xrange(0,(n/2))):
	
		max_heapify(a,i,len(a))

def heap_sort(a,heapsize):
	build_max_heap(a,heapsize)
	#heapsize=heapsize-1
	for i in reversed(xrange (1,heapsize+1)):
		a[0],a[i]=a[i],a[0]
		#heapsize=heapsize-1
		max_heapify(a,0,i)
	return a
def main():
	a=[5,13,2,25,7,17,20,8,4,0,11]
	heapsize=len(a)-1
	print heap_sort(a,heapsize)

if __name__ == '__main__':
	main()
