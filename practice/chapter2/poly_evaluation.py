def poly(a,x):
	sum_=a[0]
	for i in range(1,len(a)):
		prod=1
		j=1
		while(j<=i):
			prod*=x
			j+=1
		sum_+=a[i]*prod
	return sum_
def horner(a,x):
	y=0
	for i in reversed(xrange(0,len(a))):
		y=a[i]+x*y
	return y
def main():
	a=[1,2,0,5]
	x=1
	print poly(a,x)
	print horner(a,x)
if __name__ == '__main__':
	main()