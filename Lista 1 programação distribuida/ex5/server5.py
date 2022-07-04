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
    IDADE = int(conection.recv(32))
    print(IDADE)

    #tentativa de condicional para finalização da operação em caso de falha
    if not IDADE:
        print('Fechando conexão')
        conection.close()
        break

#seleciona categorias
    if IDADE >=5 :
        if IDADE <= 7 :
            IDADE = 'Infantil A'
            #envia o salario novo para o cliente
            conection.sendall(str(IDADE).encode('utf8'))

    if IDADE >= 8 :
        if IDADE <=10 :
            IDADE = 'Infantil B'
            #envia o salario novo para o cliente
            conection.sendall(str(IDADE).encode('utf8'))

    if IDADE >= 11 :
        if IDADE <= 13 :
            IDADE = 'Juvenil A'
            #envia o salario novo para o cliente
            conection.sendall(str(IDADE).encode('utf8'))

    if IDADE >= 14 :
        if IDADE <= 17 :
            IDADE = 'Juvenil B'
            #envia o salario novo para o cliente
            conection.sendall(str(IDADE).encode('utf8'))

    if IDADE >= 18 :
        IDADE = 'Adulto '
        #envia o salario novo para o cliente
        conection.sendall(str(IDADE).encode('utf8'))
        conection.close()
