import ipaddress
ip='192.168.0.1'
add=ipaddress.ip_address(ip)
net=ipaddress.ip_network(ip, strict=False)
for ip in net:
	print(add, net)