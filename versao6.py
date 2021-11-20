#importa bibliotecas
import pygame

#inicializa pygame
pygame.init()

#dimensões de tela
TELA_WIDTH = 600  #largura
TELA_HEIGHT = 600  #altura

#velocidade
clock = pygame.time.Clock()
FPS = 6   #frames por segundo

# variaveis do jogo
GRAVIDADE = 100 #100 #gelatina cair depois de pular

#cria janela do jogo
screen = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))
pygame.display.set_caption('Jelly')

#cores
BRANCO = (255,255,255)

#carrega as imagens
imagem_gelatina = pygame.image.load('imagens/geleia.png').convert_alpha()
imagem_fundo = pygame.image.load('imagens/fundo.jpg').convert_alpha()

#classes
class Gelatina():
    def __init__(self, x , y):
        self.image = pygame.transform.scale(imagem_gelatina , (160,120))
        self.width = 110
        self.height = 100
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = (x,y)
        self.vel_y = 0  #velocidade na direção y
    def move(self):
        #reseta a variavel da posicao
        delta_x = 0  # mudança da coordenada x
        delta_y = 0  #mudança da coordenada y

        #processa os apertos dos botões
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            delta_x = -150   #mudar esse numero se quiser que ela ande mais ou menos rápido
        if key[pygame.K_RIGHT]:
            delta_x =  150   #mudar esse numero se quiser que ela ande mais ou menos rápido
                
        #gravidade
        self.vel_y += GRAVIDADE 
        delta_y += self.vel_y

        #checa se a gelatina não sai da tela
        if self.rect.left + delta_x < 0:
            delta_x =  - self.rect.left
        if self.rect.right + delta_x > TELA_WIDTH:
            delta_x = TELA_WIDTH - self.rect.right
        
        #checa colisão com o chão/ nao deixa a gelatina passar a tela
        if self.rect.bottom + delta_y > TELA_HEIGHT:
            delta_y = 0 
            self.vel_y = -200 #200 #determina intensidade que ela quica do chão 

        #atualiza a posição do retangulo (gelatina)
        self.rect.x += delta_x
        self.rect.y += delta_y


    def draw(self):
        screen.blit(self.image, (self.rect.x - 30 ,self.rect.y - 5))
        pygame.draw.rect(screen, BRANCO , self.rect, 2)

gelatina = Gelatina(TELA_WIDTH // 2, TELA_HEIGHT - 150) #MUDAR A HEIGHT


#loop do jogo
run = True
while run:
    
    clock.tick(FPS)

    gelatina.move()

    #background
    screen.blit(imagem_fundo, (0,0))

    #sprites
    gelatina.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    #atualiza tela de display
    pygame.display.update()
pygame.quit() 