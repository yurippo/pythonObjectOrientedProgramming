#eu criei uma funcao para criar uma conta

def cria_conta(numero,titular,saldo,limite):

    conta = {"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}

    return conta

#se eu executar essa funcao ela vai criar uma conta para mim
#com isso agente consegue agrupar nossos dados e encapsula-los em uma funcao


#cria a funcao depositar que deposita um valor em uma conta
def deposita(conta,valor):

    conta["saldo"] += valor  # para incrementar ou podemos usar conta["saldo"] + valor forma mais cumprida


#cria a funcao sacar que saca um valor em uma conta
def saca(conta,valor):

    conta["saldo"] -= valor  # para decrementar ou podemos usar conta["saldo"] - valor forma mais cumprida

#cria a funcao extrato que imprime informacao so vamos imprimir saldo nesse caso

def extrato (conta):
    print("Saldo: {}".format(conta["saldo"]))


#Para Testar
# No Python Console, dentro do próprio PyCharm, teste o código, crie uma conta, deposite um valor,
# visualize o extrato com o saldo incrementado, saque um valor e visualize o extrato com o saldo decrementado,
# por exemplo:
#
# >>> from teste import cria_conta, deposita, saca, extrato
# >>> conta = cria_conta(123, "Nico", 55.0, 1000.0)
# >>> deposita(conta, 300.0)
# >>> extrato(conta)
# Saldo 355.0
# >>> saca(conta, 100.0)
# >>> extrato(conta)
# Saldo 255.0


# Nesta aula, revisamos:
#
# Dicionário
# Funções
# Encapsulamento de código
