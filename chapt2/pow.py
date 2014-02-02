def power(x,n):
	prod=1
	for i in range(0,n):
		prod*=x
	return prod
def main():
	x=2
	n=3
	print  power(x,n)
if __name__ == '__main__':
	main()