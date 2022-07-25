import zmq

context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = "tcp://192.168.40.47:5555"  # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "REAJUSTE") # subscribe to TIME messages

for i in range(10): # Five iterations
	reajuste = s.recv().split() # receive a message
	salario = int(reajuste[2])

	if (reajuste[3] == 'operador'):
		salario *= 1.2
	else:
		salario *= 1.18

	print(f'Nome: {reajuste[1]}\n Salario: {salario}\n Cargo: {reajuste[3]}\n')
