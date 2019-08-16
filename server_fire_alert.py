from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8090))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print('From', str(addr), 'client connected.')

data = connectionSock.recv(1024)
print(data.decode('utf-8'))
