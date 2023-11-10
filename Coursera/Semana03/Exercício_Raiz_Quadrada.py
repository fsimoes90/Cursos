import math

# Receber os parâmetros a, b e c da equação
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcular o discriminante (delta)
delta = b**2 - 4*a*c

# Verificar as condições e imprimir os resultados
if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"a raiz desta equação é {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    if raiz1 < raiz2:
        print(f"as raízes da equação são {raiz1} e {raiz2}")
    else:
        print(f"as raízes da equação são {raiz2} e {raiz1}")
