def mege(a,b):
	i=len(a)-len(b)-1#asuume a has space enough to hold b
	print i
	j=len(b)-1
	k=len(a)-1
	while(i>=0 and j>=0):
		if a[i]>=b[j]:
			a[k]=a[i]
			k=k-1
			i=i-1
		else:
			a[k]=b[j]
			k=k-1
			j=j-1
	
	while(j>=0):
		a[k]=b[j]
		k=k-1
		j=j-1
	return a

def main():
	a=[1,5,8,12,14,0,0,0,0]
	b=[21,50,70,111]
	print mege(a,b)
if __name__ == '__main__':
	main()