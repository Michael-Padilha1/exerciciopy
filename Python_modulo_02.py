# DESAFIO 36.   Faça um programa que forneça um empréstimo bancário. a) Pergunte o valor do imóvel; b) Salário do comprador; c) Quantos anos para pagar; d) Calcular valor mensal da prestação (max: 30% salário), caso contrário sem empréstimo.


'''imovel = float(input('Digite o valor do imóvel que deseja financiar: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Quantos anos para pagar? '))
numero_parcelas = 12 * anos
valor_parcela = imovel/numero_parcelas
porcentagem_salario = (valor_parcela/salario) * 100 
if porcentagem_salario <= 30:
    print('Empréstimo concedido!!!')
    print(f'O total de parcelas é {numero_parcelas}')
    print(f'O valor das parcelas: R$ {valor_parcela:.2f}')
    print(f'O valor das parcelas representa: {porcentagem_salario:.2f}% do seu salário.')
    print('Parabéns pela aquisição, felicidades no novo lar!!!')
elif porcentagem_salario >30:
    print(f'Em {numero_parcelas} vezes o valor da parcela R$ {valor_parcela:.2f}  representa {porcentagem_salario:.2f}% do seu salário. Infelizmente só aprovamos até 30% do valor do salário.')
print('Obrigado pela preferência!!!')'''



# DESAFIO 37.   Faça um programa que receba um numero inteiro qualquer e escolha base de conversão. 1- Binário, 2- octanal, 3- hexadecimal.

'''numero = float(input('Digite um número qualquer: '))
print('Qual Base a bese de conversão: 1) Binário  2) Octal  3) Hexadecimal')
base = int(input('Digite sua opção: '))
if base == 1:

elif base == 2:

else:'''



# DESAFIO 38.   Faça um programa que leia dois números e compare eles entre si: maior, menor, ou iguais.


'''n_1 = int(input('Digite um número qualquer: '))
n_2 = int(input('Digite outro número qualquer: '))
if n_1 == n_2:
    print(f'Os números {n_1} e {n_2} são IGUAIS.')
elif n_1 > n_2:
    print(f'O número {n_1} é maior que {n_2}.')
else:
    print(f'O número {n_2} é maior que {n_1}.')'''



# DESAFIO 39.   Faça um programa que receba o ano do nascimento e informe de acordo com sua idade: a) Se ainda irá se alistar ao serviço militar; b) se é a hora de se alistar; c) se já passou o momento d) mostrar o prazo que falta e o que passou


'''idade = int(input('Digite sua idade: '))
if idade == 18:
    print('Chegou o ano do seu alistamento.')
elif idade < 18:
    falta = 18 - idade
    print(f'Ainda não chegou o momento do seu momento, está faltando {falta} ano(s) para o seu alistamento.')
elif idade > 18:
    passou = idade - 18
    print(f'Já se passaram {passou} ano(s) desde seu alistamento.')'''



# DESAFIO 40.   Faça um programa que receba as duas notas do aluno e calcule sua media e mostra. Media abaixo de 5.0 reprovado, Media 5.0-6.9 recuperação e Media 7 ou mais aprovado.


'''nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
media = (nota_1 + nota_2)/2
if media >= 7.0:
    print(f'Sua média {media:.1f}')
    print('Parabéns, você está aprovado!!!')
elif media < 7.0 and media > 5.0:
    print(f'Sua média: {media:.1f}')
    print('Você está de recuperação, estude mais!!!')
else:
    print(f'Sua média {media:.1f}')
    print('Você está reprovado, nos vemos no ano que vem!!!')'''



# DESAFIO 41.   Faça um programa que leia a data de nascimento do atleta e separe por categoria de acordo com a idade. Até 9 anos: mirim; Até 14 anos: infantil; Até 19: junior; Até 20 anos: Sênior; Acima: master.

'''idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Você está na categoria MIRIM até 9 anos.')
elif idade > 9 and idade <= 14:
    print('Você está na categoria INFANTIL até 14 anos.')
elif idade > 14 and idade <= 19:
    print('Você está na categoria JUNIOR até 19 anos.')
elif idade == 20:
    print('Você está na categoria SÊNIOR até 20 anos.')
else:
    print('Você está na categoria MASTER acima 20 anos.')'''



# DESAFIO 42.   Exercicio 35 falando que tipo de triângulo.

'''reta_a = float(input('Digite o tamanho da reta A: '))
reta_b = float(input('Digite o tamanho da reta B: '))
reta_c = float(input('Digite o tamanho da reta C: '))
if reta_a + reta_b <= reta_c or reta_a + reta_c <= reta_b or reta_b + reta_c <= reta_a:
    print('Não tem como formar triângulo, pois a soma de dois lados SEMPRE deve ser maior que o terceiro.')
elif reta_a == reta_b == reta_c:
    print('O triângulo é equilátero, ele tem todos os lados iguais.')
elif reta_a == reta_b or reta_a == reta_c or reta_b == reta_c:
    print('O triângulo é isóceles, tem 2 lados iguais.')
else:
    print('O triângulo é escaleno, todos os lados são diferentes.')'''



# DESAFIO 43.   Faça um programa que receba o peso e altura de uma pessoa e mostre o seu IMC e mostre conforme tabela: Abaixo 18.5 : abaxo do peso; Entre 18.5 e 25 : peso ideal; Entre 25-30 sobre peso; 30-40: Obesidade; Acima de 40: Obesidade morbida.


'''altura = float(input('Digite sua altura sua altura em metros: '))
peso = float(input('Digite o seu peso: '))
imc = peso/altura**22
if imc <= 18.5:
    print(f'Você está abaixo do peso (IMC: < 18.5), seu IMC {imc}')
elif imc > 18.5 and imc <= 25:
    print(f'Você está no peso ideal (IMC: 18.5 - 25), seu imc {imc}')
elif imc > 25 and imc <= 30:
    print(f'Você está sobre peso (IMC: 25 - 30), seu IMC {imc}')
elif imc > 30 and imc <=40:
    print(f'Você está em obesidade (IMC: 30 - 40), seu IMC {imc}')
else:
    print(f'Você está em obesidade morbida (IMC: > 40), seu IMC {imc}')'''



# DESAFIO 44.   Faça um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento. A vista dinheiro/cheque: 10% desconto, a vista no cartão 5% desconto, Até 2x no cartão preço normal, 3x ou mais juros 20%.


'''valor = float(input('Digite o valor do produto: R$ '))
print('Formas de pagamento: 1) Dinheiro  2) Cartão  3) Cheque')
forma_pagamento = int(input('Digite a forma de pagamento: '))
if forma_pagamento == 1 or forma_pagamento == 3:
    valor_pagar = valor - (valor * 0.15)
    print(f'Para pagamento à vista no dinheiro, desconto 15% o valor de R$ {valor:.2f} fica por R$ {valor_pagar:.2f}')
elif forma_pagamento == 2:
    numero_parcelas = int(input('Digite o número de parcelas: '))
    if numero_parcelas == 1:
        valor_pagar = valor - (valor * 0.05)
        print(f'Para pagamento à vista no cartão, desconto 5% o valor de R$ {valor:.2f} fica por R$ {valor_pagar:.2f}')
    elif numero_parcelas <= 2:
        valor_pagar = valor 
        print(f'Para pagamento em até 2 vezes o valor é o da etiqueta de R$ {valor:.2f}')
    else:
        valor_pagar = valor * (1 + 20/100)
        print(f'Para parcelamento em 3x ou mais valor de R$ {valor:.2f} sofre um acréscimo de 20% e fica por R$ {valor_pagar:.2f}')'''