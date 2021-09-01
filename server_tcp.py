from socket import *
server='127.0.0.1'
port=43210
obj_socket=socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server,port))
obj_socket.listen(2)
print("Waiting for customer's reponse...")
while True:
	con, customer=obj_socket.accept()
	print('Connected with: '+customer)
	while True:
		msg_got=str(con.recv(1024))
		print('Received: '+msg_got)
		msg_sent=b'Hello customer'
		con.send(msg_sent)
		break
	con.close()