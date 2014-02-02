#implementation of partition

def quicksort(a,l,r):
	p=a[l] #choose a pivot element
	#partition around pivot element 
	i=l+1
	for j in range(l+1,r):
		if a[j]<p:
			a[i],a[j]=a[j],a[i]
			i=i+1
	a[l],a[i-1]=a[i-1],a[l]

	quicksort(a,l,i-1)
	quicksort(a,i+1,r)
	return a

def main():
	a=[3,8,2,5,1,4,7,6]
	print quicksort(a,0,len(a))

if __name__ == '__main__':
	main()
