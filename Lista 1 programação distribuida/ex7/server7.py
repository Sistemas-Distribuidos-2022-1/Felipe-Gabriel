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

    TEMPO_DE_TRAB = int(conection.recv(32))
    print(TEMPO_DE_TRAB)

    #tentativa de condicional para finalização da operação em caso de falha
    if not IDADE:
        print('Fechando conexão')
        conection.close()
        break

    if not TEMPO_DE_TRAB:
        print('Fechando conexão')
        conection.close()
        break

#seleciona se pode aposentar ou não
    if IDADE >=65 and TEMPO_DE_TRAB >= 30 :
        APOSENTAR = ('Pode aposentar. ')
        conection.sendall(str(APOSENTAR).encode('utf8'))

    if IDADE >= 60 and TEMPO_DE_TRAB >= 25 :
        APOSENTAR = ('Pode aposentar. ')
        conection.sendall(str(APOSENTAR).encode('utf8'))

    if IDADE < 60 or TEMPO_DE_TRAB < 25:
        APOSENTAR = ('Não pode se aposentar')
        conection.sendall(str(APOSENTAR).encode('utf8'))

    if IDADE >=60 and TEMPO_DE_TRAB < 25 :
        APOSENTAR = ('Pode aposentar. ')
        conection.sendall(str(APOSENTAR).encode('utf8'))

    if IDADE >=65 and TEMPO_DE_TRAB < 30 :
        APOSENTAR = ('Pode aposentar. ')
        conection.sendall(str(APOSENTAR).encode('utf8'))
