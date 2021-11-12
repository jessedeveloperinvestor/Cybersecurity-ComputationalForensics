import itertools
string=input('Type in the string to ber permuted/form the words/passwords of the Wordlist\n')
result=itertools.permutation(string, len(string))
for i in result:
	print(''.join(i))