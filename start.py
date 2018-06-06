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

	fontOS_start = pygame.font.SysFont('Verdana', 30, True)
	fontOS_about = pygame.font.SysFont('Verdana', 24, True)
	fontOS_exit = pygame.font.SysFont('Verdana', 20, True)

	textStart = fontOS_start.render('Start', True, (255, 255, 255))
	textAbout = fontOS_about.render('About', True, (255, 255, 255))
	textExit = fontOS_exit.render('Exit', True, (255, 255, 255))

	textArray = [textStart, textAbout, textExit]
	texPosition = 175
	for x in range(len(textArray)):
		fontPosition = textArray[x].get_rect(center = (_SCREEN_WIDTH / 2, texPosition))
		displayRun.blit(textArray[x], fontPosition)
		texPosition += 50
		pass


	# MÉTODO get_pressed PARA CAPTURAR TECLAS PRESSIONADAS
	keys = pygame.key.get_pressed()



	pygame.display.flip()


	#Fechar a janela com ESC
	if keys[pygame.K_ESCAPE]:
		pygame.quit()
		break

	mpos = pygame.mouse.get_pos()
	#print(mpos)
	print(textAbout.get_rect())
