def repalacewithzero(a,m,n):
	row=[False]*m
	column=[False]*n
	for i in range(0,m):
		for j in range (0,n):
			if a[i][j]==0:
				row[i]=True
				column[j]=True
	for i in range(0,m):
		for j in range(0,n):
			if row[i] or column[j]:
				a[i][j]=0
	return a
def main():
	a=[[1,2,3],[4,0,5],[6,7,8]]
	print repalacewithzero(a,3,3)
if __name__ == '__main__':
	main()