# Classe abstrata que gerará as entidades tanto de jogadores quanto de inimigos
from abc import ABC, abstractmethod

import pygame.image


class Entidade(ABC):
    def __init__(self, nome:str, posicao: tuple):
        self.nome = nome
        #metodo convert_alpha trata a imagem .png de maneira otimizada
        self.surf = pygame.image.load(f'./asset/{nome}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=posicao[0], top=posicao[1])
        self.velocidade = 0

    @abstractmethod
    def move(self):# metodo será implementado nas classes filhas
        pass