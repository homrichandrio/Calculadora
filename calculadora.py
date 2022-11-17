
# operação entre dois valores
# pendente - limpar a tela caso usuario queira fazer um novo cálculo
# mostrar operação ao usuário
# fechar programa caso o usuário não queria fazer uma nova operação

import time as tm
import sys
import os



# variavel para execução do programa originalmente definida como True
executar = True
while executar == True:

    os.system('cls') or None

    # mensagens da inicialização do programa

    print('\n----------------------------------------------\nBem-vindo ao programa Cálculadora em Python!\n----------------------------------------------\n')
    tm.sleep(2)
    print('Para utilização deste programa, utilize os códigos abaixo para realizar as seguintes operações:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Exponenciação\n\n----------------------------------------------\n')
    tm.sleep(2)

    # definição do código da operação à ser utilizada - convertida em float
    codigo_operacao = input("Informe o código da operação que você deseja fazer: ")
    print('')
    tm.sleep(1)
    ### validação da entrada do código da operação pelo usuário e atribuição das variaveis imputadas pelo usuário

    if float(codigo_operacao) < 1:
        cond_codigo_operacao = False
    elif float(codigo_operacao) > 4:
        cond_codigo_operacao = False
    else:
        cond_codigo_operacao = True

    while cond_codigo_operacao == False:
        print('\nCódigo Invalido.\nInforme um novo código abaixo:\n')
        codigo_operacao = input()
        tm.sleep(1)
        if float(codigo_operacao) < 1:
            cond_codigo_operacao = False
        elif float(codigo_operacao) > 4:
            cond_codigo_operacao = False
        else:
            cond_codigo_operacao = True

    # execução da atribuição das variaveis pelo inputadas usuário
    else:
        valor1, valor2 = (float(input("Informe o primeiro valor que você deseja utilizar: ")),float(input("Informe o segundo valor que você deseja utilizar: ")))
        print('\n----------------------------------------------\n')
        tm.sleep(1)
    ### inicialização do processamento dos imputs para cada uma das operações

    # operação de soma 
    if codigo_operacao == '1':
        resultado = valor1 + valor2
        print('Sendo:\n{} + {} = {}\n\n----------------------------------------------\n'.format(valor1,valor2,resultado))
        tm.sleep(1)
    # operação de subtração 
    elif codigo_operacao == '2':
        resultado = valor1 - valor2
        print('Sendo:\n{} - {} = {}\n\n----------------------------------------------\n'.format(valor1,valor2,resultado))
        tm.sleep(1)
    # operação de multiplicação 
    elif codigo_operacao == '3':
        resultado = valor1 * valor2
        print('Sendo:\n{} * {} = {}\n\n----------------------------------------------\n'.format(valor1,valor2,resultado))
        tm.sleep(1)
    # operação de exponenciação 
    elif codigo_operacao == '4':
        resultado = valor1 ** valor2
        print('Sendo:\n{} elevado à potência de {} = {}\n\n----------------------------------------------\n'.format(valor1,valor2,resultado))
        tm.sleep(1)

        
### Comando para executar novamente o Programa conforme desejo do Usuario 

    comando_execucao = input('Gostaria de realizar um novo cálculo? (Y/N) ')
    print('')
    status_comando_execucao = False
    tm.sleep(1)

    if comando_execucao == 'Y' or comando_execucao == 'N' or comando_execucao == 'y' or comando_execucao == 'n':
        status_comando_execucao = True

    else:
        status_comando_execucao = False
        while status_comando_execucao == False:
            print('\nComando Invalido.\nInforme um novo código abaixo:\n')
            comando_execucao = input()
            tm.sleep(1)
            if comando_execucao == 'Y' or comando_execucao == 'y' or comando_execucao == 'N' or comando_execucao == 'n':
                status_comando_execucao = True
                print('\nOpção Válida Selecionada!\n')
                tm.sleep(1)
            else:
                status_comando_execucao = False

    if comando_execucao == 'Y' or comando_execucao == 'y':
        executar = True

    else:
        executar = False
        tm.sleep(1)

os.system('cls') or None
print('\n-------------------------------------------------\nVocê utilizou o programa Cálculadora em Python!\n-------------------------------------------------\n')
tm.sleep(2)
print('Este programa foi desenvolvido por Andrio Homrich.\nVersão 1.1 lançada em 16.11.2022\n\n-------------------------------------------------\nVolte Sempre!\n-------------------------------------------------\n')
tm.sleep(2)
tm.sleep(2)        
sys.exit()
