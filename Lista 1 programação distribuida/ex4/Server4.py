import socket

#definições
HOST= 'localhost'
PORT= 15000

#abrindo as portas
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))

#aguardando conexão do cliente
soc.listen()
print('Aguardando conexão de um cliente')
conection, ender = soc.accept()

print('Conectado em', ender)

#recebe os parametros
while True:
    sexo = int(conection.recv(1024))
    print(sexo)

    peso = int(conection.recv(1024))
    print(peso)    

    altura = int(conection.recv(1024))
    print(altura)

   #faz o cálculo do peso ideal
    if sexo == 1:
        ideal = (72,7 * altura) - 58
    elif sexo == 2:
        ideal = (62,1 * altura) - 44,7
   
    #tentativa de condicional para finalizar a operação em caso de falha
    if not sexo:
        print('Fechando a conexão')
        conection.close()
        break

    elif not peso:
        print('Fechando a conexão')
        conection.close()
        break

    elif not altura:
        print('Fechando a conexão')
        conection.close()
        break
    
    #envia o salario novo para o cliente
    conection.sendall(str.encode(ideal))