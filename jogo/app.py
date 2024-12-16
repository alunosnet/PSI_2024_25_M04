import pygame
import random

pygame.init()

#definir a janela
largura = 800
altura  = 600
tamanho = (largura,altura)
titulo  = "Primeiro Jogo"

#criar a janela
janela = pygame.display.set_mode(tamanho)
pygame.display.set_caption(titulo)
cor_fundo = (36, 36, 36)

#Assets
#player
player_ficheiro    = "imagens\\aviao.png"
player_velocidadex = 1
player_velocidadey = 1
player_imagem = pygame.image.load(player_ficheiro)
player_rect = player_imagem.get_rect()
player_rect.topleft = (400,300)

#texto de game over
font = pygame.font.SysFont("arial",40)
texto = font.render("Game Over",True,(255,255,255))

#npc
npc_ficheiro     = "imagens\\npc.png"
npc_velocidadex  = 1
npc_velocidadey  = 1
npc_imagem       = pygame.image.load(npc_ficheiro)
npc_rect         = npc_imagem.get_rect()
npc_rect.topleft = (400,50)

relogio = pygame.time.Clock()

player_estado = True    #player vivo
run = True
#Game Loop
while run:
    if player_estado == False:
        player_velocidadex = 0
        player_velocidadey = 0
    #atualizar as posições
    player_rect = player_rect.move(player_velocidadex,player_velocidadey)
    #atualizar a posição do npc
    if player_rect.left > npc_rect.left:
        npc_velocidadex = 1
    else:
        npc_velocidadex = -1
    if npc_rect.bottom > altura:
        npc_rect.top = 0
        npc_rect.left = random.randint(10,790-npc_rect.width)

    npc_rect = npc_rect.move(npc_velocidadex,npc_velocidadey)
    #limpar a janela com a cor de fundo
    janela.fill(cor_fundo)
    #desenhar player
    janela.blit(player_imagem,player_rect)
    #desenhar npc
    janela.blit(npc_imagem,npc_rect)

    #testar limites da janela
    if player_rect.left < 0 or player_rect.top < 0 or player_rect.right > largura or player_rect.bottom > altura:
        #game over
        player_estado = False

    if player_estado == False:
        janela.blit(texto,(50,50))
        
    #atualizar a janela
    pygame.display.flip()

    relogio.tick(60)
    #verificar colisões
    if player_rect.colliderect(npc_rect):
        player_estado = False
    #eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            run = False
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player_velocidadex = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                player_velocidadey = 0
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                run = False
            #tecla para a esquerda
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                player_velocidadex = -1
            #tecla para a direita
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                player_velocidadex = 1
            #tecla para a cima
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                player_velocidadey = -1
            #tecla para baixo
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                player_velocidadey = 1

