def binary_search(a,p,r,key):
	if p<=r: 
		q=(p+r)/2
		if a[q]==key:
			return q,True
		if a[q]>key:
			return binary_search(a,p,q-1,key)
		return binary_search(a,q+1,r,key)
def binary_search_iterative(a,p,r,key):
	while(p<=r):
		q=(p+r)/2
		if a[q]==key:
			return q,True
		if a[q]>key:
			r=q-1
		else:
			p=q+1
	return False
def main():
	a=[3,4,5,6,7]
	print binary_search_iterative(a,0,4,7)
if __name__ == '__main__':
	main()

