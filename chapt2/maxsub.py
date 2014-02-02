def find_maximum_crossing_subarray(a,low,mid,high):
	left_sum=-999
	sum_=0
	for i in reversed(xrange(low,mid+1)):
		sum_+=a[i]
		if sum_>left_sum:
			left_sum=sum_
			max_left=i
	right_sum=-999
	sum_=0
	for j in range(mid+1,high+1):
		sum_+=a[j]
		if sum_>right_sum:
			right_sum=sum_
			max_right=j
	return (max_left,max_right,left_sum+right_sum)

def find_maximum_subarray(a,low,high):
	if low==high:
		return (low,high,a[low])
	mid=(low+high)/2
	
	(left_low,left_high,left_sum)=find_maximum_subarray(a,low,mid)
	
	(right_low,right_high,right_sum)=find_maximum_subarray(a,mid+1,high)
	
	(cross_low,cross_high,cross_sum)=find_maximum_crossing_subarray(a,low,mid,high)
	if (left_sum>=right_sum and left_sum>=cross_sum):
		return (left_low,left_high,left_sum)
	elif(right_sum>=left_sum and right_sum>=cross_sum):
		return (right_low,right_high,right_sum)
	else :
		return (cross_low,cross_high,cross_sum)
def main():
	a=[-1,9,9,-22,7,17]
	print find_maximum_subarray(a,0,len(a)-1)
if __name__ == '__main__':
	main()