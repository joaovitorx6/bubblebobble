import pygame,sys

pygame.init()


while True:
	#  CARREGANDO JANELA DE EXIBIÇÃO
	## Estrutura da janela principal
	display_background = pygame.display
	display_background.set_caption('Nome do Jogo')

	## INICIALIZANDO A JANELA DE EXIBIÇÃO
	display_run = display_background.set_mode([640, 480])
	## SETANDO IMAGEM DO FUNDO
	display_run.blit(pygame.image.load('img/background_02.png'), (0, 0))
	


	# MÉTODO get_pressed PARA CAPTURAR TECLAS PRESSIONADAS
	keys = pygame.key.get_pressed()



	pygame.display.flip()


	#Fechar a janela com ESC
	if keys[pygame.K_ESCAPE]:
		pygame.quit()
		break