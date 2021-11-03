import socket
s=socket.socket(socketAF_INET, socket.SOCK_DGRAM)
print('Socket client was created successfully')
host='localhost'
port=5433
message='Hello server, how are you?'
try:
	print('Client: '+message)
	s.sendto(message.encode(), (host, 5432))
	data, server = s.recvfrom(4096)
	data=data.decode()
	print('Client: '+data)
finally:
	print('Client: Closing connection')
	s.close()