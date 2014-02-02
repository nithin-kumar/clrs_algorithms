def merge(a,p,q,r):
	n1=q-p+1
	n2=r-q
	l=[0]*(n1+1)
	r=[0]*(n2+1)
	for i in range(0,n1):
		l[i]=a[p+i]
	for j in range(0,n2):
		r[j]=a[q+j+1]
	return l,r
def main():
	a=[5,8,9,2,3]
	print merge(a,0,2,4)
if __name__ == '__main__':
	main()
