def power(a,n):
	if n==1:
		return a
	return a*power(a,n-1)
def main():
	print power(2,10)
if __name__ == '__main__':
	main()