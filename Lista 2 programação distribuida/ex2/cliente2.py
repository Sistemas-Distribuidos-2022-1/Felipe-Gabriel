#--------------------------------------------------------------------------
import socket

#define as portas para conexão
HOST = 'LocalHost'
PORT = 15000

soq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soq.connect((HOST, PORT))

#--------------------------------------------------------------------------
#Lê os dados da pessoa e envia para o servidor
print("Digite o Nome: ")
nome = input()
soq.sendall((nome+'\n').encode())

print("Digite o Sexo: ")
sexo = input()
soq.sendall((sexo+'\n').encode())

print("Digite a Idade: ")
idade = input()
soq.sendall((idade+'\n').encode())

#--------------------------------------------------------------------------
#recebe a resposta do servidor e printa na tela
resposta = soq.recv(1024).decode()
print(resposta)
#--------------------------------------------------------------------------
