import os
host_ip=input('Type the IP of the Host')
os.system('ping -n 6 {}'.format(host_ip))