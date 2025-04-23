# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.
usuario_correto = 'fernando.simoes'
senha_correta = '@biru1718'
usuario = input('Informe o usuario:')
senha = input('Informe sua senha:')
if usuario == usuario_correto and senha == senha_correta:
    print('Bem Vindo Fernando')
else:
    print('Usuario ou senha invalido(s)')