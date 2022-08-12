class Data:

    def __init__(self,dia,mes,ano):
     print("Construindo objeto... {}".format(self))
     self.dia = dia
     self.mes = mes
     self.ano = ano

#nova funcao def formatada()
    def formatada(self):
     print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")

#     def formatada(self):
#         print(f"{self.dia}/{self.mes}/{self.ano}")
# #yaay! Meu codigo funciona ;) codigo anterior

d = Data(21,11,2007)

d.formatada()


# Você não precisa fazer este exercício para continuar no treinamento, mas é bom praticar, certo?
#
# Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar.
# Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada. Ela deve funcionar dessa forma:
#
# from datas import Data
# d = Data(21,11,2007)
# d.formatada()
#
# Imprime:
#
# 21/11/2007

# Crie e implemente essa classe dentro de uma arquivo datas.py. Mãos à obra!