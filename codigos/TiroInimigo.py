from codigos.Constantes import VEL_ENTIDADE
from codigos.Entidade import Entidade


class TiroInimigo(Entidade):
    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)

    def move(self):
        self.rect.centery += VEL_ENTIDADE[self.nome]