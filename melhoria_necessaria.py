# Melhoria necessária
#
# Fernanda criou a classe Jogo com o método incrementa() que,
# ao ser chamado, atualizará o valor do atributo self.contador:

class Jogo:

    def __init__(self):
        print("Construindo objeto... {}".format(self))
        self.contador = 0

    def incrementa(self):
        self.contador += 1

jogo = Jogo()
jogo.incrementa()
print(jogo.contador)

#Então, ela realizou sem sucesso o seguinte teste:



#Marque a opção que possui o código de Fernanda corrigido para que o seu teste funcione.