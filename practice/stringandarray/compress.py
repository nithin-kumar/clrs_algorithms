def stringCompress(a):
	i=1
	t=""
	word=""
	j=0
	while i<len(a):
		count=1
		while a[i]==a[i-1]:
			count+=1
			i+=1
			if i>=len(a):
				break
		word=a[j]+str(count)
		t+=word
		i=i+1
		j=j+count
	return t
def main():
	s="aabcccc"
	print stringCompress(s)
if __name__ == '__main__':
	main()

