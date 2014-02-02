def binaryinsertion(a,p,r):
	for j in range(p+1,len(a)-1):
		i=0
		key=a[j]
		mid=i+j/2
		if a[mid]>key:
			insert(a,mid,key)
	return a
def insert(a,k,key):
	i=k
	while(i>=0 and a[i]>key):
		a[i+1]=a[i]
		i=i-1
	a[i+1]=key
def main():
	a=[3,7,2,1,4,9]
	print binaryinsertion(a)
if __name__ == '__main__':
	main()