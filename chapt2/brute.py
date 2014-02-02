def max_subarray(a,low,high):
	max_so_far=-999# it holds the maximum difference
	
	for i in range(low,high):
		sum_=0
		for j in range(i,high+1):
			sum_=sum_+a[j]
			if sum_>max_so_far:
				max_so_far=sum_
				buy=i
				sell=j
	return buy,sell,max_so_far
def main():
	a=[-1,2,3,-2,-7,18]
	print max_subarray(a,0,len(a)-1)
if __name__ == '__main__':
	main()
