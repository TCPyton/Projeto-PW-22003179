def ler_numero():
    number = int(input("Introduza um número inteiro: "))
    return number
   

def imprime_resultados(n,positivo,par):
    if (positivo and par):
        print(f'Numero = {n}, é positivo, e é par')
    elif (not positivo and par):
         print(f'Numero = {n}, é negativo, e é par')
    elif (not positivo and not par):
         print(f'Numero = {n}, é negativo, e é impar')
    else:
         print(f'Numero = {n}, é positivo e é impar')