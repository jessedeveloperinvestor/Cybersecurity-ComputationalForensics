import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket was built successfuly')
host='localhost'
port=5432
s.bind((host, port))
message='Server: Hello client'
while 1:
	data, end = s.recvfrom(6096)
	if data:
		print('Server sending message...')
		s.sendto(data+(message.encode()), end)