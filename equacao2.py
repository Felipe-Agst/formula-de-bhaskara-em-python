import math

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("O valor de delta é menor que 0. Não é possível calcular o delta de um número negativo.")
else:
    delta_sem_raiz = math.sqrt(delta)
    delta1 = (-b + delta_sem_raiz) / (2*a)
    delta2 = (-b - delta_sem_raiz) / (2*a)

    print("O valor de delta é:", delta)
    print("As raízes da equação são:", delta1, "e", delta2)
