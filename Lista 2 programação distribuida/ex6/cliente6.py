import socket

HOST = 'LocalHost'
PORT = 1010

soq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soq.connect((HOST, PORT))

print("Nome: ")
nome = input()
soq.sendall((nome+'\n').encode())

print("Nivel: ")
nivel = input()
soq.sendall((nivel+'\n').encode())

print("Salario bruto: ")
salariobruto = input()
soq.sendall((salariobruto+'\n').encode())

print("Numero de dependentes: ")
dependentes = input()
soq.sendall((dependentes+'\n').encode())

resposta = soq.recv(1024).decode()
print(resposta)
