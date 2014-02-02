def find_range_elements(a,k,p,q):# find no of elements in the range a[p..q]
	c=[0]*k
	for i in a:
		c[i]=c[i]+1
	for j in range(1,k):
		c[j]=c[j]+c[j-1]
	return c[q]-c[p-1]
def main():
	a=[2,5,3,0,2,3,0,3]
	k=6
	print find_range_elements(a,k,2,5)
if __name__ == '__main__':
	main()