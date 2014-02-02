def poly(a,x):
	k=len(a)
	sum=a[0]
	for i in range(1,k):
		l=1
		z=a[i]
		for j in range(0,i):
			l=l*x
		sum+=z*l
	return sum
def main():
	a=[1,4,5]
	x=2
	print poly(a,x)
if __name__ == '__main__':
	main()
