def merge(a,b):
	i=len(a)-len(b)-1
	k=len(a)-1
	j=len(b)-1
	while i>=0 and j>=0:
		if a[i]>=b[j]:
			a[k]=a[i]
			k-=1
			i-=1
		else:
			a[k]=b[j]
			k-=1
			j-=1
	while j>=0:
		a[k]=b[j]
		k-=1
		j-=1
	return a
def main():
	a=[3,5,7,8,9,0,0,0,0,0]
	b=[1,4,6,10,11]
	print merge(a,b)
if __name__ == '__main__':
	main()