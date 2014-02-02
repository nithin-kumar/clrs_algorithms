def merge(a,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[0]*n1
	R=[0]*n2
	for i in range(0,n1):
		L[i]=a[p+i]
	for j in range(0,n2):
		R[j]=a[q+j+1]
	i=0
	j=0
	k=p
	while i<n1 and j<n2:
		if L[i]<=R[j]:
			a[k]=L[i]
			k=k+1
			i=i+1
		else:
			a[k]=R[j]
			k=k+1
			j=j+1
	while i<n1:
		a[k]=L[i]
		k=k+1
		i=i+1
	return a
def main():
	a=[12,13,15,2,4,5]
	print merge(a,0,2,5)
if __name__ == '__main__':
	main()
