import random
def partition(a,l,r):
	p=random.randrange(l,r+1)
	a[l],a[p]=a[p],a[l]
	i=l
	h=l
	pivot=a[l]
	for j in range(l+1,r+1):
		if a[j]==pivot:
			a[h+1],a[j]=a[j],a[h+1]
			h=h+1
		elif a[j]<pivot:
			y=a[j]
			a[j]=a[h+1]
			a[h+1]=a[i]
			a[i]=y
			i=i+1
			h=h+1
	return i,h,a
def quicksort(a,l,r):
	if l<r:
		q,t=partition(a,l,r)
		quicksort(a,l,q-1)
		quicksort(a,t+1,r)
		return a
def main():
	a=[6,22,4,6,7,4,5,6,4]
	print quicksort(a,0,len(a)-1)
if __name__ == '__main__':
	main()