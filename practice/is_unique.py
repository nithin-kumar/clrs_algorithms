#import StringIO
def isUnique(string):
	#buffer_=StringIO.StringIO()
	#list_=[]
	#for character in string:
		#if character not in list_: 
			#list_.append(character)
	#if len(string)!=len(list_):
		#return False
	#return True
	dict_={}
	for i in string:
		if dict_[i]:
			return False
		dict_[i]=True
	return True
def main():
	string='nith'
	if (isUnique(string)):
		print "String contains unique characters !!"
	else:
		print "Not unique !!!"
if __name__ == '__main__':
	main()
			
