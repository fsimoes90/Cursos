from pathlib import Path

pasta_atual = Path(__file__).parent

# ##### lendo um arquivo forma não recomendada #####
# lista_compras = open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8')
# print(lista_compras.read())
# lista_compras.close()

# ##### lendo um arquivo forma recomendada #####
# with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
#     print(lista_compras.read())

# ##### lendo linha a linha #####
# with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
#     linha = lista_compras.readline()
#     while linha != '':
#         print(linha, end='')
#         linha = lista_compras.readline()
#     print(linha)

# ##### lendo todas as linhas #####
# with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
#     print(lista_compras.readlines())

# ##### Escrevendo arquivo #####
# itens_comprados = ['farinha', 'fermento', 'água']
# with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
#     itens_lista = lista_compras.readlines()

# with open(pasta_atual / 'lista_de_compras_atualizada.txt', encoding='utf-8', mode='w') as lista_atualizada:
#     for item in itens_lista:
#         if item.replace('\n', '') in itens_comprados:
#             lista_atualizada.write(item)
# print(itens_lista)

# ##### Escrevendo arquivo linha a linha #####
# itens_comprados = ['farinha', 'fermento', 'água']
# with open(pasta_atual / 'lista_de_compras.txt', encoding='utf-8') as lista_compras:
#     itens_lista = lista_compras.readlines()

#     itens_lista_atualizada = []
#     for item in itens_lista:
#         if not item.replace('\n', '') in itens_comprados:
#             itens_lista_atualizada.append(item)

# with open('lista_de_compras_atualizada.txt', encoding='utf-8', mode='w') as lista_atualizada:
#     itens_lista_atualizada[-1] = itens_lista_atualizada[-1].replace('\n','')
#     lista_atualizada.writelines(itens_lista_atualizada)
# print(itens_lista_atualizada)

##### Acrescentando valores a um arquivo #####
novos_itens = ['banana']
novos_itens_c_quebra = []
for item in novos_itens:
    novos_itens_c_quebra.append(f'\n{item}')
with open('lista_de_compras_atualizada.txt', encoding='utf-8', mode='a') as lista_adicionada:
    lista_adicionada.writelines(novos_itens)
