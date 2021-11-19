import os
import sys
import pygame
from pygame import rect  
from pygame.locals import*
class Gelatina(pygame.sprite.Sprite): 
    def __init__(self,imagem):
        pygame.sprite.Sprite.__init__(self)
        self.pos_y_inicial= alt-105 #referencia        
        self.pulo=False
        self.image=imagem 
        self.image=pygame.transform.scale(imagem, (120,100))
        self.rect=self.image.get_rect()
        self.rect.center=(30,30)
        self.rect.x=-20
        
    def pular (self): 
        self.pulo=True

    def update (self): 
        if self.pulo==True: 
            if self.rect.y<=390:
                self.pulo= False 
            self.rect.y-=5
        else: 
            if self.rect.y<self.pos_y_inicial: 
                self.rect.y+=5
            else: 
                self.rect.y=self.pos_y_inicial  
        if self.rect.right> larg: 
            self.rect.right=larg+10
        if self.rect.left <0: 
            self.rect.left=-20
class Chao(pygame.sprite.Sprite): 
    def __init__(self, posicao_x, imagem): 
        pygame.sprite.Sprite.__init__(self)
        self.image= imagem
        self.image=pygame.transform.scale(self.image, (500,100))
        self.rect=self.image.get_rect()
        self.rect.y=alt-75
        self.rect.x=0#posicao_x
    def update(self): 
        if  self.rect.topright[0]<0: 
            self.rect.x=larg
        #self.rect.x-=5 #velocidade

pygame.init()
#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)

#dimensões
larg=500
alt=600
#permite acesso as fotos na pasta imagens 
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")

tela=pygame.display.set_mode((larg, alt)) #criando a tela principal
image_geleia= pygame.image.load(os.path.join(direct_imag, "geleia.png" )).convert_alpha()
pygame.display.set_caption('Gelatin Jumping')
imagem_fundo=pygame.image.load('fundo.jpg').convert() #criando a imagem de fundo
imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
imagem_chao=pygame.image.load(os.path.join(direct_imag, "chao.png")).convert_alpha()
clock=pygame.time.Clock() #velocidade de processamento
todas =pygame.sprite.Group()
gelatina=Gelatina(image_geleia)
todas.add(gelatina)
#criando movimentação no chão 

chao=Chao(100,imagem_chao)
todas.add(chao)
#Loop principal
while True:
    delta_time=clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado
    for event in eventos: 
        if event.type==pygame.QUIT:
            pygame.quit() #permitindo que se feche a janela
            sys.exit()
            # permitindo movimentação pelo teclado
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                gelatina.rect.x+=30     
            if event.key==pygame.K_LEFT:
                gelatina.rect.x-=30
            if event.key==pygame.K_SPACE: 
                gelatina.pular()
    #movimenta a geleia caso a tecla fique pressionada
    if pygame.key.get_pressed()[K_RIGHT]: 
        gelatina.rect.x+=5 
    if pygame.key.get_pressed()[K_LEFT]: 
        gelatina.rect.x-=5
    tela.blit(imagem_fundo, (0,0))
    todas.draw(tela)
    pygame.display.update() 
    todas.update()
    

    pygame.display.flip() #faz a atualização da tela 