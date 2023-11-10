def vogal(caractere):
    # Converte o caractere para minúscula para fazer a verificação
    caractere = caractere.lower()
    
    # Verifica se o caractere é uma vogal
    if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
        return True
    else:
        return False

# Exemplos de execução
print(vogal("a"))  # Saída: True
print(vogal("b"))  # Saída: False
print(vogal("E"))  # Saída: True
