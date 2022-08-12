
class Cliente:

    def __init__(self,nome):
        print("Construindo objeto... {}".format(self))
        self.__nome = nome #para o @property funcionar o atributo tem que estar privado __nome se nao nao funciona

    @property #aqui se trata de uma propriedade nao preciso colocar () no metodo e ele executa o metodo por baixo dos panos
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        print("Chamando setter nome()")
        self.__nome = nome



# Testando @property nome() getter
# cliente = Cliente("nico")
# Construindo objeto... <cliente.Cliente object at 0x000001DA39328D60>
# Chamando @property nome()
# Chamando @property nome()
# cliente.nome
# Chamando @property nome()
# 'Nico'

# Testando setter and getter depois tbm
#
# cliente = Cliente("nico")
# Construindo objeto... <cliente.Cliente object at 0x000001ADD083D540>
# Chamando @property nome()
# cliente.nome = "marco"
# Chamando setter nome()
# Chamando @property nome()
# cliente.nome
# Chamando @property nome()
# 'Marco'



