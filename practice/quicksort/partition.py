def partition(a,l,r):
	pivot=a[l]
	i=l+1
	counter=0
	for j in range(l+1,r+1):
		if a[j]<pivot:
			a[i],a[j]=a[j],a[i]
			i=i+1
		else:
			counter+=1
	a[l],a[i-1]=a[i-1],a[l]
	if counter==len(a)-1:
		return (l+r)/2
	return i-1
def main():
	a=[4,4,4,4,4,5]
	print partition(a,0,5)
if __name__ == '__main__':
	main()