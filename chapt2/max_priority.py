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
	return a
def heap_sort(a,heapsize):
	build_max_heap(a,heapsize)
	#heapsize=heapsize-1
	#print a
	for i in reversed(xrange (1,heapsize+1)):
		a[0],a[i]=a[i],a[0]
		#heapsize=heapsize-1
		max_heapify(a,0,i)
	return a
def heap_maximum(a):
	return a[0]
def heap_extract_max(a,heapsize):
	if heapsize<1:
		return "Underflow"
	maximum=a[0]
	a[0]=a[heapsize]
	heapsize=heapsize-1
	max_heapify(a,0,heapsize)
	return maximum,a
def increase_key(a,i,key):
	if(a[i]>key):
		return "NO BENEFIT"
	#a[i]=key
	#while (i>=0 and a[parent(i)]<a[i]):
		#a[i],a[parent(i)]=a[parent(i)],a[i]
		#i=parent(i)
	while (i>0 and a[parent(i)]<key):
		a[i]=a[parent(i)]
		i=parent(i)
	a[i]=key
	return a
def heap_insert(a,key,heapsize):
	heapsize=heapsize+1
	a.append(-999)
	increase_key(a,heapsize,key)
	return a
def enqueue(a,x,heapsize):
	if(heapsize==0):
		a.append(x)
		heapsize=1
		return a,heapsize
	else :
		return heap_insert(a,x,heapsize)

def dequeue(a,heapsize):
	return heap_extract_max(a,heapsize)

def main():
	a=[]
	heapsize=len(a)-1
	#print heap_sort(a,heapsize)
	#print build_max_heap(a,heapsize)
	#print heap_maximum(a)
	#print heap_extract_max(a,heapsize)
	#print heap_insert(a,22,heapsize)
	#print increase_key(a,1,45)
	a,heapsize= enqueue(a,2,heapsize)
	print a
	#print enqueue(a,5,heapsize)
	#print a
	print dequeue(a,heapsize)

	

if __name__ == '__main__':
	main()
