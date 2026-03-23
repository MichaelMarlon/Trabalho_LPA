from codigos.Constantes import VEL_ENTIDADE, ATRASO_ENTIDADE_TIRO
from codigos.Entidade import Entidade
from codigos.TiroInimigo import TiroInimigo


class Inimigo(Entidade):

    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)
        self.atraso_tiro = ATRASO_ENTIDADE_TIRO[self.nome]
    def move(self):
        self.rect.centery += VEL_ENTIDADE[self.nome]

    def tiro(self):
        self.atraso_tiro -= 1
        if self.atraso_tiro == 0:
            self.atraso_tiro = ATRASO_ENTIDADE_TIRO[self.nome]
            return TiroInimigo(nome=f'Tiro{self.nome}', posicao=(self.rect.centerx, self.rect.centery))

