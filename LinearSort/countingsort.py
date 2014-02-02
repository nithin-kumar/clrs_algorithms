def countingsort(a,b,c,k):
	#for i in range(k+1):
		#c.append(0)
	for j in range(len(a)):
		c[a[j]]=c[a[j]]+1
	print c
	for i in range(1,k+1):
		c[i]=c[i-1]+c[i]
	print c
	for j in reversed(xrange(len(a))):
		print j
		b[c[a[j]]]=a[j]
		c[a[j]]=c[a[j]]-1
	return b
def main():
	a=[2,5,3,0,2,3,0,3]
	b=[0]*(len(a))
	k=6
	c=[0]*(k)
	print c
	#c=[]
	print countingsort(a,b,c,k)
if __name__ == '__main__':
	main()