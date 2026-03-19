import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.jpg')# variavel para carregar a imagem
        self.rect = self.surf.get_rect(left=0, top=0)# criando o retangulo dentro da janela
    def run(self):
        # metodo blit usado para desenhar a imagem dentro do retangulo
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()# metodo para atualizar a janela
        pass