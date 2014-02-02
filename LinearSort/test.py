def countingsort(a,b,c,k):
	#for i in range(k+1):
		#c.append(0)
	for j in a:
		c[j]=c[j]+1
	print c
	for i in range(1,k):
		c[i]=c[i-1]+c[i]
	print c
	for j in reversed(xrange(len(a))):
		
		b[c[a[j]]-1]=a[j]
		c[a[j]]=c[a[j]]-1
	return b,c
def main():
	a=[6,0,2,0,1,3,4,6,1,3,2]
	b=[0]*(len(a))
	k=7
	c=[0]*(k)
	#print c
	#c=[]
	print countingsort(a,b,c,k)
if __name__ == '__main__':
	main()