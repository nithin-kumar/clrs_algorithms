def findSum(a,p,r,num):
	if p<r:
		q=(p+r)/2
		return findSum(a,p,q,num) or findSum(a,q+1,r,num) or findCross(a,p,q,r,num)
def findCross(a,p,q,r,num):
	j=q+1
	i=q
	while i>=p and j<=r:
		if a[i]+a[j]==num:
			return i,j
		j=j+1
		i=i-1
	return None
def main():
	a=[5,6,9,12,11,111,0]
	num=11
	print findSum(a,0,len(a)-1,num)
if __name__ == '__main__':
	main()