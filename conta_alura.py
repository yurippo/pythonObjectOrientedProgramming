class ContaAlura:


    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

# Imagine que uma conta bancária no banco AluraInvest geralmente
# é criada com limite de mil reais.

# Como podemos fazer no Python para economizar a escrita do código de
# criação de um objeto Conta? Neste caso podemos supor que apenas as
# contas com limites especiais precisariam passar tal argumento
# (no exemplo acima apenas conta3 tem um limite especial).
# Isso é feito colocando na declaração da função construtora __init__ um valor
# padrão para o limite.

#E o código de nossos 3 objetos ficaria assim:
#
# conta_alura = ContaAlura(1, "Fulano", 0.0)
# conta_alura2 = ContaAlura(2, "Beltrano", 0.0)
# conta_alura3 = ContaAlura(3, "Sicrano", 0.0, 2000.0)



