from pathlib import Path

item_remover = 'Passear com cachorro'

pasta_atual = Path(__file__).parent

with open(pasta_atual / 'view_lista.html') as html:
    linhas_html = html.readlines()

nova_linha_html = []
escrever_linha = True
for i, linha in enumerate(linhas_html):

    if i < len(linhas_html) -3 and item_remover in linhas_html[i + 2]:
        escrever_linha = False

    if escrever_linha:
        nova_linha_html. append(linha)
    print(i, linha)



with open(pasta_atual / 'view_lista_atualizada.html', mode='w') as html:
    html.writelines(nova_linha_html)