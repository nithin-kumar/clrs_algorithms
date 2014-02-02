def find_cross(a,low,high):
	mid=(low+high)/2
	if low<high and mid>0:
		
		if a[mid]>a[mid-1] and a[mid+1]>a[mid]:
			mid =find_cross(a,low,mid)
			mid=find_cross(a,mid,high)
	return mid
def main():
	a=[9,10,11,12,3,8]
	print find_cross(a,0,len(a)-1)
if __name__ == '__main__':
	main()
	
