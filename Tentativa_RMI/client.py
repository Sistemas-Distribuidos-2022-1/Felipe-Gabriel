import Pyro4

nome = input("Digite seu nome: ").strip()
sexo = input("Digite seu sexo(masculino ou feminino): ").strip()
idade = input("Digite sua idade: ").strip()


funcaoremota = Pyro4.Proxy("PYRONAME:funcaoremota")
print(funcaoremota.maioridade(sexo,idade))
