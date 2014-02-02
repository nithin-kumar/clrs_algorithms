def reverse(a):
	j=len(a)-1
	i=0
	#print a
	while(i<j):
		print a
		#print a[i]
		a[i],a[j]=a[j],a[i]
		#print a
		j=j-1
		i=i+1
	return a
def main():
	a=[-1,2]
	print reverse(a)
if __name__ == '__main__':
	main()