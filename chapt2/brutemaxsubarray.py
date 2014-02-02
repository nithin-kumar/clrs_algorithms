def max_subarray(a,low,high):
	max_diff=-999# it holds the maximum difference
	diff=0
	for i in range(low,high):
		for j in range(i+1,high+1):
			diff=a[j]-a[i]
			if diff>max_diff:
				max_diff=diff
				buy=i
				sell=j
	return a[buy],a[sell],max_diff
def main():
	a=[-1,2,3,-2,-7,18]
	
	print max_subarray(a,0,len(a)-1)
if __name__ == '__main__':
	main()
