#2 stack in single array
def main():
	a=[]
	top=-1
	def push(x):
		a.append(x)
		return a
	def pop():
		a.pop()
	print push(2)
	print push(3)
	pop()
	print a
if __name__ == '__main__':
	main()
