#clientes_Tupla = [
#    ('Fernando',1234,'xxx@gmail.com'),
#    ('Eric',4321,'yyy@mgil.com')
#]
#for cliente in clientes_Tupla:
#    nome = cliente[0]
#    cpf = cliente[1]
#    email = cliente[2]
#    print(f'Nome: {nome}\nCPF: {cpf}\nE-mail: {email}\n')
#print('Lista finalizada')

clientes_chave = [
    {'nome': 'Fernando', 'cpf': 123, 'email': "xxx@gmail.com"},
    {'nome': 'Eric', 'cpf': 123, 'email': "yyy@gmail.com"}
]
for cliente in clientes_chave:
    nome = cliente['nome']
    cpf = cliente['cpf']
    email = cliente['email']
    print(f'Nome: {nome}\nCPF: {cpf}\nE-mail: {email}\n')
print('Lista finalizada')