
import math 
# #### Inteiros (`int`)
print("\nExercício 1:\n")
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
soma = num1 + num2
print(f"Exercicio 1: {soma}")

print("\nExercício 2:\n")
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um numero: "))
resto = num%5
print(f"Exercício 2: {resto}")

print("\nExercício 3:\n")
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
mult = numero1 * numero2
print(f"Exercicio 3: {mult}")

print("\nExercício 4:\n")
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
nmr1 = int(input("Digite um numero: "))
nmr2 = int(input("Digite outro numero: "))
div = nmr1 // nmr2
print(f"Exercicio 4: {div}")

print("\nExercício 5:\n")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um numero: "))
quadrado = numero**2
print(f"Exercício 5: {quadrado}")

# #### Números de Ponto Flutuante (`float`)

print("\nExercício 6:\n")
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
float1 = float(input("Digite um numero decimal: "))
float2 = float(input("Digite outro: "))
somaFloat = float1+float2
print(f"Exercício 6: {somaFloat}")

print("\nExercício 7:\n")
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
float3 = float(input("Digite um numero decimal: "))
float4 = float(input("Digite outro: "))
meanFloat = (float3+float4) / 2
print(f"Exercício 7: A média é {meanFloat}")

print("\nExercício 8:\n")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base**expoente
print(f"Exercício 8: {potencia}")

print("\nExercício 9:\n")
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em celsius: "))
fahrenheit = 1.8 * celsius + 32
print(f"Exercicio 9: a temperatura em fahrenheit é {fahrenheit}°F")

print("\nExercício 10:\n")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
areaCirculo = math.pi * raio**2
print(f"Exercicio 10: {areaCirculo:.2f}")

# #### Strings (`str`)

print("\nExercício 11:\n")
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
str = input("Digite uma palavra: ").upper()
print(str)

print("\nExercício 12:\n")
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ").upper()
print(nome)

print("\nExercício 13:\n")
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
str1 = input("Digite uma frase: ").strip()
print(str1)

print("\nExercício 14:\n")
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
mes = data.split("/")[0]
dia = data.split("/")[1]
ano = data.split("/")[2]

print(dia)
print(mes)
print(ano)

print("\nExercício 15:\n")
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str3 = input("String 1: ")
str4 = input("String 2: ")
concat = str3 + str4
print(concat)

# #### Booleanos (`bool`)

print("\nExercício 16:\n")
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool1 = bool(input("True or false: "))
bool2 = bool(input("True or false: "))
result = bool1 and bool2
print(result)

print("\nExercício 17:\n")
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
bool3 = bool(input("True or false: "))
bool4 = bool(input("True or false: "))
result1 = bool1 or bool2
print(result1)

print("\nExercício 18:\n")
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
bool5 = bool(input("True or false: "))
print(not bool5)

print("\nExercício 19:\n")
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
val1 = int(input("Valor 1: "))
val2 = int(input("Valor 2: "))
if val1==val2:
    print("Valores são iguias.")
else:
    print("Valores diferentes.")

print("\nExercício 20:\n")
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
val3 = int(input("Valor 1: "))
val4 = int(input("Valor 2: "))
if val3!=val4:
    print("Valores são diferentes.")
else:
    print("Valores iguias.")

# #### try-except e if

print("\nExercício 21:\n")
# 21: Conversor de Temperatura
try:
    try1 = int(input("Digite os graus em celsius: "))
    fahr = 1.8 * try1 + 32
    print(fahr)
except:
    print("Wrong type")

print("\nExercício 22:\n")
# 22: Verificador de Palíndromo
word = input("Type a word: ")
if isinstance(word, str):
    word = word.replace(" ","").lower()
    wordInvert = word[::-1]
    if wordInvert == word:
        print("palindromo")
    else:
        print("nao palindromo")
else:
    print("A variável não é uma string.")

print("\nExercício 23:\n")
# 23: Calculadora Simples
try:
    calc1 = int(input("Escolha o primeiro número: "))
    calc2 = int(input("Digite o segundo numero: "))
    oper = input("Escolha um operador matemática, entre: /, -, +, *: ")
    if oper=='/':
        resultado = calc1/calc2
    elif oper=='+':
        resultado = calc2+calc1
    elif oper=='-':
        resultado = calc2-calc1
    elif oper=='*':
        resultado = calc1*calc2
    else:
        print("Operador invalido ou divisão por zero.")
    print("Resultado: ", resultado)
except ValueError:
    print("Wrong type!")

print("\nExercício 24:\n")
# 24: Classificador de Números
try:
    classNum = int(input("Digite um número: "))
    if classNum >= 0:
        print("Número positivo.")
    else:
        print("Número negativo")
    if classNum%2==0:
        print("Número par")
    else:
        print("Número ímpar")
except ValueError:
    print("Wrong type!")

print("\nExercício 25:\n")
# 25: Conversão de Tipo com Validação
try:
    numbers = []
    n = input("Enter a list of numbers split by a comma: ").split(",")
    for i in n:
        numbers.append(int(i))
    print(numbers)
except ValueError as e:
    print(f"Error: {e}. Please enter only integers separated by commas.")