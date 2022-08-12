# O problema de Chalita
#
# Chalita decidiu aplicar o que aprendeu na aula sobre método em Python.
# Ele criou a classe Pessoa que recebe em seu "construtor" um nome e sobrenome
# e que declara o único método exibe_nome_e_sobrenome(). Vejamos o código que ele escreveu:


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def exibe_nome_e_sobrenome(self):

        print("{0} {1}".format(self.nome, self.sobrenome))




pessoa = Pessoa("Chalita", "Steppat")
pessoa.exibe_nome_e_sobrenome()

#O codigo tinha 2 erros Chalita não declarou o método com def, muito menos recebeu self como parâmetro.