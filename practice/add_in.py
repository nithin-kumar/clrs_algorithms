def add(a,b):
	length_a=len(a)
	length_b=len(b)
	if length_a>=length_b:
		big=a
		small=b
	else:
		big=b
		small=a
	carry=0
	c=[0]*(len(big)+1)
	j=len(small)-1
	for i in reversed(xrange(0,len(big))):
		result=c[i+1]+big[i]
		#print result
		if j>=0:
			result=result+small[j]
		j=j-1
		c[i+1]=result%10
		c[i]=result/10
		#result=0
	#if carry!=0:
	#	c[0]=carry
	return c
def main():
	a=[1,0,0]
	b=[1,0,0]
	print add(a,b)
if __name__ == '__main__':
	main()

