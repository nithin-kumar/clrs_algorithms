def add(a,b,c):
	for i in range(len(a)):
		temp=a[i]+b[i]+c[i]
		c[i]=temp%2
		c[i+1]=temp/2
	return c
def main():
	a=[1000]
	b=[1100]
	c=[0000]
	print add(a,b,c)
if __name__ == '__main__':
	main()
