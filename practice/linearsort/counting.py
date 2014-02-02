def counting_sort(a,b,k):
	c=[0]*(k+1)
	for i in range(0,len(a)):
		c[a[i]]+=1
	for j in range(1,k+1):
		c[j]+=c[j-1]
	for i in reversed(xrange(0,len(a))):
		b[c[a[i]]-1]=a[i]
		c[a[i]]-=1
	return b
def main():
	a=[0,1,2,3,2,3,1,2,3,4]
	k=4
	b=[0]*len(a)
	print counting_sort(a,b,k)
if __name__ == '__main__':
	main()