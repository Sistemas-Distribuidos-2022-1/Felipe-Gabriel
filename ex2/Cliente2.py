import socket

#definições
HOST= '127.0.0.1'
PORT= 15000

#conectando no servidor
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

#lendo e enviando o nome para o servidor
print('Nome: ')
nome = input()
soc.sendall(str.encode(nome))

#lendo e enviando o sexo para o servidor
print('Sexo: masculino = 1 ou feminino = 2 ')
sexo = input()
soc.sendall(str(sexo).encode('utf8'))

#lendo e enviando a idade para o servidor
print('Idade :')
idade = input()
soc.sendall(str(idade).encode('utf8'))


#recebe do servidor o resultado do processamento
maior = soc.recv(1024)

#envia a mensagem de confirmação
print('Verificação:', maior.decode())