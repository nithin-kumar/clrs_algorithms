#finding the second min
def min_max(a,count):
	min_=a[0]
	max_=a[0]
	l=[]
	s=[]
	for i in range(1,len(a)):
		if a[i]<min_:
			l.append(min_)
			s.append(a[i])
			min_=a[i]
		#else:
			#s.append(a[i])
			
		#elif a[i]>max_
	count=count+1
	if count==5:
		return min_
	return min_max(l,count)

def main():
	count=0
	a=[1,2,3,32,4,0,-1,4,-6,5,6,7,989]
	print min_max(a,count)
if __name__ == '__main__':
	main()
