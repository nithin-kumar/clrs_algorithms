def merge(a,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[0]*(n1+1)
	R=[0]*(n2+1)
	for i in range(0,n1):
		L[i]=a[p+i]
	for j in range(0,n2):
		R[j]=a[q+j+1]
	L[n1]=10000
	R[n2]=10000
	i=0
	j=0
	print L,R
	for k in range(p,r+1):
		if L[i]<=R[j]:
			a[k]=L[i]
			i=i+1
		else:
			a[k]=R[j]
			j=j+1
	return a
def main():
	a=[0,5,8,9,2,3,10]
	print merge(a,0,3,6)
if __name__ == '__main__':
	main()
