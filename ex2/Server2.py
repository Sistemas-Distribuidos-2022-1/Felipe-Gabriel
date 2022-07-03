import socket

#definições
HOST= 'localhost'
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

    sexo = int(conection.recv(32))
    print(sexo)    

    idade = int(conection.recv(1024))
    print(idade)

    # Assume que o cidadão é menor de idade, caso entre nas seleções quer 
    # dizer que ele é maior de idade
    maior = 'Menor de idade'

    if idade >= 18 :
        if sexo == 1:
            maior = 'Maior de idade'

        
    if idade >= 21 :
        if sexo == 2:    
            maior = 'Maior de idade'
    
    
        
    # Tentativa de fechar o soc em caso de falha
    if not nome:
        print('Fechando a conexão')
        conection.close()
        break

    # envia o resultado final para o cliente
    conection.sendall(str(maior).encode('utf8'))