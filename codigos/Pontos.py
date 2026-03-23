from datetime import datetime
from time import strftime

import pygame
from pygame import Surface, Rect
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE
from pygame.font import Font

from codigos.Constantes import COR_AMARELA, PONTUACAO_POSICAO, COR_VERDE, MENU_OPCAO, COR_BRANCA, COR_PRETA
from codigos.DBProxy import DBProxy


class Pontos:
    def __init__(self,window:Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Pontos.png')  # variavel para carregar a imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # criando o retangulo dentro da janela

    def salvar(self,modo_jogo:str, pontos_jogadores:list[int]):
        pygame.mixer_music.load('./asset/Pontos.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBPontos')
        nome = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.texto_pontos(48,'VOCÊ GANHOU!!',COR_VERDE,PONTUACAO_POSICAO['Título'])
            if modo_jogo == MENU_OPCAO[0]:
                pontos = pontos_jogadores[0]
                texto = 'Jogador1 informe o seu nome (4 caracteres):'
            if modo_jogo == MENU_OPCAO[1]:
                if pontos_jogadores[0] >= pontos_jogadores[1]:
                    pontos = pontos_jogadores[0]
                    texto = 'Jogador1 informe o seu nome (4 caracteres):'
                else:
                    pontos = pontos_jogadores[1]
                    texto = 'Jogador2 informe o seu nome (4 caracteres):'
            self.texto_pontos(30,texto,COR_PRETA,PONTUACAO_POSICAO['DigiteNome'])
            for event in pygame.event.get():
                # Evento de saida
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN and len(nome) == 4:
                        db_proxy.salvar({'nome':nome,'pontos':pontos,'data': pegar_data()})
                    elif event.key == K_BACKSPACE:
                        pass
                    else:
                        if len(nome) < 4:
                            nome += event.unicode


            pygame.display.flip()
            pass


    def mostrar(self):
        pygame.mixer_music.load('./asset/Pontos.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def texto_pontos(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf,dest=text_rect)


def pegar_data():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime,strftime("d/%m/%y")
    return f'{current_time} - {current_date}'














