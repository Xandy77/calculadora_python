# importação de biblioteca
import os

#inicia o loop
while True:
    print(f'{'-'*20} CALCULADORA PYTHON {'-'*20}\n')
    print('1 - Soma.')
    print('2 - Subtração.')
    print('3 - Multiplicação.')
    print('4 - Divisão.')
    print('5 Resto da Divisão')
    print('6 Potenciação')

    print('5 - Sair do programa.')

# operação escolhida
operacao = input('Operação desejada: ')

# verifica se o usuário vai fazer o calculo ou sair do programa 
if operacao != '5':
    
#informar os numeros
 x = str(input('Informe o 1º número: ')).replace(',', '.')
 y = str(input('Informe o 2º número: ')).replace(',', ',')

# converte para float
 x = float(x)
 y = float(y) 

# limpa tela
os.system('cls')

# verfica a operaçãodesejada
match operacao:
    case '1':
        print(f'{x} + {y} = {x + y}')
    case '2':
        print(f'{x} - {y} = {x - y}')
    case '3':
        print(f'{x} x {y} = {x * y}')
    case '4':
     if y != 0:
        print(f'{x} : {y} = {x / y}')
     else:
      print('Valor do divisor inaválido.')
    case '5':
      if y != 0:
    print(f'Resto de {x} : {y} = {x %}')
    case _:
        print('Operação Inválida')

# executa o programa
else:
    print('Programa encerrado!')
    break