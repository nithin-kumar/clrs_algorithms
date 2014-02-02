def insertion(a):
  for j in range(1,len(a)):
  	key=a[j]
  	i=j-1
  	while(i>=0 and a[i]>key):
  		a[i+1]=a[i]
  		i=i-1
  	a[i+1]=key
  return a

def main():
	print insertion([9,7,5,4,3,2,1])
if __name__ == '__main__':
	main()