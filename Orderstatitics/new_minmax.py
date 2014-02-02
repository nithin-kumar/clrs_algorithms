#3 comparison for 2 element
def minmax_new(a):
	#assume n is odd
	print len(a)
	if len(a)%2==0:
		k=2
		min_=a[0]
		max_=a[1]
		if(a[0]>a[1]):
			min_=a[1]
			max_=a[0]
	else:
		k=1
		min_=a[0]
		max_=a[0]
	for i in range(k,len(a)-1):
		if a[i+1]<a[i]:
			if a[i+1]<min_:
				min_=a[i+1]
			if a[i]>=max_:
				max_=a[i]
		else:
			if a[i+1]>max_:
				max_=a[i+1]
			if a[i]<min_:
				min_=a[i]
	return max_,min_
def main():
	a=[0,1,-1]
	print minmax_new(a)
if __name__ == '__main__':
	main()
