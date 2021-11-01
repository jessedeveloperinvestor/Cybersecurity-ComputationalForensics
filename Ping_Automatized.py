import os
with open('hosts.txt') as file:
	dump=file.read()
	dump=dump.splitlines()
	for ip in dump:
		print('Checking IP: ',ip)
		os.system('ping -n 2 {}'.format(ip))