# ESSE ARQUIVO SERÁ A PÁGINA INICIAL DO JOGO
import pygame

# INICIANDO O PYGAME
pygame.init()

# DEFINIÇÕES DO TAMANHO DA TELA
_SCREEN_WIDTH = 640
_SCREEN_HEIGHT = 480

# CARREGANDO IMAGEM DO PERSONAGEM, PEGANDO O RETÂNGULO DA IMAGEM DO PERSONAGEM E DEFININDO POSICIONAMENTO
# DA IMAGEM NO EIXO X E Y.
personagem=pygame.image.load('img/personagem_teste.png')
personagem_rect=personagem.get_rect()
personagem_rect.x=0
personagem_rect.y=400

# FUNÇÃO DO MOVIMENTO DO PERSONAGEM
def moves (keys, personagem_rect):
    if keys[pygame.K_LEFT]:
        personagem_rect.x-=20
        if personagem_rect.x<0:
          personagem_rect.x=0
    if keys[pygame.K_RIGHT]:
        personagem_rect.x+=20
        if personagem_rect.x>595:
          personagem_rect.x=595
    if keys[pygame.K_UP]:
        personagem_rect.y-=30
        if personagem_rect.y<0:
          personagem_rect.y=0
    if keys[pygame.K_DOWN]:
        personagem_rect.y+=30
        if personagem_rect.y>400:
          personagem_rect.y=400

#FUNÇÃO PARA ORGANIZAR OS BLOCOS SOBRE O BACKGROUND
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

while True:
    # PEGANDO AS TECLAS PRESSIONADAS
    keys = pygame.key.get_pressed()

    #  CARREGANDO JANELA DE EXIBIÇÃO
	## Estrutura da janela principal
    displayBackground = pygame.display
    displayBackground.set_caption('Nome do Jogo')

    ## INICIALIZANDO A JANELA DE EXIBIÇÃO
    displayRun = displayBackground.set_mode([_SCREEN_WIDTH, _SCREEN_HEIGHT])

    ## SETANDO IMAGEM DO FUNDO
    displayRun.blit(pygame.image.load('img/background_02.png'), (0, 0))

    # SETANDO IMAGEM DO PERSONAGEM COM OS PARÂMETROS DO SEU RETÂNGULO
    displayRun.blit(personagem, personagem_rect)

    # CHAMANDO A FUNÇÃO DOS MOVIMENTOS DO PERSONAGEM
    moves(keys,personagem_rect)

    pygame.display.flip()
