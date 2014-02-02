def insertion_sort(a,n):
	#print a
	if n>0:
		insertion_sort(a,n-1)
		return insert(a,n)
def insert(a,k):
	key=a[k]
	i=k-1
	while i>=0 and a[i]>key:
		a[i+1]=a[i]
		i=i-1
	a[i+1]=key
	return a 
def main():
	a=[4,7,1,2,39]
	print insertion_sort(a,4)
if __name__ == '__main__':
	main()