import self as self

import conta


class Conta:

#essa eh chamada uma funcao construtora chamada automaticamente no Python na hora de construir o objeto

    def __init__(self,numero,titular,saldo,limite):
     print("Construindo objeto... {}".format(self))
     self.__numero = numero
     self.__titular = titular
     self.__saldo = saldo
     self.__limite = limite


    def extrato(self):
     print("Saldo do {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
     self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar): #esse eh um exemplo de metodo privado assim como o atributo pode ser privado o metodo tbm usando __ na frente
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar


    def saca(self,valor):
     if (self.__pode_sacar(valor)):
      self.__saldo -= valor
     else:
      print("O valor {} passou o limite".format(valor))


    def transfere(self,valor,destino):
     self.saca(valor)
     destino.deposita(valor)

    @property
    def saldo(self):
     return self.__saldo

    @property
    def titular(self):
     return self.__titular

    def get_numero(self):
     return self.__numero

    @property #transformando get_limite limite em anotation e nao preciso mais usar () para chamar o metodo vai chamar por baixo dos panos
    def limite(self):
     return self.__limite

    @limite.setter #transformando set_limite limite em setter anotation e nao preciso mais usar () para chamar o metodo vai chamar por baixo dos panos e settar
    def limite(self,limite):
     self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos(): #isso eh um exemplo de um metodo estatico isto eh da classe chamo ele sem uma referencia nao eh o objeto que chama eh a classe eh o static method todas as linguagens OO tem
        return {"BB":"001","Caixa":"104","Bradesco":"237"}



#
# No Python Console, dentro do próprio PyCharm, teste o código,
# crie duas contas e transfira um valor de uma conta para outra,
# visualizando os seus extratos em seguida, por exemplo:

# >>> from conta import Conta
# >>> conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x7f82af89d048>
# >>> conta2 = Conta(321, "Marcos", 100.0, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x7f82af89d400>
# >>> conta.transfere(10.0, conta2)
# >>> conta.extrato()
# Saldo de 45.5 do titular Nico
# >>> conta2.extrato()
# Saldo de 110.0 do titular Marcos

# O que aprendemos?
#
# Nesta aula, aprendemos:
#
# Métodos, que definem o comportamento de uma classe
# Criação de métodos
# Como chamar métodos através do objeto
# Acesso aos atributos através do self
# Garbage Collector
# O tipo None

# Solid
# Falamos nessa aula sobre a coesão que é ligado ao principio de responsabilidade única. Aprendemos que
# uma classe deve ter apenas uma responsabilidade (ou deve ter apenas uma razão para existir). Em outras palavras,
# ela não deve assumir responsabilidades que não são delas.
#
# Além desse princípio de responsabilidade única existem outras que foram definidos através do Robert C. Martin no início
# dos anos 2000 e são conhecidos pelo acrônimo SOLID:
#
# S - Single responsibility principle
# O - Open/closed principle
# L - Liskov substitution principle
# I - Interface segregation principle
# D - Dependency inversion principle
# Na Alura temos cursos específicos sobre o SOLID, mas fique tranquilo, na medida que você avança no mundo OO esses princípios
# ficam mais claros e fáceis de se entender.
#
# O que aprendemos?
#
# Nesta aula, aprendemos:
#
# Atributos privados
# Encapsulamento de código
# Encapsulamento da manipulação dos atributos nos métodos
# Coesão do código


#Testando os @properties getters and setters chammando getter and setter com sintaxe amigavel e por baixo dos panos
#
# PyDev console: starting.
# Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
# from conta import Conta
# conta = Conta(123,"Nico",55.5,1000.0)
# Construindo objeto... <conta.Conta object at 0x00000210CF898E50>
# conta.limite
# 1000.0
# conta.limite = 2000.0
# conta.limite
# 2000.0

# Já vimos que podemos criar getters e setters para acessar e alterar o valor de atributos privados.
# No python existe uma forma mais comum de criar estes getters e setters, diferente de Java, onde se coloca
# get ou set como prefixo de um método, usamos Propriedades.
#Exemplo
#@property
# def nome(self):
#     return self.__nome
# E se quisermos alterar os atributos através de uma propriedade, o jeito correto de fazer e
#Exemplo
# @nome.setter
# def nome(self, nome):
#     self.__nome = nome
#
# Nesta aula, aprendemos:
#
# Métodos de leitura dos atributos, os getters
# Métodos de modifição dos atributos, os setters
# Propriedades
