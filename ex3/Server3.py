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
    nota1 = int(conection.recv(1024))
    print(nota1)

    nota2 = int(conection.recv(1024))
    print(nota2)    

    nota3 = int(conection.recv(1024))
    print(nota3)

    #calculo da media
    media = (nota1 + nota2) / 2

    media = (media + nota3) / 2
   
    resultado = ' reprovado'

    if media >= 7:
        resultado = 'aprovado'      
    elif media>= 3 and media <= 7 :
        if media >= 5 :
            resultado = 'aprovado'
   

    if not nota1:
        print('Fechando a conexão')
        conection.close()
        break

    elif not nota2:
        print('Fechando a conexão')
        conection.close()
        break

    elif not nota3:
        print('Fechando a conexão')
        conection.close()
        break
    
    #retorna o resultado do aluno pro cliente
    conection.sendall(str.encode(resultado))