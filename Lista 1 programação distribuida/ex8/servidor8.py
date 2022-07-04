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

while True:

    #recebe os parametros    
    saldo_medio = (conection.recv(1024))
    

    #verificação de falha
    if not saldo_medio:
        print('Fechando conexão')
        conection.close()
        break

    #decodifica saldo medio
    saldo_medio = int(saldo_medio.decode())
    print(saldo_medio)

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
