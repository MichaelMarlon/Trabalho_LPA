from codigos.Entidade import Entidade


class Fundo(Entidade):

    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)

    def move(self):
        pass