import socket

#definições
HOST='localhost'
PORT= 15000

#abrindo as portas
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))

#aguardando conexão do cliente
soc.listen()
print('Conecte um cliente')
conection, ender = soc.accept()

print('Conectado em', ender)

#recebe os parametros
while True:
    nome = conection.recv(1024)
    print(nome)

    cargo = int(conection.recv(32))
    print(cargo)    

    salario = int(conection.recv(1024))
    print(salario)

    #tentativa de condicional para finalização da operação em caso de falha
    if not nome:
        print('Fechando conexão')
        conection.close()
        break

#calcula os novos salários
    if cargo == 1:
        novoSalario = salario * (120/100)
        
    elif cargo == 2:
        novoSalario = salario * (118/100)
        
    #envia o salario novo para o cliente 
    conection.sendall(str(novoSalario).encode('utf8'))

