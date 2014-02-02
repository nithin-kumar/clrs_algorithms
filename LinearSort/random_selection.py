import random
def randomized_select(a,p,r,i):
	if p==r:
		return a[p]
	q=randomized_partition(a,p,r)
	k=p-q+1
	if i==k:
		return a[q]
	elif i<k:
		return randomized_select(a,p,q-1,i)
	else:
		return randomized_select(a,q+1,r,k-i)
def randomized_partition(a,p,r):
	pivot=random.randrange(p,r+1)
	a[p],a[pivot]=a[pivot],a[p]
	i=p+1
	p=a[p]
	for j in range(p+1,r+1):
		if a[j]<=p:
			a[i],a[j]=a[j],a[i]
			i=i+1
	a[0],a[i-1]=a[i-1],a[0]
	return i-1
def main():
	a=[3,5,7,2,4,6,8]
	print randomized_select(a,0,len(a)-1,3)