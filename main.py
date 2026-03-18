import pygame
pygame.init()

windows = pygame.display.set_mode(size=(1000,800))
while True:
    # checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# fechando a janela
            quit()# finalizando pygame