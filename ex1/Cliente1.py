import socket

#definições
HOST= '127.0.0.1'
PORT= 15000

#conectando no servidor
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

#lê e envia o nome do funcionário para o servidor
print('Nome do funcionário: ')
nome = input()
soc.sendall(str.encode(nome))

#lê e envia o cargo do fundionário para o servidor
print('Cargo : operador = 1 e programador = 2 ')
cargo = input()
soc.sendall(str(cargo).encode('utf8'))

#lê e envia o salario lido para o servidor
print('Salário :')
salario = input()
soc.sendall(str(salario).encode('utf8'))

#recebe o valor do novo salário do servidor
novoSalario = soc.recv(1024)

print('Novo Salário:', novoSalario.decode())