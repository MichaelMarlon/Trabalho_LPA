import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codigos.Constantes import TELA_LARGURA, COR_LARANJA, MENU_OPCAO, COR_BRANCA, COR_PRETA


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.jpg')# variavel para carregar a imagem
        self.rect = self.surf.get_rect(left=0, top=0)# criando o retangulo dentro da janela
    def run(self):
        # metodo usado para carregar a música de fundo
        pygame.mixer_music.load('./asset/Menu.mp3')
        # comando para tocar a música - parametro -1 para musica repetir
        pygame.mixer_music.play(-1)
        # loop usado para ficar desenhando o desenho da imagem de opçao de menu
        while True:
            # metodo blit usado para desenhar a  de fundo dentro do retangulo
            self.window.blit(source=self.surf, dest=self.rect)
            # carregando as imagens de texto dentro do retangulo
            self.menu_text(25,'Trabalho Linguagem de Programação Aplicada',(0,0,0),((TELA_LARGURA/2),20))
            self.menu_text(100, 'Space War', (COR_LARANJA), ((TELA_LARGURA / 2), 100))

            # loop para iterar na constante MENU_OPCAO
            for i in range(len(MENU_OPCAO)):
                self.menu_text(35, MENU_OPCAO[i], (COR_PRETA), ((TELA_LARGURA / 2), 250 +50 *i))

            pygame.display.flip()# metodo para atualizar a janela
            # checando todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechando a janela
                    quit()  # finalizando pygame
    # metodo usado para escrever texto no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
