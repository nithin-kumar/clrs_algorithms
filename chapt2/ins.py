def insertionsort(a,n):
	if n==0:
		return a[n]
	else:
		key =a[n]
		insertionsort(a,n-1)
		i=n-1
		while i>0 and a[i]>key:
			a[i+1]=a[i]
			i=i-1
		a[i+1]=key
def main():
	a=[5,2,1,3,10,7]
	print insertionsort(a,5)
if __name__ == '__main__':
	main()