import socket
port = 10500
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', port))
server.listen()

print(f"===  Servidor aguardando conexôes na porta {port} ===")
conn, addr = server.accept()
print(f'Conexão recebida de {addr}')

while True:
    ##recebe os dados enviados pelo cliente.
    data = conn.recv(4096)
    print(f'Cliente: {data.decode()}')

    
    msg = input(': ')
    conn.send(msg.encode())
    ##encerra a conexão


    conn.close
    
