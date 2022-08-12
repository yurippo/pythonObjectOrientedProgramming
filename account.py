class Account:

    def __init__(self, numero, saldo, limite):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0

    # NOVO MÉTODO AQUI
    def __temSaldoDisponivelPara(self, valor):
        return valor < (self.__saldo + self.__limite)

    def saca(self, valor):

        if self.__temSaldoDisponivelPara(valor):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")

    def deposita(self, valor):
      self.__saldo += valor


    def transfere(self, valor, destino):

        valorTotal = valor + self.__tarifaTransferencia

        if self.__temSaldoDisponivelPara(valorTotal):

          self.__saldo -= valorTotal
          self.saca(valor)
          self.deposita(valor)

          print("Transferência efetuada.")
        else:
            print("Saldo insuficiente.")


    # Como líder técnico da empresa, você precisa
    # inspecionar as modificaçõesv que  Paulo fez
    # na classe anterior e ajudá - lo no  desenvolvimento
    # profissional. Analise o código do Paulo




    #codigo anterior sem a nova implementacao

    # def __init__(self, numero, saldo, limite):
    #     self.__numero = numero
    #     self.__saldo = saldo
    #     self.__limite = limite
    #     self.__tarifaTransferencia = 8.0
    #
    # def saca(self, valor):
    #
    #     if valor < (self.__saldo + self.__limite):
    #         self.__saldo -= valor
    #         print("Saque efetuado.")
    #     else:
    #         print("Saldo insuficiente.")
    #
    # def transfere(self, valor, destino):
    #
    #     valorTotal = valor + self.__tarifaTransferencia
    #
    # if valorTotal < (self.__saldo + self.__limite):
    #
    #     self.__saldo -= valorTotal
    #     destino.deposita(valor)
    #
    #     print("Transferência efetuada.")
    # else:
    #     print("Saldo insuficiente.")

    #codigo anterior
    # outros métodos omitidos...



