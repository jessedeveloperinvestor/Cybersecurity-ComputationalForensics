import hashlib
string-input('Type in the text to get hashed')
menu=int(input(''' ### CHOOSE THE KIND OF HASH ###\n1)MD5\n2)SHA1\n3)SHA256\n4)SHA512\nType in the number of wished kind of hash '''))
if menu==1:
	result=hashlib.md5(string.encode('utf-8'))
	print('The hash MD5 of the string ',string' is: ',result.hexdigest())
elif menu==2:
	result=hashlib.sha1(string.encode('utf-8'))
	print('The hash SHA1 of the string ',string' is: ',result.hexdigest())
elif menu==3:
	result=hashlib.sha256(string.encode('utf-8'))
	print('The hash SHA256 of the string ',string' is: ',result.hexdigest())
elif menu==4:
	result=hashlib.sha512(string.encode('utf-8'))
	print('The hash SHA512 of the string ',string' is: ',result.hexdigest())
else:
	print('Issue. Try again.')