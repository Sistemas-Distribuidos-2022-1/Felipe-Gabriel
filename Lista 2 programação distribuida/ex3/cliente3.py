import socket

HOST = 'LocalHost'
PORT = 15000

soq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soq.connect((HOST, PORT))

#Lê e envia as notas dos alunos
print("Digite a Nota 1: ")
nota1 = input()
soq.sendall((nota1+'\n').encode())

print("Digite a Nota 2: ")
nota2 = input()
soq.sendall((nota2+'\n').encode())

print("Digite a Nota 3: ")
nota3 = input()
soq.sendall((nota3+'\n').encode())

resposta = soq.recv(1024).decode()
print(resposta)
