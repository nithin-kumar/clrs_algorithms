def min_max(a):
	min_=a[0]
	max_=a[0]
	for i in range(1,len(a)):
		if a[i]<min_:
			min_=a[i]
		elif a[i]>max_:
			max_=a[i]
	return min_,max_

def main():
	a=[1,2,3,32,4,4,5,6,7,989]
	print min_max(a)
if __name__ == '__main__':
	main()
