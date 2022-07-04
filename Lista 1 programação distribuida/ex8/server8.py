#--------------------------------------------------------------------------
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

#--------------------------------------------------------------------------
#recebe os parametros
while True:
    saldo_medio = int(conection.recv(32))
    print(saldo_medio)

    #tentativa de condicional para finalização da operação em caso de falha
    if not saldo_medio:
        print('Fechando conexão')
        conection.close()
        break

#seleciona se pode aposentar ou não
    if saldo_medio >= 0 and saldo_medio <= 200 :
        CREDITO = ('zero, pois sem crédito disponível')
        conection.sendall(str(CREDITO).encode('utf8'))

    if saldo_medio >= 201 and saldo_medio <= 400 :
        saldo_medio = saldo_medio * (20/100)
        conection.sendall(str(saldo_medio).encode('utf8'))

    if saldo_medio >= 401 and saldo_medio<= 600 :
        saldo_medio = saldo_medio * (30/100)
        conection.sendall(str(saldo_medio).encode('utf8'))

    if saldo_medio >= 601 :
        saldo_medio = saldo_medio * (40/100)
        conection.sendall(str(saldo_medio).encode('utf8'))
#--------------------------------------------------------------------------
