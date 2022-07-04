import socket

#definições
HOST= '127.0.0.1'
PORT= 15000

#conectando no servidor
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

#lê e envia a nota do aluno
print('Nota 1 : ')
nota1 = input()
soc.sendall(str(nota1).encode('utf8'))

#lê e envia a nota do aluno
print('Nota 2')
nota2 = input()
soc.sendall(str(nota2).encode('utf8'))

#lê e envia a nota do aluno
print('Nota 3')
nota3 = input()
soc.sendall(str(nota3).encode('utf8'))

#recebe o resultado do aluno
resultado = soc.recv(1024)

#mostra o resultado final do aluno
print('O aluno foi:', resultado.decode())