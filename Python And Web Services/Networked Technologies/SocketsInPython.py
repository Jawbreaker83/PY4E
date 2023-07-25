#Python has built-in support for TCP Sockets; the equivalent of dialing the phone only to make a connection;

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# returns an object and then the connect method is called in the object two things are passed in, (1) the host we wish to connect to, i.e. a domain name and (2) a port
mysock.connect(('data.pr4e.org', 80))