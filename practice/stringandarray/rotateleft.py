def rotate(a,n):
	for layer in range(0,n/2):
	#layer=0
		first=layer
		last=n-1-layer
		for i in reversed(xrange(first,last)):
			offset=last-last
			#save top
			temp=a[i][last]
			#right---->top
			a[first][last]=a[last-offset][last]
			#bottom--->right
			a[last-offset][last]=a[last][offset-first]
			#left ----->bottom
			a[last][offset-first]=a[offset-first][i]
			#top--->left
			a[offset-first][i]=temp
	return a
def main():
	a=[[1,2,3],[4,5,6],[7,8,9]]
	print rotate(a,3)
if __name__ == '__main__':
	main()