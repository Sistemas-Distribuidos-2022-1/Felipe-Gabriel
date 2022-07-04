import socket

#definições
HOST= '127.0.0.1'
PORT= 15000

#conectando no servidor
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))


#lê a idade do nadador
print('Digite a idade do nadador: ')
idade = input()
soc.sendall(str(idade).encode('utf8'))


#recebe a seleção da categoria
categoria = soc.recv(1024)

print('Categoria:', categoria.decode())
