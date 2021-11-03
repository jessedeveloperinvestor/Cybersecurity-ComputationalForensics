import hashlib
file1='Hashes.txt'
file2='Hashes2.txt'
hash1=hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())
hash2=hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())
if hash1.digest() != hash2.digest():
	print(f'The file: {file1} is different from {file2}')
	print('The hash of the file Hashes.txt is: ', hash1.hexdigest())
	print('The hash of the file Hashes2.txt is: ', hash2.hexdigest())
else:
	print(f'The file: {file1} is equal to {file2}')