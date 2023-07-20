'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {0} e {1} é: {2}'.format(n1, n2, s))'''


            # DESAFIOS                                  

# Desafio 1 e 2 era introdução do programa print("Hello, World")


# DESAFIO 03.       Crie um programa que receba dois números, realize a soma entre eles e mostre o resultado e a soma.


'''numero_1 = int(input('Digite o primeiro número que você deseja somar: '))
numero_2 = int(input('Digite o segundo número da soma: '))
soma = numero_1 + numero_2
print(f'A soma entre {numero_1} e {numero_2} é : {soma}')'''



# DESAFIO 04.      Faça um programa que leia algo pelo teclado e mostre seus tipos primitivos


'''teste = input('Digite algo: ')
print('A palavra é string?  {}'.format(teste.isalpha()))
print('A palavra é um número? {}'.format(teste.isnumeric()))
print('A palavra é alfanumérica? {}'.format(teste.isalnum()))
print('A palavra está capitalizada? {}'.format(teste.istitle()))''' 




# DESAFIO 05.  Faça um programa que receba um número e mostre seu antecessor e seu sucessor.


'''numero = int(input('Digite um número: '))
print('O antecessor é o número: {}, o número digitado foi: {} e o seu sucessor é: {}'.format((numero-1), numero, (numero+1)))'''



# DESAFIO 06.    Faça um programa que receba um número e mostre o seu dobro, triplo e raiz quadrada.


'''numero = int(input('Digite um número: '))

print('O dobro do número é: {}, o triplo é: {} e a sua raiz quadrada é: {}'.format((numero * 2), (numero * 3), (numero ** (1/2))))'''



# DESAFIO 07.   Faça um programa que receba as duas notas de um aluno e faça sua média.


''''nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2
print('A média é: {:.2f}'.format(media))'''



# DESAFIO 08.    Faça um programa que leia valores em metros e retorne em centimetros:


'''metros = float(input('Quantos metros você gostaria de converter para centrimetros, milimetros e decimetros? '))
centimetros = metros * 100
milimetros = metros * 1000
decimetro = metros * 10
print('{} metros, equivale a: {}cm, {}mm e a {} dm'.format(metros, centimetros, milimetros, decimetro))'''



# DESAFIO 09.    Faça um programa que leia o número inteiro e devolva sua tabuada.


'''numero = int(input('Digite um número para ver sua tabuada: '))
n = 0
while n <=10:
    mult = numero * n
    print('{} x {:2} = {}'.format(numero, n, mult))
    n += 1'''



# DESAFIO 10.    Faça um programa que converta o valor que a pessoa tem na carteira de reais para dólares. U$$: 1.00 = R$: 3.27


'''reais = float(input('Digite quantos reais você tem em sua carteira R$: '))
dolares = reais / 3.27
print('Com R$: {} você pode comprar U$$: {:.2f}'.format(reais, dolares))'''



# DESAFIO 11.    Faça um programa que calcule a área de uma parede em metros e a quantidade e tinta necessária para pintar essa parede. Cada litro pinta 2m quandrados.


'''largura = float(input('Digite o comprimento da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = altura * largura
quantidade_tinta = area / 2
print('A área total a ser pintada é de: {:.2f} metros quadrados. E a quantidade são: {:.2f} litros'.format(area, quantidade_tinta))'''



# DESAFIO 12.    Faça um programa que receba o preço de um produto  conceda 5% de desconto e devolva o valor do produto e o desconto do produto.


'''def produto_desconto():
    produto = float(input('Digite o valor do produto? R$ '))
    desconto = float(input('Digite o percentual de desconto: '))
    desconto = produto * (desconto/100)
    preco_desconto = produto - desconto
    print('O valor do produto é R$: {}'.format (produto))
    print('O valor do desconto é R$: {:.2f}'.format(desconto))
    print('O valor total a pagar é de: R$ {:.2f}'.format(preco_desconto))
    

produto_desconto()'''



# DESAFIO 13.    Faça um programa que receba o salário de um funcionário e acrescente 15% de aumento, retornar o novo salário.


'''salario = float(input('Digite o seu salário: R$ '))
novo_salario = salario  + (salario * 15 / 100)
print('Seu salário atual é de: R$ {}'.format(salario))
print('Seu novo salário após o aumento de 15% é de: R$ {:.2f}'.format(novo_salario))'''



# DESAFIO 14.   Faça um programa que receba a temperatura em celsius e retorne em Fahenheit,


'''temperatura = float(input('Digite a temperatura em graus Celsius: '))
Fahrenheit = ((9 * temperatura) / 5) + 32
print('A temperatura em Fahrenheit é: {} F'.format(Fahrenheit))''' 



# DESAFIO 15.   Faça um programa que calcule o valor a ser pago pelo aluguel de um veículo. Sabendo que a diária custa R$ 60.00/Dia e o km rodado custa R$ 0.15/Km.


'''dias_alugados = int(input('Quantos dias você gostaria de alugar o carro? '))
km_rodado = float(input('Quantos kms você rodou? '))
valor_aluguel = dias_alugados * 60
valor_km = km_rodado * 0.15
total_aluguel = valor_aluguel + valor_km
print('O valor do aluguel para {} dias: R$ {:.2f}\n'.format(dias_alugados, valor_aluguel))
print('O valor dos {} kms rodados: R$ {:.2f}\n'.format(km_rodado, valor_km))
print('O valor do total do aluguel: R$ {:.2f}'.format(total_aluguel))'''



# DESAFIO 16.   Faça um programa que receba um número e retorne apenas sua parte inteira.


'''numero = float(input('Digite um número qualquer: '))
print('A parte inteira do número é: {}'.format(int(numero)))'''



# DESAFIO 17.   Faça um programa que receba o cateto oposto e o adjacente de um triângulo e calcúle o comprimento da Hipotenusa:


'''import math
cateto_adj = float(input('Digite o cateto oposto: '))
cateto_opos = float(input('Digite o cateto adjacente: '))
hipotenusa = math.sqrt((((cateto_adj ** 2) + (cateto_opos ** 2))))
print('O valor da hipotenusa: {:.2f}'.format(hipotenusa))'''

# ou


'''ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
hi = math.hypot(ca, co)
print(hi)'''



# DESAFIO 18.   Faça um programa programa que pegue um ângulo qualquer e retorne: seno, cosseno e tangente desse  angulo


'''from math import cos, sin, tan, radians 
angulo = float(input('Digite o ângulo que você deseja saber o sen, cos, tang: '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print('Para o ângulo de {} graus, cosseno: {:.2f}, seno: {:.2f} e tangente: {:.2f}'.format(angulo, cosseno, seno,tangente))'''



# DESAFIO 19.    Faça um programa que escolha uma pessoa aleatória para fazer limpeza do quadro.


'''from random import choice

nome_1 = input('Digite o primeiro nome: ')
nome_2 = input('Digite o segundo nome: ')
nome_3 = input('Digite o terceiro nome: ')
nome_4 = input('Digite o quarto nome: ')
nomes = [nome_1, nome_2, nome_3, nome_4]
print('O nome sorteado foi: {}'.format(choice(nomes)))'''



# DESAFIO 20.   Faça um programa que escolha aleatoriamente a ordem de apresentação de trabalho.


'''from random import shuffle

n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o segundo aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('A ordem de apresentação é: {}'.format(nomes))'''



# DESAFIO 21. colocar musica pra tocar
   


# DESAFIO 22.   Faça um programa que receba o nome completo de uma pessoa:  a) retorne o nome com letras maiúsculas; b) retorne o nome com todas as letras minúsculas; c) quantas letras ao todo sem os espaços; d) quantas letras tem o primeiro nome?


'''nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
nome = nome.split()
print(len(nome[0]))'''



# DESAFIO 23.   Faça um programa que receba um número e separe em miliar, centenza, dezana, unidade.


'''numero = int(input('Digite um número: '))
miliar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100)   // 10
unidade = numero % 10
print(f'Miliar: {miliar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')'''

# OU 

'''numero = int(input('Digite um número: '))
miliar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero % 10
print(f'Miliar: {miliar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')'''



# DESAFIO 24.   Faça um programa que receba o nome de uma pessoa e diga se ela começa com nome SANTO.


'''nome = str(input('Digite o nome da sua cidade: ').strip().upper())
nome = nome.split()
print('SANTO'in nome[0])'''



# DESAFIO 25.  Faça um programa que receba o nome de uma pessoa e diga se tem SILVA no nome:


''''nome = str(input('Digite seu nome: ').upper())
print('SILVA' in nome)'''



# DESAFIO 26.   Faça um programa que receba uma frase e: a) Quantas vezes aparece a letra A; b) Onde ela aparece pela primeira vez; c) Onde ela aparece pela última vez;


'''frase = str(input('Digite uma frase: ').lower().strip())
print(frase.count('a'))
print(frase.find('a') + 1)
print(frase.rfind('a')+ 1)'''



# DESAFIO 27.   Faça um programa que receba um nome e: a) Retorne o primeiro nome; b) Retorne o último nome.


'''nome = str(input('Digite seu nome completo: ').title().strip())
nome = nome.split()
print(f'O primeiro nome: {nome[0]}')
print(f'O último nome: {nome[-1]}')'''



# DESAFIO 28.   Faça um programa que advinhe o número entre 0 e 5 sorteado pelo computador.


'''from random import randint

numero = int(input('Digite um número entre 1 e 5: '))
sorteado = randint(1,5)
if numero == sorteado:
    print('Parabens você acertou!')
else:
    print('Voce errou!')
    print(f'Número sorteado: {sorteado}')
print('Fim do programa!')'''



# DESAFIO 29.   Faça um programa que diga se a velocidade está dentro do limite de 80km/h, caso ultrapassar o limite, informar que recebera uma multa de R$ 7.00 / Km acima do limite.


'''velocidade = int(input('Digite a sua velocidade: '))
if velocidade > 80:
    diferenca = velocidade - 80
    valor = diferenca * 7
    print('Você está acima do limite de 80km/h, você pagará uma multa de R$ 7.00/km acima do limite.\n')
    print(f'Você excedeu o limite em: {diferenca}km/h\n')
    print(f'O valor da multa: {diferenca} km/h x R$ 7.00: R$ {valor:.2f}\n')
else:
    print('Você está dentro do limite permitido.')'''



# DESAFIO 30.   Faça um programa que receba um número e diga se ele é par ou impar.


'''numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')'''



# DESAFIO 31.   Faça um programa que cálcule a passagem beaseada em kms. Até 200km R$ 0.50 acima R$ 0.45.

'''km_viagem = int(input('Digite a distância da sua viagem(km): '))
if km_viagem <= 200:
    valor = km_viagem * 0.50
    print(f'O valor da passagem para {km_viagem} x 0.50: R$ {valor:.2f}')
else:
    valor = km_viagem * 0.45
    print(f'O valor da passagem para {km_viagem} x 0.45: R$ {valor:.2f}')'''



# DESAFIO 32.   Faça um programa que receba um ano qualquer e cálcule se ele é bissexto.


'''from datetime import date
ano = int(input('Digite o ano para saber se ele é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')'''



# DESAFIO 33.   Faça um programa que receba 3 números e diga qual é o maior e o menor.


'''numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_3 = int(input('Digite o teceiro numero: '))
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3
maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3
print(f'O maior número é: {maior} e o menor número: {menor}')'''


# ou 


'''numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_3 = int(input('Digite o teceiro numero: '))
if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'O número {numero_1} é o maior número.')
    if numero_2 > numero_3:
        print(f'O número {numero_3} é o menor número')
    else:
        print(f'O número {numero_2} é o menor.')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'O número {numero_2} é o maior.')
    if numero_1 > numero_3:
        print(f'o número {numero_3} é o menor.')
    else:
        print(f'O número {numero_1} é o menor.')
else:
    print(f'O número {numero_3} é o maior.')
    if numero_1 > numero_2:
        print(f'O número {numero_2} é o menor.')
    else:
        print(f'O número {numero_1} é o menor.')'''

    

# DESAFIO 34.   Faça um programa que pergunte ao funcionário o seu salário e calcule o valor do seu aumento. a) Para salários acima de R$ 1250.00 aumento de 10%; b) Para salários abaixo de R$ 1250.00 aumento de 15%.


'''salario = float(input('Digite o seu salário para podermos calcular seu aumento. Salário R$ '))
if salario >= 1250:
    aumento = salario * (10/100)
    salario_final = salario + aumento
    print(f'O seu salário de R$ {salario:.2f} recebera um acréscimo de 10%. Acréscimo: R$ {aumento:.2f}.')
    print(f'R$ {salario:.2f} + R$ {aumento:.2f}. O seu novo salário: R$ {salario_final:.2f}')
else:
    aumento = salario * (15/100)
    salario_final = salario + aumento
    print(f'O seu salário de R$ {salario:.2f} recebera um acréscimo de 15%. Acréscimo: R$ {aumento:.2f}.')
    print(f'R$ {salario:.2f} + R$ {aumento:.2f}. O seu novo salário R$ {salario_final:.2f}')'''



# DESAFIO 35.    Faça um programa que leia o comprimento de tres retas e veja se pode formar triangulo.


'''reta_1 = float(input('Digite o comprimeito da primeira reta: '))
reta_2 = float(input('Digite o comprimeito da segunda reta: '))
reta_3 = float(input('Digite o comprimeito da terceira reta: '))
if reta_1 + reta_2 <= reta_3 or reta_2 + reta_3 <= reta_1 or reta_1 + reta_3 <= reta_2:
    print('A soma de duas retas deve ser SEMPRE maior que a terceira para se formar um triângulo. Nesse caso, não temos formação de triângulo.')
else:
    print('As retas formam triângulo!')
    if reta_1 == reta_2 == reta_3:
        print('O triângulo formado é equilátero (todos os seus lados são iguais).')
    elif reta_2 == reta_1 != reta_3 or reta_2 == reta_3 != reta_1 or reta_3 == reta_1 != reta_2:
        print('O triângulo formado é isóceles (2 lados são iguais).')
    else: 
        reta_1 != reta_2 != reta_3
        print('O triângulo formado é escaleno (todos os seus lados são diferentes).')'''



#    COLOCANDO CORES NO PYTHON
#    PARA CHAMAR O CÓDIGO: print('\033[0;30;40mOlá, Mundo!\33[m')
#    CÓDIGO: Tudo dentro das aspas do comando: O início  \033[     Comando das cores: 0;30;40m    fim: \33[m são fixos
#    Primeira casa: style [0: sem nada, 1: negrito, 4: sublinhado, 7: com preenchimento]
#    Segunda casa: cor letra[30: branco, 31: vermelho, 32: verde, 33: amarelo, 34: azul, 35: roxo, 36: marinho, 37: cinza]
#    Terceira casa: fundo [40: branco, 41: vermelho, 42: verde, 43: amarelo, 44: azul, 45: roxo, 46: marinho, 47: cinza]    

'''print('\033[0;30;40mOlá, Mundo!\33[m')
print('\033[0;31;41mOlá, Mundo!\33[m')
print('\033[0;32;42mOlá, Mundo!\33[m')
print('\033[0;33;43mOlá, Mundo!\33[m')
print('\033[0;34;44mOlá, Mundo!\33[m')
print('\033[0;35;45mOlá, Mundo!\33[m')
print('\033[0;36;46mOlá, Mundo!\33[m')
print('\033[0;37;47mOlá, Mundo!\33[m')

print()

print('\033[1;30;40mOlá, Mundo!\33[m')
print('\033[1;31;41mOlá, Mundo!\33[m')
print('\033[1;32;42mOlá, Mundo!\33[m')
print('\033[1;33;43mOlá, Mundo!\33[m')
print('\033[1;34;44mOlá, Mundo!\33[m')
print('\033[1;35;45mOlá, Mundo!\33[m')
print('\033[1;36;46mOlá, Mundo!\33[m')
print('\033[1;37;47mOlá, Mundo!\33[m')

print()

print('\033[4;30;40mOlá, Mundo!\33[m')
print('\033[4;31;41mOlá, Mundo!\33[m')
print('\033[4;32;42mOlá, Mundo!\33[m')
print('\033[4;33;43mOlá, Mundo!\33[m')
print('\033[4;34;44mOlá, Mundo!\33[m')
print('\033[4;35;45mOlá, Mundo!\33[m')
print('\033[4;36;46mOlá, Mundo!\33[m')
print('\033[4;37;47mOlá, Mundo!\33[m')

print()

print('\033[7;30;40mOlá, Mundo!\33[m')
print('\033[7;31;41mOlá, Mundo!\33[m')
print('\033[7;32;42mOlá, Mundo!\33[m')
print('\033[7;33;43mOlá, Mundo!\33[m')
print('\033[7;34;44mOlá, Mundo!\33[m')
print('\033[7;35;45mOlá, Mundo!\33[m')
print('\033[7;36;46mOlá, Mundo!\33[m')
print('\033[7;37;47mOlá, Mundo!\33[m')

print(f'Olá, {'\033[33m'} Michael {'\33[m'}')'''



# DESAFIO 36.   Colocar cores em 10 exercícios passados.