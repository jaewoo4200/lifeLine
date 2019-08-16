from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8090))

print('Server Connected')
clientSock.send('화재가 감지되었습니다.'.encode('utf-8'))

