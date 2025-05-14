# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
try:
    info = input("Digite a informação a se repetir: ").strip()
    mult = int(input("Digite a quantidade de vezes a repetir a informação: "))
    resultado = (info + ' ') * mult
    print(resultado.rstrip())
except ValueError:
    print("Erro: Digite um número válido para a repetição.")