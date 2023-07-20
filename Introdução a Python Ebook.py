

          # Operadores de Atribuição

from math import pi
from math import tau, e
print(pi)

exemplo = "Ada Lovelace"
print(type(exemplo))

exemplo = 10
[print(type(exemplo))]

exemplo = 10.20
print(type(exemplo))

exemplo = True
print(type(exemplo))

exemplo = True
print(exemplo)

print(pow(2,3))

x =2 
   #x recebe 2
x += 2
x = x + 2 

x -= 2
x = x - 2 

x *= 2
x = x * 2 

x/= 2
x = x / 2 

x%= 2
x = x % 2 

x**= 2
x = x ** 2 

x//= 2
x = x // 2    


              #OPERAÇÕES ARITMÉTICAS

# SOMA NÚMERO INTEIRO:

10+50

# SOMA NÚMERO FLUTUANTE (float)

10.5+1.5

# SUBTRAÇÃO

30-40
# MULTIPLICAÇÃO

2.4*10

# DIVISÃO

10/2

# EXPONENCIAÇÃO

2**3

# PRECEDÊNCIA DE OPERAÇÕES - PREFERÊNCIA MULTIPLICAÇÃO

2*8+6

# PRECEDÊNCIA DE OPERAÇÕES - PREFERÊNCIA SOMA

2*(8+6)

# PRECEDÊNCIA DE OPERAÇÕES - MULTIPLICAÇÃO E DIVISÃO NÃO SE SOBREPÕEM
# EXECUTA A QUE ESTÁ MAIS A ESQUERDA.

2*6/3

# PRECEDÊNCIA DE OPERAÇÕES - EXPOENTE
# TEM PREFERÊNCIA QUANDO COMPARADO A DIVISÃO OU MULTIPLICAÇÃO

2*2**3


# PARA EXECUTAR PRIMEIRO MULTIPLICAÇÃO

(2*2)**3

# DIVISÃO USANDO SOMENTE PARTE INTEIRA DO RESULTADO

5//2

# MÓDULO (RESTO DA DIVISÃO) - PODEMOS UTILIZAR PARA SEPARAR IMPAR//PAR

4%2

# MÓDULO (RESTO DA DIVISÃO)

3%2
             # ENTRADA DE DADOS E CONVERSÃO DE TIPOS

aluno = input("Digite seu nome: ")
periodoCorrente = int(input("Digite seu período corrente: "))
ira = float(input("Digite seu IRA(Índice de Rend. Acadêmico): "))
laurea = bool(input("Informe se você foi laureado(a) na turma: "))
print(type(aluno))
print(type(periodoCorrente))
print(type(ira))
print(type(laurea))



base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
area = base * altura
print(area)


    # Formatação de Strings


from datetime import datetime
anoAtual = datetime.now().year
clube = "Palmeiras"
anoNascimento = 1988
formacao = "Medicina Vetetinária"

print(f"{anoAtual - anoNascimento}" )
from math import pi
print(f"Valor de pi é: {pi:.20f}.")

altura = float(input("Digite sua altura em metros: "))
altura = altura * 100
print(f"Sua altura em centimetros é de: {altura}") 

deltaS = float(input("Digite o valor de Delta S: "))
deltaT = float(input("Digite o valor de Delta T: "))
vms = deltaS / deltaT
print("A velocidade média em metros por segundo é: ", vms)

from math import pi
raio = float(input("Digite o raio da circunferência: "))
areaCircunferencia = pi * pow(raio,2)
print("A área da circunferência é de: ", areaCircunferencia)

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
areaTriangulo = (base * altura)/2
print(areaTriangulo) 


    # Estruturas Condicionais (if, else e elif)



print("##Seja bem vindo ao programa de empréstimos do banco JOIA##. Responda: 0 - Não e 1 - Sim")
nomeNegativado = int(input("Possui nome negativado? "))
if nomeNegativado == 1:
    print("Infelizmente não podemos lhe conceder emprestimo")
else:
    carteiraAssinada = int(input("Possui carteira assinada? "))
if carteiraAssinada == 0:
     print("Infelizmente não podemos lhe conceder emprestimo")
else:
     casaPropria = int(input("Possui casa própria? "))
if casaPropria == 0:
     print("Infelizmente não podemos lhe conceder emprestimo")
else:
     print("Permitido iniciar o processo de emprestimo")

     



    # Operadores Lógicos

numero1 = int(input("Por favor digite um número qualquer: "))
numero2 = int(input("Por favor digite um número qualquer: "))
numero3 = int(input("Por favor digite um número qualquer: "))
if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    exit()
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é o maior")
if numero2 > numero1 and numero2 > numero3:
    print("O segundo número é o maior")
if numero3 > numero1 and numero3 > numero2:
    print(f"O terceiro número é o maior")

    

    # If e Else


# Teste de Par e Impar
valor = int(input("Digite um número qualquer: "))
if valor % 2 == 0:
    print("O valor é par")
else:
    print("O valor é impar")

    



# Descontos Loja seu Takanara

numeroCamisas = int(input("Quantidade de camisas: "))
valorCamisa = 10.00
valorFinal = numeroCamisas * valorCamisa
if numeroCamisas <= 5:
   valorFinal = valorFinal * (1 - 3/100)  
else:
     if numeroCamisas <= 10:
        valorFinal = valorFinal * (1 - 5/100)
     else:
        valorFinal = valorFinal * (1 - 7/100)
print(f"Valor final: R$ {valorFinal:.2f}")


        # Elif

print(f"{'*' * 18}  {'GRANDEZAS ELÉTRICAS'}  {'*' * 18}")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Intensidade (em Ampére)")
print("*" * 48)
op = int(input("Qual grandeza você deseja calcular? "))
if op < 1 or op > 3:
    print("Opção inválida")
elif op == 1:
    R = float(input("Digite o valor da resistência (em Ohm): "))
    i = float(input("Digite o valor da Intensidade (em Ampére): "))
    U = R * i 
    print(f"\nU = {U:.2f}")
elif op == 2:
    U = float(input("Digite o valor da tensão (em Volt): "))
    i = float(input("Digite o valor da Intensidade (em Ampére): "))
    R = U / i
    print(f"\nR = {R:.2f}")
else:
    U = float(input("Digite o valor da tensão (em Volt): "))
    R = float(input("Digite o valor da resistência (em Ohm): "))
    i = U / R
    print(f"\ni = {i:.2f}")



# calcular medida das lados e ver se o triângulo existe

from math import sqrt
x1 = float(input("Digite a cordenada de x do Ponto 1: "))
y1 = float(input("Digite a cordenada de y do Ponto 1: "))
x2 = float(input("Digite a cordenada de x do Ponto 2: "))
y2 = float(input("Digite a cordenada de y do Ponto 2: "))
x3 = float(input("Digite a cordenada de x do Ponto 3: "))
y3 = float(input("Digite a cordenada de y do Ponto 3: "))
l1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
l2 = sqrt((x3 - x1)**2 + (y3 - y1)**2)
l3 = sqrt((x3 - x2)**2 + (y3 - y2)**2)
cond1 = True
cond2 = True
cond3 = True
if l1 == 0 or l2 == 0 or l3 == 0:
    cond1 = False
if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    cond2 = False
if l1 <= abs(l2 - l3) or l2 <= abs(l1 - l3) or l3 <= abs(l1 - l2):
    cond3 = False
triangulo = True
if cond1 == False or cond2 == False or cond3 == False:
    triangulo = False
    print("\nNenhum triâgulo formado. \nMotivo(s): ")
    if cond1 == False:
        print("Pelo menos um dos lados é igual a zero.")
    if cond2 == False:
        print("Pelo menos um lado é maior que a soma dos outros dois lados.")
    if cond3 == False:
        print("Um dos lados é menor ou igual ao modulo da diferença")
elif l1 == l2 == l3:
    print("Triângulo equilátero.")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("Trinângulo escaleno.")
else:
    print("Triângulo isóceles.")
if triangulo:
    print(f"A medida do lado 1: {l1:.2f}")
    print(f"A medida do lado 2: {l2:.2f}")
    print(f"A medida do lado 3: {l3:.2f}")




altura1 = float(input("Digite a altura da primeira pessoa: "))
altura2 = float(input("Digite a altura da segundaa pessoa: "))
altura3 = float(input("Digite a altura da terceira pessoa: "))
maisAlto = altura1
mediano = altura1
maisBaixo = altura1
if altura1 > altura2 and altura1 > altura3:
    maisAlto = altura1
    if altura2 > altura3:
        mediano = altura2
        maisBaixo = altura3
    else: 
        mediano = altura3
        maisBaixo = altura2
elif altura2 > altura1 and altura2 > altura3:
    maisAlto = altura2
    if altura1 > altura3:
        mediano = altura1
        maisBaixo = altura3
else:
    maisAlto = altura3
    if altura1 > altura2:
        mediano = altura1
        maisBaixo = altura2
    else:
        mediano = altura2
        maisBaixo = altura1
print(f"\n O mais alto em metros tem: {maisAlto}, o mediano tem: {mediano} e o menor tem: {maisBaixo}")





        # Estruturas de repetição (while e for)

cont = 1
while cont <= 4000:
    print("Olá.")
    cont += 1
print("\nFim")




    #Estrutura While

soma = 0
termo = 1
while termo <= 10:
    soma = termo + soma
    termo = termo + 1
    print(soma, termo)
    print("\nFim.")

'''   1 termo = 1   soma = 0+1
2 termo = 2   soma = 0+1+2
3 termo = 3   soma = 0+1+2+3
4 termo = 4   soma = 0+1+2+3+4
5 termo = 5   soma = 0+1+2+3+4+5
6 termo = 6   soma = 0+1+2+3+4+5+6
7 termo = 7   soma = 0+1+2+3+4+5+6+7
8 termo = 8   soma = 0+1+2+3+4+5+6+7+8
9 termo = 9   soma = 0+1+2+3+4+5+6+7+8+9 
10 termo = 10 soma = 0+1+2+3+4+5+6+7+8+9+10

Soma = 55 
Último termo = 11 e que não entra na contagem. '''




            # Range

print((range(3)))

# Ou
               # Start, Stop, Step
print(list(range(0, 3, 1)))



            # For

for cont in range(101):
    print(cont)



soma = 0
for termo in range(11):
    soma += termo
    print(soma, termo)

soma = 0
for termo in range(1,11):
    soma += termo
print(soma, termo)


        # Comando Break

# Crie um programa no qual o usuário informe um número inteiro positivo N e armazene-o em uma variável. Em seguida, o usuário deve digitar N números. Ao fim, o programa deve im- primir a média aritmética dos N números digitados.


n = int(input("Digite a quantidade de números que deseja informar: "))
soma = 0 
for cont in range(n):
    num = float(input("Digite o número: "))
    soma += num
    media = soma/n
print(f"A media dos números informados é: {media:.2f}")

# Construir o programa a seguir, considere que os usuá- rios só informarão números inteiros positivos. Crie um progra- ma que receba 5 números digitados e, ao fim, exibir quantos números são pares.


pares = 0
for cont in range(5):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
print(pares)


# Construa um programa para fazer uma pequena entrevista com os alunos de uma turma. Na entrevista, são informados o sexo e a idade de cada aluno. Considere que o usuário não sabe quan- tos alunos existem na turma. O programa deve exibir a quantida- de de homens acima de 18 anos e a quantidade de mulheres de qualquer idade. Para encerrar o programa, o usuário deve infor- mar uma idade negativa.


homensAcima18 = 0
mulheres = 0
while True:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
       break
    sexo = input("Digite o sexo:")
    if sexo == "M" or sexo =="m":
       if idade >= 18: 
          homensAcima18 += 1
    elif mulheres:
         mulheres += 1

print(f"A quantidade de homens acima de 18 anos: {homensAcima18} e a quantidade total de mulheres: {mulheres}")




            # Listas

dados = ["Michae dos Santos Padilha", 0, 1.74, True]
print(f"Nome...............: {dados[0]} \nFilhos.............: {dados[1]} \nAltura.............: {dados [2]:.2f}m")
if dados [3] == True:
    print("Usa instagram......: Sim.")
else:
    print("Usa instagram......: Não.")

# Utilização do .append()
carro = []
carro.append("gol")
while True:
    nome = input("Digite o nome do carro: ")
    carro.append(nome)
    resp = input("Deseja continuar: [S|N]?: ")
    if resp == "N" or resp == "n":
        break
print(carro)


# Utilização do .insert(indice, elemento)

atrizes = ["Paolla de Oliveira"]
atrizes.append("Sheron Menezes")
atrizes.insert(1, "Raquel Nunes")
print(atrizes)



        #EMBARALHANDO E SORTEANDO ELEMENTOS

        
import random
nomes = ["michael", "joao", "claudia", "denise", "andre", "silvio"]
random.shuffle(nomes)
print(f"Lista embaralhada: {nomes}")
sorteada = random.choice(nomes)
print(f"O nome sorteado: {sorteada}")





        # ORDENANDO ELEMENTOS



import random 
atrizes = ["Adriana Prado", "Bárbara Borges", "Camila Queiroz",
"Danielle Winits", "Fernanda Paes Leme", "Helena Ranaldi",
"Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]
random.shuffle(atrizes)

 # Ordena elementos crescentemente
atrizes.sort() # mesmo que usar atrizes.sort(reverse = False)
print(atrizes)

# Ordena elementos decrescentemente
atrizes.sort(reverse = True)
print(atrizes)





         # REMOVENDO ELEMENTOS




# remove() e pop() e a função del.

# <lista>.remove(<elemento>) 
# <lista>.pop(<índice>)
# del <lista>[<índice>]


nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]
nomes.remove("claudia")
print(nomes)
print()

nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]
nomes.pop(4)
print(nomes)
print()

nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]
nomes.pop()
print(nomes)

print()

nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]
del nomes[4]
print(nomes)
print()

nomes.clear()   # Limpa a lista

del nomes   # deleta a lista toda   




        # CLONANDO E COMPARANDO LISTAS


# list()     copia = list()

# Ex:
nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]
copia = list(nomes)
print(nomes)
print(copia)    



# Vamos imaginar a situação em que desejamos remo- ver todos os elementos de uma lista, mas, antes disso, precisa- mos fazer um backup (cópia) dessa lista. Caso a cópia seja igual à original, a lista original poderá ser esvaziada; caso contrário, um erro deverá ser exibido.


nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]

backup = list(nomes)
if backup == nomes:
    nomes.clear()
    print("lista de atrizes esvaziada")
    print("Lista de backup: ", backup)
else:
    print("Erro: Cópia gerada não é igual a") 






          # INCLUINDO ELEMENTOS DE UMA LISTA EM OUTRA





# listaA.extend(listaB)

nomes = ["joao", "denise", "claudia", "mariana", "eduardo", "jean"]
nomesa = ["thiago", "otavio"]
nomes.extend(nomesa)
print(nomes)






#  OCORRÊNCIAS DE ELEMENTOS E  COMPRIMENTO DA LISTA


#  número de ocorrências (repetições de determinado elemento):     lista.count(elemento)


nomes = ["joao", "denise", "claudia", "claudia", "eduardo", "jean"]
ocorrencia = nomes.count("claudia")
print(f"O elemento Claudia se repete {ocorrencia} vezes.")



# comprimento da lista (conta o número de elementos): len(lista)

nomes = ["joao", "denise", "claudia", "claudia", "eduardo", "jean"]
print(f"A lista possui {len(nomes)} elementos")    




            # MENOR, MAIOR E SOMA DE ELEMENTOS


#  min(lista) : menor elemento da lista
#  max(lista) : maior elemento da lista
#  sum(lista) : soma dos elementos da lista


NotasTurma = [10, 10, 5, 6, 9, 110, 30]
sum(NotasTurma)
min(NotasTurma)
max(NotasTurma)
media = sum(NotasTurma) / len(NotasTurma)
print(f"A maior nota é:  {max(NotasTurma)} a menor nota da turma é: {min(NotasTurma)} e a media das notas é: {media}")





            # RETORNANDO O ÍNDICE DE UM ELEMENTO

# index() é usado para mostrar a primeira posição da ocorrencia (aparição) de um elemento não monstrando as repetições seguintes 
# lista.index(elemento)

nomes = ["joao", "denise", "claudia", "claudia", "eduardo", "jean"]

procurarPor = input("Digite o nome que deseja procurar: ")
if procurarPor in nomes:
    indice = nomes.index(procurarPor)
    print(f" O nome: {procurarPor} está no índice {indice}.")
else:
    print(f" o nome: {procurarPor} não está na lista.")



#

atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda"]
for nome in atrizes: print(nome)        

                                                                



            # RETORNANDO ÍNDICE E ELEMENTO



# for índice, elemento enumerate(lista)


nomes = ["joao", "denise", "claudia", "claudia", "eduardo", "jean"]
for indice, nome in enumerate(nomes):
    print(f"{nome} está armazenado no índice: {indice}")
