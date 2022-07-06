import socket

HOST = 'LocalHost'
PORT = 7890

soq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soq.connect((HOST, PORT))

print("Idade: ")
idade = input()
soq.sendall((idade+'\n').encode())

resposta = soq.recv(1024).decode()
print(resposta)
