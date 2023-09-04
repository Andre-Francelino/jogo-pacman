import pygame
import constantes
import sprites
import os

class Game:
    def __init__(self):
        #criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()
    
    def novo_jogo(self):
        # Esse método instancia as classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()
        
    def rodar(self):
        # Esse método inicia o Loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()
    
    def eventos(self):
        # Esse método define os eventos no jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False
    
    def atualizar_sprites(self):
        # Esse método controla a atualização das sprites
        self.todas_as_sprites.update()
    
    def desenhar_sprites(self):
        # Esse método é responsável pelo desenho das sprites
        self.tela.fill(constantes.PRETO)        #limpando a tela
        self.todas_as_sprites.draw(self.tela)   #desenhando as sprites
        pygame.display.flip()
    
    def carregar_arquivos(self):
        # Esse método irá carregar os arquivos de audio e imagens
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        self.spritesheet = os.path.join(diretorio_imagens, constantes.SPRITESHEET)
        self.pacman_start_logo = os.path.join(diretorio_imagens, constantes.PACMAN_START_LOGO)
        self.pacman_start_logo = pygame.image.load(self.pacman_start_logo).convert()
        
    def mostrar_texto(self, texto, tamanho, cor, x, y):
        # Método exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)
    
    def mostrar_tela_start(self):
        self.mostrar_texto(
            '-Pressione uma tecla para jogar',
            32,
            constantes.AMARELO,
            constantes.LARGURA / 2,
            320
        )
        
        pygame.display.flip()
        self.esperar_por_jogador()
    
    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                
    def mostrar_tela_game_over(self):
        pass
    
g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()