import pygame
from pygame.locals import *

class windowLost1player:
    def __init__(self, username1, username2, vidas, puntos):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas = vidas
        self.puntos = puntos

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas, vas a comenzar el mismo nivel!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)
        self.red_label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Usuario\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            from Niveles import nivel1
                            juego=nivel1(self.player1, self.player2, self.vidas, self.puntos, None, None)
                            juego.run()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel1
                        juego=nivel1(self.player1, self.player2, self.vidas, self.puntos, None, None)
                        juego.run()

            # Dibuja la imagen de fondo
            self.pantalla.blit(self.fondo, (0, 0))

            self.draw_text_inputs()
            self.draw_ready_button()
            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs(self):
        # Renderizar las etiquetas
        label_surface = self.font.render(self.label, True, self.label_color)
        self.pantalla.blit(label_surface, (110, 250))


    def draw_ready_button(self):
        # Crea el botón en el centro de la ventana
        self.ready_button = pygame.Rect(350 , self.height // 2 , 100, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ready_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ready!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ready_button.center)
        self.pantalla.blit(text_surface, text_rect)

##################################################################################################################
##################################################################################################################
class windowLost2players:
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas_player1 = vidas_player1
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = vidas_player2
        self.puntos_player2 = puntos_player2

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Usuario\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            from Niveles import nivel1
                            juego=nivel1(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1)
                            juego.run()
                            print("se presionó ready")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel1
                        juego=nivel1(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1)
                        juego.run()

            self.pantalla.blit(self.fondo, (0,0))
            self.draw_text_inputs1()
            self.draw_text_inputs2()
            self.draw_ready_button()
            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs1(self):
        # Renderizar las etiquetas
        label_surface = self.font.render(self.label, True, self.label_color)
        self.pantalla.blit(label_surface, (100, 250))

    def draw_text_inputs2(self):
        # Define el mensaje que quieres mostrar
        self.label2 = '¡Ahora es turno de '+ self.player2 + '!'
        
        # Renderiza la etiqueta
        label_surface2 = self.font.render(self.label2, True, self.label_color)
        
        # Coloca la etiqueta en la posición que desees. En este caso, la he puesto en (200, 400)
        self.pantalla.blit(label_surface2, (100, 400))



    def draw_ready_button(self):
        # Crea el botón en el centro de la ventana
        self.ready_button = pygame.Rect(350 , self.height // 2 , 100, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ready_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ready!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ready_button.center)
        self.pantalla.blit(text_surface, text_rect)