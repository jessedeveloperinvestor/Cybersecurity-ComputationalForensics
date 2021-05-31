import socket
resp='S'
while(resp=='S'):
	url=input('Insert a URL: ')
	ip=socket.gethostbyname(url)
	print("This link's IPv4 is: "+ip)
	resp=input("Insert 'S' to continue or something else to exit ").upper()