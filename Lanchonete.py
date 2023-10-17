print('Bem Vindo(a) a Lanchonete')

print('  ------------------- Cardápio -------------------  ')

print('|   Código  |        Descrição           |  Valor  |')
print('|    100    |      Cachorro Quente       | R$ 9.00 |')
print('|    101    |   Cachorro Quente Duplo    | R$ 11.00|')
print('|    102    |           X-Egg            | R$ 12.00|')
print('|    103    |          X-Salada          | R$ 13.00|')
print('|    104    |          X-Baicon          | R$ 14.00|')
print('|    105    |           X-Tudo           | R$ 17.00|')
print('|    200    |      Refrigerante Lata     | R$ 5.00 |')
print('|    201    |         Chá Gelado         | R$ 4.00 |')

acumulador = 0

# -----------------------Inicio função código-----------------------
while True: # Enquando(while): Estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado
    código = input('Entre com o código desejado:') # Input permite solicitar uma informação ao usuário, faz um login em um sistema
    if código != '100' and código != '101' and código != '102' and código != '103' and código != '104' and código != '105' and código != '200' and código != '201':
        print('Opção Inválida. Pare de digitar códigos que não exitem!:')
        continue  # Se o usuário digitar algo inválido volta para o começo do while

    elif (código == '100'): # O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa
        valor = 9
        print('Você escolheu um Cachorro Quente no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '101'):
        valor = 11
        print('Você escolheu um Cachorro Quente Duplo no valor de R$ {:.2f} reais.'. format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '102'):
        valor = 12
        print('Você escolheu um X-Egg no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '103'):
        valor = 13
        print('Você escolheu um X-Salada no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '104'):
        valor = 14
        print('Você escolheu um X-Baicon no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '105'):
        valor = 17
        print('Você escolheu um X-Tudo no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '200'):
        valor = 5
        print('Você escolheu um Refrigerante Lata no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

    elif (código == '201'):
        valor = 4
        print('Você escolheu um Chá Gelado no valor de R$ {:.2f} reais.' .format(valor))
        acumulador = acumulador + valor  # Pagar o valor

# -----------------------Verifica se o cliente deseja mais alguma coisa-----------------------

    pedir_mais = input('Deseja pedir mais alguma coisa (S/Digite outra tecla)?:')
    pedir_mais = pedir_mais.upper()  # Resolve o problema de digitar 's' e 'S'
    if pedir_mais == 'S':
        continue
    else:  # # O comando é usado para execultar um bloco de códgo, caso o resultado da expressão informada na instrução if seja falso
        print('Valor total a ser pago: R${:.2f}'.format(acumulador, valor))