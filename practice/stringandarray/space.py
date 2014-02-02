def replaceSpace(s,length):
	t=""
	for i in s:
		if i==" ":
			t+="%20"
		else:
			t+=i
	return t
def main():
	s="nithin  kumar "
	print replaceSpace(s,len(s))
if __name__ == '__main__':
	main()