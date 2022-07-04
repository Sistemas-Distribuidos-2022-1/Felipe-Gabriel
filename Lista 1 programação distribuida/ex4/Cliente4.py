import socket

#definições
HOST= '127.0.0.1'
PORT= 15000

#conectando no servidor
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

#lê o sexo do cliente e envia para o servidor
print('Sexo: 1 masculino ou 2 feminino ')
sexo = input()
soc.sendall(str(sexo).encode('utf8'))

#lê o peso do cliente e envia para o servidor
print('peso:')
peso = input()
soc.sendall(str(peso).encode('utf8'))

##lê a altura do cliente e envia para o servidor
print('altura:')
altura = input()
soc.sendall(str(altura).encode('utf8'))

#recebe o resultado do peso ideal
ideal = soc.recv(1024)

#coloca na tela o resultado do processamento
print('Peso ideal:', ideal.decode())