def left(i):
	return (2*i)+1
def right(i):
	return (2*i)+2
def max_heapify(a,i,heapsize):
	l=left(i)
	r=right(i)
	if(l<heapsize and a[l]>a[i]):
		largest=l
	else:
		largest=i
	if(r<heapsize and a[r]>a[largest]):
		largest=r
	if largest!=i:
		a[i],a[largest]=a[largest],a[i]
		max_heapify(a,largest,heapsize)
	return a
def build_max_heap(a,n):
	for i in reversed(xrange(0,n/2)):
		max_heapify(a,i,len(a))
def heap_sort(a):
	build_max_heap(a,len(a)-1)
	print a
	for i in reversed(xrange(1,len(a))):
		
		a[0],a[i]=a[i],a[0]
		max_heapify(a,0,i)
	return a
def main():
	a=[8,3,5,1,44,34,56,677]
	print heap_sort(a)
if __name__ == '__main__':
	main()
