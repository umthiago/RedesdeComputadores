

import socket

port = 10500
dest = 'localhost'
##msg = 'Busquem conhecimento. Atte Et Bilu.'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== Conectando ao servidor {dest} : {port} ===')
client.connect((dest,port))

##cria um input pro cliente mandar mensagem pro servidor
while True:
    msg = input(': ')
    client.send(msg.encode())

    msg = client.recv(4096)
    print(f'Servidor: {msg.decode()}')

    
    client.close
