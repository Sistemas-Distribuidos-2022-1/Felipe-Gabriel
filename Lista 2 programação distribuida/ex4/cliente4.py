import socket

HOST = 'LocalHost'
PORT = 15000

soq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soq.connect((HOST, PORT))

print("Altura: ")
altura = input()
soq.sendall((altura+'\n').encode())

print("Sexo: ")
sexo = input()
soq.sendall((sexo+'\n').encode())

resposta = soq.recv(1024).decode()
print(resposta)
