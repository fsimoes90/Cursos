chave = {
    'Fernando': 'FAS',
    'Eric': 'WEAR'
}

for name in chave:
    abre = chave[name]
    print(f'Abreviação do nome {name} é: {chave[name]}')
    
imprime_chave = chave['Fernando']
imprime_chave_get = chave.get('Fernando', 'não existe')
imprime_chave_get_naoexiste = chave.get('Stefane', 'não existe')
print("\n", imprime_chave_get_naoexiste)

for nome in chave.keys():
    print("\n", nome)
for abre in chave.values():
    print("\n", abre)
for k,v in chave.items():
    print(f"\n {k} -> {v}")
    #print(f"\n", k,v)
    
copia = chave.copy()