#Vamos testar se uma palavra é um palíndromo?! 
#Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def verify_palindrome(frase):
    frase = frase.replace(" ", "").lower()
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        return True
    else:
        return False

entrada = input("Digite uma palavra ou frase: ")

if verify_palindrome(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")