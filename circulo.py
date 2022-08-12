class Circulo:


 PI = 3.14

    #
    #
    # @staticmethod
    # def obter_pi():
    #     return 3.14
#
# Conhecemos nessa aula os métodos estáticos que podem ser chamados a partir da classe
# , sem ter um objeto criado. No exemplo abaixo criamos uma classe Circulo que possui um método estático obter_pi():

# E agora podemos usar esse método estático a partir da classe:
#
# Testando no Python console:
#
# import sys; print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['C:\\Users\\Yuri Prata\\PycharmProjects\\pythonObjectOrientedProgramming', 'C:/Users/Yuri Prata/PycharmProjects/pythonObjectOrientedProgramming'])
# PyDev console: starting.
# Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
# from circulo import Circulo
# Circulo.obter_pi()
# 3.14

# Repare que o método existe apenas para devolver o valor do PI.
# Nada errado com isso, mas já que usamos um valor simples não bastaria
# usar um atributo simples? Em outras palavras, será que é preciso criar um método?
# A resposta é não pois podemos usar um atributo da classe. Veja como é simples:
#
# class Circulo:
#
#     PI = 3.14

# Repare que não usamos self e o atributo nem foi definido dentro do __init__.
# O atributo faz parte da classe, ou seja, é um atributo estático que pode ser usado
# sem ter criado um objeto. Veja como fica simples:
#
# Circulo.PI
# 3.14

# Tudo bem?

# Testando atributo statico

# import sys; print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['C:\\Users\\Yuri Prata\\PycharmProjects\\pythonObjectOrientedProgramming', 'C:/Users/Yuri Prata/PycharmProjects/pythonObjectOrientedProgramming'])
# PyDev console: starting.
# Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
# from circulo import Circulo
# Circulo.PI
# 3.14
