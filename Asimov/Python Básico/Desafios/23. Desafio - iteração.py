# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

valores = [10, 30, -8, 0, -2, 4]
soma = 0 
for valor in valores:
    soma += valor
    
media = soma / len(valores)
#print(sum(valores))

print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media}')

maximo = valores[0]
for valor in valores:
    if valor > maximo:
        maximo = valor
print(f"O Valor máximo é: {maximo}")
#print(max(valores))

palavras = ['oi', 'Python', 'x', 'y']
for palavra in palavras:
    if len(palavra)>=5:
        print(f'Palavra(s) += 5 caracteres na lista de palavras: \n{palavra}')

