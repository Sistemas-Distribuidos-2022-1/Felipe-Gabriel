#--------------------------------------------------------------------------
import socket

#definições
HOST= '127.0.0.1'
PORT= 15000

#conectando no servidor
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

#--------------------------------------------------------------------------
print('Digite o saldo médio do cliente: ')
saldo_medio = input()
soc.sendall(str(saldo_medio).encode('utf8'))

#recebe a seleção da categoria
credito = soc.recv(1024)

print('O saldo médio do usuário é: ', saldo_medio)
print('O valor do crédito é: ', credito.decode())
#--------------------------------------------------------------------------
