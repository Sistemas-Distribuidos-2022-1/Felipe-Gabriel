#--------------------------------------------------------------------------
import socket

#definições
HOST = 'LocalHost'
PORT = 15000

soq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soq.connect((HOST, PORT))

#--------------------------------------------------------------------------

#Lê e envia os dados do funcionário
print(" Nome do Funcionario: ")
nome = input()
soq.sendall((nome+'\n').encode())

print("Cargo do Funcionario: ")
cargo = input()
soq.sendall((cargo+'\n').encode())

print("Salario do Funcionario: ")
salario = input()
soq.sendall((salario+'\n').encode())

#recebe a resposta do servidor e a printa no terminal
resposta = soq.recv(1024).decode()
print(resposta)
#--------------------------------------------------------------------------