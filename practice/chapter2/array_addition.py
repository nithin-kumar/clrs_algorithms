def add(a,b):
	length_a=len(a)
	length_b=len(b)
	if length_a>=length_b:
		big=a
		small=b
	else:
		big=b
		small=a
	j=len(small)-1
	c=[0]*(len(big)+1)
	for i in reversed(xrange(0,len(big))):
		result=c[i+1]+big[i]
		if j>=0:
			result+=small[j]
			j=j-1
		c[i+1]=result%10
		c[i]=result/10
	return c
def main():
	a=[1,2,3]
	b=[1,2,3]
	print add(a,b)
if __name__ == '__main__':
	main()