#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
#Uma dica é: Utilize condicionais para realizar a verificação e, se possível, 
#faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

def verifica_numero(num):
    return "ímpar" if num % 2 else "par"

num = int(input("Digite o número: "))
print(f"Seu número é: {verifica_numero(num)}")

