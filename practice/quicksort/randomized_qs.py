import random
def randomized_partition(a,l,r):
	random_indx=random.randrange(l,r+1)
	a[l],a[random_indx]=a[random_indx],a[l]
	pivot=a[l]
	i=l+1
	for j in range(l+1,r+1):
		if a[j]<pivot:
			a[i],a[j]=a[j],a[i]
			i=i+1
	a[l],a[i-1]=a[i-1],a[l]
	return i-1
def randomized_qs(a,l,r):
	if l<r:
		q=randomized_partition(a,l,r)
		randomized_qs(a,l,q-1)
		randomized_qs(a,q+1,r)
		return a
def main():
	a=[3,6,1,13,9,0,4]
	print randomized_qs(a,0,6)
if __name__ == '__main__':
	main()