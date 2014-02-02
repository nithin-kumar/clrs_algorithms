#logn time algorihtm for finding the exponent of the number
import time
def power2(a,n):
	if a==0 and n==0:
		return "Math Error!!"
	exponent=n
	number=a
	product=1
	while(exponent>0):
		if exponent%2==0:
			number*=number
			exponent=exponent/2
		else:
			product*= number
			exponent-=1
	return product

def main():
	print power2(10,10)
if __name__ == '__main__':
	main()