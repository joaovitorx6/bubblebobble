# ESSE ARQUIVO SERÁ A PÁGINA INICIAL DO JOGO
import pygame

pygame.init()

_SCREEN_WIDTH = 640
_SCREEN_HEIGHT = 480

while True:
    #  CARREGANDO JANELA DE EXIBIÇÃO
	## Estrutura da janela principal
    displayBackground = pygame.display
    displayBackground.set_caption('Nome do Jogo')

    ## INICIALIZANDO A JANELA DE EXIBIÇÃO
    displayRun = displayBackground.set_mode([_SCREEN_WIDTH, _SCREEN_HEIGHT])

    ## SETANDO IMAGEM DO FUNDO
    displayRun.blit(pygame.image.load('img/background_02.png'), (0, 0))

    ##FUNÇÃO PARA ORGANIZAR OS BLOCOS SOBRE O BACKGROUND
    def block (x_block,y_block,qtd_block,eixo):
        if eixo=='x':
            qtd_block=(qtd_block*20)+x_block
            while x_block<=qtd_block:
                block = pygame.image.load('img/blocks_02.png')
                displayRun.blit(block,(x_block,y_block))
                x_block+=20
        elif eixo=='y':
            qtd_block=(qtd_block*20)+y_block
            while y_block<=qtd_block:
                block = pygame.image.load('img/blocks_02.png')
                displayRun.blit(block,(x_block,y_block))
                y_block+=20

    block(0,0,20,'y')
    pygame.display.flip()
