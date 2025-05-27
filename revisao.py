# 1. Declare 3 variáveis representando nome, idade e nota de um aluno. Depois, exiba esses dados com print.

nomeAluno = "Avelino"
idadeAluno = 16
notaAluno = 10.0

print(f"Nome: {nomeAluno}, Idade: {idadeAluno}, Nota: {notaAluno}")

# 2. Crie expressões utilizando operadores aritméticos e relacionais.

x = 100
x += 1
print(x)

# 3. Peça uma nota e diga se o aluno foi aprovado (nota ≥ 6).
# nota = input("Nota(1 a 10): ")
# if nota >= "6.0":
#     print(f"Aprovado! ({nota})")
# else:
#     print(f"Reprovado! ({nota})")



# 4. Imprima os números de 1 a 10 usando um laço for.

for i in range(-1, 10):
    i += 1
    print(i)

# 5. Crie uma função que receba dois números e retorne a soma.

numb1 = int(input('Qual o primeiro  numero : '))
numb2 = int(input('Qual o segundo numero : '))

try:
    resultado   = numb1 + numb2
    print(resultado)
except:
    print('á algo errado')


# 6. Peça ao usuário seu nome e idade e exiba em uma frase formatada.

Nome_usuario = str(input('Qual seu nome ?'))
print(f' Bem vindo ao céu sr.(a) {Nome_usuario}')



# 7. Crie uma lista com 5 frutas e imprima a segunda e a última fruta.

frutas = ["maça", "laranja", "uva", "pera", "melancia"]
print()

# 8. Crie uma matriz 3x3 com números de 1 a 9 e imprima todos os elementos da diagonal principal.

matriz = {1, 2, 3,
          4, 5, 6,
          7, 8, 9}

# 9. Peça um número ao usuário e use try/except para impedir erro caso ele digite texto.

try:
     Numeros = float(input('Digite  um numero : '))
     print()

except ValueError:
    print('algo deuy errado tente novamente') 

# 10. Peça para o usuário inserir uma frase e a modifique com pelo menos 3 métodos de string

frase = input("Escreva uma Frase: ")
print(frase.lower)
print(frase.upper)
print(frase.strip)

# 11. Use um while para pedir um número maior que zero. Se o número for negativo, use continue para pedir de novo.

i = 0
while i < 0:
    if i <= -1:
        i += 1
        continue
    print(i)
    i += 1

# 12. Crie um código com dois for que imprimam a tabuada de 1 a 5.

for a in range(6):
    for b in range(11):
        total = a * b
        print(f'{a} * {b} = {total}')

# 13. Use range para imprimir os múltiplos de 3 entre 0 e 30.

for i in range(1, 11):
    i *= 3
    print(i)

# 14. Crie uma tupla com os dias da semana e mostre a terça-feira.

tupla = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")
print(tupla[1])

# 15. Peça uma idade e use uma operação ternária para dizer se é maior de idade.

# idadeUser2 = input("Idade:")
# ok = "Ok!" if idadeUser2 >= 18 else "Não."
# print(ok)

# 16. Crie uma função com dois parâmetros: nome e curso. Ela deve imprimir uma saudação.

nome = str(input(' Qual o nome do usuario ? '))
curso = str(input('Qual o curso você faz ? '))
print(f'BEM VINDO SR.(A) {nome} e seu curso é {curso}')



# 17. Altere a função anterior para que, ao invés de print, ela retorne a saudação.

nome = str(input(' Qual o nome do usuario ? '))
curso = str(input('Qual o curso você faz ? '))
(f'BEM VINDO SR.(A) {nome} e seu curso é {curso}')
# 18. Crie um programa que cadastre nome, idade e curso de um aluno em um dicionário. A chave será o nome do aluno, o valor será outro dicionário com idadae e nota final. Exiba nome, idade e nota de cada aluno