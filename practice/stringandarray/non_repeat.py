def non_repeat(s):
	boolean =[0]*256
	for i in s:
		boolean[ord(i)]+=1
	for i in s:
		if boolean[ord(i)]==1:
			return i
	return False
def main():
	s="nitthhin"
	print non_repeat(s)
if __name__ == '__main__':
	main()