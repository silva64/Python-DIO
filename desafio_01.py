menu = """"""

[d] Depositário
[s] Sacar
[e] Extrato
[q] Sair

=> """"""

saldo = 00
limite = 500500
extrato = """"
numero_saques = 00
LIMITE_SAQUES = 33

embora verdadeiro:

 opcao = entrada(menu)

 se opcao == "d":"d":
 valor = fluoração (entrada ("Informe o valor do dispositivo:"))"Informe o valor do dispositivo:"))

 valor Se > 0:0:
 saldo += valor
 extrato += f "Depósito: R$ {valor:.2f}\n""Depósito: R$ {valor:.2f}\n"

 outro:
 imprimir ("Operação falhou! Ó valor informado é inválido.")"Operação falhou! Ó valor informado é inválido.")

 elif opcao == "s":"s":
 valor = flutuação (entrada ("Informe o valor do saque:"))"Informe o valor do saque:"))

 excedeu_saldo = valor > saldo

 excedeu_limite = valor > limite

 excedeu_saques = numero_saques >= LIMITE_SAQUES

 se excedeu_saldo:
 imprimir ("Operação falhou! Você não tem saldo suficiente.")"Operação falhou! Você não tem saldo suficiente.")

 elif excedeu_limite:
 imprimir ("Operação falhou! Ó valor do saque exceda o limite.")"Operação falhou! Ó valor do saque exceda o limite.")

 elif excedeu_saques:
 imprimir ("Operação falhou! Número Máximo de Saques Excedido.")"Operação falhou! Número Máximo de Saques Excedido.")

 valor Elif > 0:0:
 saldo -= valor
 extrato += f "Saque: R$ {valor:.2f}\n""Saque: R$ {valor:.2f}\n"
 numero_saques += 11

 outro:
 imprimir ("Operação falhou! Ó valor informado é inválido.")"Operação falhou! Ó valor informado é inválido.")

 elif opcao == "e":"e":
 imprimir ("\n================ EXTRATO ======")"\n================ EXTRATO ======")
 imprimir ("Não foram realizações movimentos" se não extra outra extra extra)"Não foram realizações movimentos" se não extra outra extra extra extra extra extra)
 imprimir (f"\nSaldo: R$ {saldo:.2f}")"\nSaldo: R$ {saldo:.2f}")
 imprimir ("===========

 elif opcao == "q":"q":
 quebrar

 outro:
 imprimir
