def cross(a,l,u,x):
	while (l <= u):
		m = (l + u) / 2
		if (x == a[m]):
			return m
		elif (a[l] <= a[m]):
			if (x > a[m]):
				l = m+1
			elif (x >=a [l]):
				u = m-1
			else :
				l = m+1
		elif (x < a[m]):
			u = m-1
		elif (x <= a[u]):
			l = m+1
		else :
			u = m - 1
	return -1
def main():
	a=[9,13,17,6,7,8]
	print cross(a,0,len(a)-1,112)
if __name__ == '__main__':
	main()
