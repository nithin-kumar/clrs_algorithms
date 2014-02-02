def rotate(a,n):
	for layer in range(0,(n/2)):
		first=layer
		last=n-1-layer
		for i in range(first,last):
			offset=i-first
			#save the top
			temp=a[first][i]
			#left---->top
			a[first][i]=a[last-offset][first]
			#bottom---->left
			a[last-offset][first]=a[last][last-offset]
			#right----->bottom
			a[last][last-offset]=a[i][last]
			#top--->right
			a[i][last]=temp
	return a
def main():
	a=[[1,2,3],[4,5,6],[7,8,9]]
	print rotate(a,3)
if __name__ == '__main__':
	main()