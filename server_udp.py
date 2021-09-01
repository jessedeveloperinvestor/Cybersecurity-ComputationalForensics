from socket import *
server='127.0.0.1'
port=43210
msg=bytes(input('Insert something: '), 'utf-8')
obj_socket=socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server,port))
print('Server is getting ready...')
while True:
	data, origin = obj_socket.recvfrom(65535)
	print('Origin: ',origin)
	print('Data received: ',data.decode())
	answer=input('Insert your answer: ')
	obj_socket.sendto(answer.encode(), origin)
obj_socket.close()