import pygame
pygame.init()
tamanho  = ( 800, 600)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("IronMan ME")
branco = (255,255,255)
preto = (0,0,0)
posicaoXpersona = 400
posicaoYpersona = 300
movimentoXpersona = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXpersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXpersona = -5    
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXpersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXpersona = 0

        
    posicaoXpersona = posicaoXpersona + movimentoXpersona

    tela.fill(branco)
    pygame.draw.circle(tela, preto, (posicaoXpersona,posicaoYpersona), 40, 0)

    pygame.display.update()
    clock.tick(60)

pygame.quit()