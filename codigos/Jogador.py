import pygame.key

from codigos.Constantes import VEL_ENTIDADE, TELA_ALTURA, TELA_LARGURA
from codigos.Entidade import Entidade


class Jogador(Entidade):

    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)

    def move(self,):
        pressionada = pygame.key.get_pressed()
        if pressionada[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= VEL_ENTIDADE[self.nome]
        if pressionada[pygame.K_DOWN] and self.rect.bottom < TELA_ALTURA:
            self.rect.centery += VEL_ENTIDADE[self.nome]
        if pressionada[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= VEL_ENTIDADE[self.nome]
        if pressionada[pygame.K_RIGHT] and self.rect.right < TELA_LARGURA:
            self.rect.centerx += VEL_ENTIDADE[self.nome]
        pass