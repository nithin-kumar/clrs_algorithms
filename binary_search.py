import sys
def binsearch(a,p,r,x):
	if r<p:
		print r, p
		return "Not found"
	mid=(p+r)/2
	if a[mid]==x:
		return mid
	if(a[mid]>x):
		return binsearch(a,p,mid-1,x)
	else:
		return binsearch(a,mid+1,r,x)
def main():
	a=[1,3,4,5,6,8]
	x=48
	print binsearch(a,0,len(a)-1,x)
if __name__ == '__main__':
	main()
