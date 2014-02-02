def isAnagram(s1,s2):
	if len(s1)!=len(s2):
		return False
	if s1==s2:
		return True
	s1_sorted=''.join(sorted(s1))
	s2_sorted=''.join(sorted(s2))
	return s1_sorted==s2_sorted
def isAnagram2(s,t):
	if len(s)!=len(t):
		return False
	boolean=[0]*256
	for i in s:
		boolean[ord(i)]+=1
	for j in t:
		if (--boolean[ord(j)]-1<0):
			return False
	return True
def main():
	s1="nithin"
	s2="nithsn"
	print isAnagram2(s1,s2)
if __name__ == '__main__':
	main()