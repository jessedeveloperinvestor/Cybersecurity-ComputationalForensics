<<<<<<< HEAD
<<<<<<< HEAD
from socket import *
server='127.0.0.1'
port=43210
obj_socket=socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server,port))
exit=''
while exit!='X':
	msg=input('Insert a message: ')
	obj_socket.sendto(msg.encode(), (server,port))
	data, origin = obj_socket.recvfrom(65535)
	print("Server's answer: ",data.decode())
	exit=input("Type in 'X' to exit: ").upper()
obj_socket.close()
=======
=======
>>>>>>> origin/main
from socket import *
server='127.0.0.1'
port=43210
obj_socket=socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server,port))
exit=''
while exit!='X':
	msg=input('Insert a message: ')
	obj_socket.sendto(msg.encode(), (server,port))
	data, origin = obj_socket.recvfrom(65535)
	print("Server's answer: ",data.decode())
	exit=input("Type in 'X' to exit: ").upper()
obj_socket.close()
<<<<<<< HEAD
>>>>>>> origin/main
=======
>>>>>>> origin/main
