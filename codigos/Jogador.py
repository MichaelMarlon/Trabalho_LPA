from tkinter.font import Font

import pygame.key

from codigos.Constantes import VEL_ENTIDADE, TELA_ALTURA, TELA_LARGURA, JOGADOR_BAIXO, JOGADOR_CIMA, JOGADOR_ESQUERDA, \
    JOGADOR_DIREITA, JOGADOR_TIRO, ATRASO_ENTIDADE_TIRO
from codigos.Entidade import Entidade
from codigos.TiroJogador import TiroJogador


class Jogador(Entidade):

    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)
        self.atraso_tiro = ATRASO_ENTIDADE_TIRO[self.nome]

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

    def tiro(self):
        self.atraso_tiro -= 1
        if self.atraso_tiro == 0:
            self.atraso_tiro = ATRASO_ENTIDADE_TIRO[self.nome]
            pressionada = pygame.key.get_pressed()
            if pressionada[JOGADOR_TIRO[self.nome]]:
                return TiroJogador(nome=f'Tiro{self.nome}',posicao=(self.rect.centerx,self.rect.centery))



















