def isUnique(s):
	if len(s)>256:
		return False
	for i in range(0,len(s)):
		for j in s[i+1:]:
			if s[i]==j:
				return False
	return True
def main():
	s="niaa"
	print isUnique(s)
if __name__ == '__main__':
	main()