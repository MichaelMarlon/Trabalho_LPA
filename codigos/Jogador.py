import pygame.key

from codigos.Constantes import VEL_ENTIDADE, TELA_ALTURA, TELA_LARGURA, JOGADOR_BAIXO, JOGADOR_CIMA, JOGADOR_ESQUERDA, \
    JOGADOR_DIREITA
from codigos.Entidade import Entidade


class Jogador(Entidade):

    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)

    def move(self,):
        pressionada = pygame.key.get_pressed()
        if pressionada[JOGADOR_CIMA[self.nome]] and self.rect.top > 0:
            self.rect.centery -= VEL_ENTIDADE[self.nome]
        if pressionada[JOGADOR_BAIXO[self.nome]] and self.rect.bottom < TELA_ALTURA:
            self.rect.centery += VEL_ENTIDADE[self.nome]
        if pressionada[JOGADOR_ESQUERDA[self.nome]] and self.rect.left > 0:
            self.rect.centerx -= VEL_ENTIDADE[self.nome]
        if pressionada[JOGADOR_DIREITA[self.nome]] and self.rect.right < TELA_LARGURA:
            self.rect.centerx += VEL_ENTIDADE[self.nome]
        pass