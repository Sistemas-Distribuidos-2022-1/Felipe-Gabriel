import zmq, time, random, names

context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = "tcp://*:5555" # how and where to communicate
s.bind(p) # bind socket to the address

while True:
	idade = str(random.randint(0,100))
	salario = str(random.randint(1200, 10000))
	nome = names.get_first_name()
	option = random.randint(1,2)
	option2 = random.randint(1,2)
	if(option == 1):
		cargo = 'operador'
	else:
		cargo = 'programador'
	
	if(option2 == 1):
		sexo = 'masculino'
	else:
		sexo = 'feminino'
	time.sleep(3) # wait 
	s.send_string(' '.join(['REAJUSTE', nome, salario, cargo]))
		
	s.send_string(' '.join(['MAIORIDADE', nome, idade, sexo]))
