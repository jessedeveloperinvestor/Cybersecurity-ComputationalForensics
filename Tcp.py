import socket
import sys
def main():
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	except socket.error as e:
		print('Conexion failed')
		print('Error: {}'.format(e))
		sys.exit()
	print('Socket was built successfuly')
	HostTarget=input('Type the host ip')
	PortTarget=input('Type the port to connect')
	try:
		s.connect((HostTarget, int(PortTarget)))
		print('TCP client connected successfuly at the host: ', HostTarget, '\nAnd at the port: ', PortTarget)
		s.shutdown(2)
	except socket.error as e:
		print('TCP client NOT connected successfuly at the host: ', HostTarget, '\nAnd at the port: ', PortTarget)
		print('Error: {}'.format(e))
		sys.exit()
if __name__ == '__main__':
	main()