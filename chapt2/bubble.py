def bubble(a):
	for i in range(0,len(a)-1):
		for j in range(0,len(a)-i-1):
			if a[j]>a[j+1]:
				a[j],a[j+1]=a[j+1],a[j]
	return a
def main():
	a=[98,5,4,13,6,7,8,0]
	print bubble(a)

if __name__ == '__main__':
	main()