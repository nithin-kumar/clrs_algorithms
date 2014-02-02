def find_sum(a,sum_):
	l=[]
	dic={}
	for i in range(0,len(a)):
		dic[a[i]]=i
	for i in range (0,len(a)):
		if sum_-a[i] in dic:
			l.append((i,dic[sum_-a[i]]))
	return l
def main():
	a=[4,5,2,7,1]
	print find_sum(a,9)
if __name__ == '__main__':
	main()