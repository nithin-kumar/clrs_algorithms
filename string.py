dic=['hai','how','are','you','she','he','good','morning','evening','i','about','his','her','.']
def correct(s):
	word=''
	out=''
	for i in s:
		word=word+i
		if word in dic:
			out=out+word+" "
			word=''
	
	print out
def main():
	
	string="goodmorningyousheeveninghaiihegoodmorningyousheeveninghaiihegoodmorningyousheeveninghaiihegoodmorningyousheeveninghaiihegoodmorningyousheeveninghaiihevgoodmorningyousheeveninghaiihegoodmorningyousheeveninghaiihevvv"
	correct(string)
if __name__ == '__main__':
		main()