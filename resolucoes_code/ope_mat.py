# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
def calcular(num1, ope, num2):
    operacoes = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': "Erro! Divisão por zero!" if num2 == 0 else num1 / num2
    }
    return operacoes.get(ope, "Operação inválida!")

try:
    num1 = int(input("Digite o primeiro número: "))
    ope = input("Digite a operação (+, -, *, /): ")
    num2 = int(input("Digite o segundo número: "))

    resultado = calcular(num1, ope, num2)
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")