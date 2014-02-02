#Name:Insertion.py
#To sort given sequence of numbers
def insertion(A):
	for j in range(1,len(A)):
		key=A[j]
		i=j-1
		while(i>=0 and A[i]>key):
			A[i+1]=A[i]
			i=i-1
		A[i+1]=key
	return A
def main():
	print insertion([2,3,1,8,5,6,89,4,33,0])
if __name__ == '__main__':
	main()

	