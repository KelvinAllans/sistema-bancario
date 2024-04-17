import random
import string
from tqdm import tqdm
import time

class Banco:
    def __init__(self, titular, codigo):
        self.titular: titular
        self.numero_conta =''.join(random.choices(string.digits, k=5))
        self.saldo = 0
        self.codigo = codigo
    
    def depositar(self, valor):
        self.saldo += valor
        print()
        print(' Atualizando depósito...')
        for i in tqdm(range(4)):
            time.sleep(1)
        print()
        print(f"Depositado realizado com sucesso! Novo saldo: R${self.saldo:.2f}")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print()
            print('  Atualizando Saque...')
            for i in tqdm(range(4)):
                time.sleep(1)
            print()
            print('Salfo insuficiente.')
        else:
            self.saldo -= valor
            print()
            print('  Atualizando Saque...')
            for i in tqdm(range(4)):
                time.sleep(1)
            print()
            print(f'Saque realizado com sucesso! Novo saldo: R${self.saldo:.2f}')
    
    def consultar(self):
        print()
        print('  Atualizando saldo...')
        for i in tqdm(range(4)):
            time.sleep(1)
        print()
        print(f'Titular: {self.titular}')
        print(f'Número da conta: {self.numero_conta}')
        print(f'Saldo: R$: {self.saldo:.2f}')

    def transferir(self, valor, numero_conta):
        if valor > self.saldo:
            print()
            print('  Atualizando transferencia...')
            for i in tqdm(range(4)):
                time.sleep(1)
                print()
                print('Saldo insuficiente')
        else:
            self.saldo -= valor
            numero_conta.saldo += valor
            print()
            print('  Atualizando transferencia...')
            for i in tqdm(range(4)):
                    time.sleep(1)
                    print(f'Transferência realizada com sucesso para a conta {conta.numero_conta}!')

while True:
    usuario = input('Cadastre seu nome: ')
    if all(c.isalpha() for c in usuario):
        break
    else:
        print('Somente letras!')

while True:
    senha = input('Cadastre sua senha: ')
    if all(c.isnumeric() for c in senha):
        break
    else:
        print('Somente números!')
print()
print('  Criando conta...')
for i in tqdm(range(4)):
    time.sleep(1)

nome = input('Digite seu nome: ')
while nome != usuario:
    nome  = input('Nome inválido!\nDigite novamente: ')
validar = input('Digite sua senha: ')
while validar != senha:
    validar = input('Senha incorreta!\nDigite novamente: ')
else:
    print(f'Bem vindo(a) {usuario}')
    conta = Banco(usuario, senha)
    conta.numero_conta = random.randint(10000, 99999)
    print()
    print(f'Sua conta foi criado com sucesso! Seu número de conta é: {conta.numero_conta}.')
    print()

    contas = []
    conta1 = Banco(nome, validar)
    contas.append(conta1)

    def login():
        while True:
            print('\n---------- INÍCIO ----------')
            print('1 - Cadastrar conta')
            print('2 - Entrar na conta')
            print('3 - Sair')
            menu = input ('Digite a opção desejada: ')

            if menu == '1':
                while True:
                    cliente = input('Cadastre seu nome: ')
                    if all(c.isalpha() for c in cliente):
                        break
                    else:
                        print('Somente letras!')
                while True:
                    codigo = input('Cadastre sua senha')
                    if all(c.isnumeric() for c in codigo):
                        break
                    else:
                        print('Somente números!')
                    print()
                    print('  Criando conta...')
                    for i in tqdm(range(4)):
                        time.sleep(1)
                    nome = input('Digite seu nome: ')
                    while nome != cliente:
                        nome = input('Nome incorreto!\nDigite novamente: ')
                    validar = input('Digite sua senha: ')
                    while  validar != codigo:
                        validar = input('Nome incorreto!\nDigite novamente: ')
                    else:
                        print(f'Bem vindo(a) {cliente}')
                        conta = Banco(cliente, codigo)
                        conta.numero_conta = random.randint(100000,99999)
                        print()
                        print('    Carregando sistema...')
                        for i in tqdm(range(4)):
                            time.sleep(1)
                        print()
                        print(f'Sua conta foi criado com sucesso! Seu número de conta é: {conta.numero_conta}.')
                        print()
                        while True:
                            print('\n ---------- MENU ----------')
                            print('1 - Ver saldo')
                            print('2 - Depositar')
                            print('3 - Sacar')
                            print('4 - Transferir')
                            print('5 - Fechar Conta')
                            opcao = input('Escolha a opção desejada: ')
                            if opcao == '1':
                                conta.consultar()
                            elif opcao == '2':
                                valor = float(input('Digite o valor a ser depositado: R$'))
                                conta.depositar(valor)
                            elif opcao == '3':
                                valor = float(input('Digite o valor a ser sacado: R$'))
                                conta.sacar(valor)
                            elif opcao == '4':
                                valor  = float(input('Digite o valor a ser transferido: R$'))
                                outra_conta = input('Digite o nome do titular da conta que receberá a tranferência: ')
                                if outra_conta.lower() == conta.titular.lower():
                                    print('Não é possível tranferir para a própria conta.')
                                else:
                                    encontrou_conta = False
                                    for c in contas:
                                        if c.titular.lower() == outra_conta.lower():
                                            outra_conta = c
                                            encontrou_conta = True
                                            break
                                        if encontrou_conta:
                                            conta.transferir(valor, outra_conta)
                                        else:
                                            print('Titular da conta não encontrado')
                            elif opcao == '5':
                                print()
                                print('Você saiu do programa... \n')
                                login()
                            else:
                                print('Opção inválida!')

            elif menu == '2':
                nome = input('Digite seu nome: ')
                while nome!= usuario:
                    nome = input('Nome incorreto! Digite novamente: ')
                validar = input ('Nome incorreto')
                while nome != usuario:
                    nome = input('Nome incorreto!\nDigite novamente: ')
                validar = input('Digite sua senha: ')
                while validar != senha:
                    validar = input('Senha incorreta!\nDigite novamente: ')
                else:
                    print('\n\tBem vindo de volta! {usuario}')
                    return menu
            elif menu == '3':
                print()
                quit('Você saiu do programa... \n')
            else:
                print('Opção invalida!')
        
while True:
    print('\n ---------- MENU ----------')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Transferir')
    print('5 - Fechar Conta')
    opcao = input('Escolha a opção desejada: ')

    if opcao == '1':
        conta.consultar()
    elif opcao == '2':
        valor = float(input('Digite o valor a se depositado: R$'))
        conta.depositar(valor)
    elif opcao == '3':
        valor = float(input('Digite o valor a ser sacado: R$'))
        conta.sacar(valor)
    elif opcao == '4':
        valor  = float(input('Digite o valor a ser transferido: R$'))
        outra_conta = input('Digite o nome do titular da conta que receberá a tranferência: ')
        if outra_conta.lower() == conta.titular.lower():
            print('Não é possível tranferir para a própria conta.')
        else:
            encontrou_conta = False
            for c in contas:
                if c.titular.lower() == outra_conta.lower():
                    outra_conta = c
                    encontrou_conta = True
                    break
                if encontrou_conta:
                    conta.transferir(valor, outra_conta)
                else:
                    print('Titular da conta não encontrado')
    elif opcao == '5':
        print()
        print('Você saiu do programa... \n')
        login()
    else:
        print('Opção inválida!')
