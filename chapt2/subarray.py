def max_sub(a):
	n=len(a)
	max_sum=-9999
	ending_here_sum=-999
	for j in range(n):
		ending_here_high=j
		if ending_here_sum>0:
			ending_here_sum+=a[j]
		else:
			ending_here_low=j
			ending_here_sum=a[j]
		if ending_here_sum>max_sum:
			max_sum=ending_here_sum
			low=ending_here_low
			high=ending_here_high
		print ending_here_low
	return low,high,max_sum
def main():
	a=[-1,-2,-3]
	print max_sub(a)
if __name__ == '__main__':
	main()