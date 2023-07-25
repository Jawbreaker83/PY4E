
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# returns an object and then the connect method is called in the object two things are passed in, (1) the host we wish to connect to, i.e. a domain name and (2) a port
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) <1):
		break
	print(data.decode())
mysock.close()