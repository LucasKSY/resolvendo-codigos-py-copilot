#calcular a média de três notas fornecidas na entrada do usuário. 
#Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

def calcular_media(*notas):
    return round(sum(notas) / len(notas), 2)

notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(3)]

print(f"A média das notas é: {calcular_media(*notas)}")