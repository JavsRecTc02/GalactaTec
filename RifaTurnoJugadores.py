import pygame
from pygame.locals import *
import random

from Niveles import nivel1

class rifaWindow:
    def __init__(self, username1, username2):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Rifa de jugadores")
        self.user1 = username1
        self.user2 =  username2

        #Se realiza la rifa aleatoria de cual de los 2 jugadores tiene el primer turno
        if random.randint(1, 2) == 1:
            self.winner = self.user1
            self.loser = self.user2
        else:
            self.winner = self.user2
            self.loser = self.user1

        self.label = "El jugador " + self.winner + " iniciará la partida"

        self.red_label = "ACLARACION: Se esta tomando como usuario2 default una cuenta ya registrada"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (0, 0, 0)
        self.red_label_color = (255, 0, 0)  # Color rojo para el nuevo texto

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            print("se presionó")
                            niveles_window = nivel1(self.winner, self.loser)
                            niveles_window.run()

            self.pantalla.fill((255,255,255))
            self.draw_text_inputs()
            self.draw_ready_button()
            self.draw_red_text()
            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs(self):
        # Renderizar las etiquetas
        label_surface = self.font.render(self.label, True, self.label_color)
        self.pantalla.blit(label_surface, (250, 300))

    def draw_red_text(self):
        # Renderizar el nuevo texto
        red_label_surface = self.font.render(self.red_label, True, self.red_label_color)
        self.pantalla.blit(red_label_surface, (100, 100)) 

    def draw_ready_button(self):
        # Crea el botón en el centro de la ventana
        self.ready_button = pygame.Rect(self.width // 2 - 50, self.height // 2 + 200, 100, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ready_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ready!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ready_button.center)
        self.pantalla.blit(text_surface, text_rect)
