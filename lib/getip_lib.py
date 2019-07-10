import socket

def getIP(domain):
  myaddr = socket.getaddrinfo(domain, 'http')
  print(myaddr[0][4][0])