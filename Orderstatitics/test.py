def min_max(a):
	min_=a[0]
	max_=a[0]
	sec=0
	for i in range(1,len(a)):
		if a[i]<min_:
			sec=min_
			min_=a[i]
		elif a[i]>max_:
			max_=a[i]
	return min_

def main():
	a=[0,1,2,3,-1,32,4,4,5,6,7,989]
	print min_max(a)
if __name__ == '__main__':
	main()
