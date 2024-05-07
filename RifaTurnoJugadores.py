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
            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs(self):
        # Renderizar las etiquetas
        label_surface = self.font.render(self.label, True, self.label_color)
        self.pantalla.blit(label_surface, (250, 300))

    def draw_ready_button(self):
        # Crea el botón en el centro de la ventana
        self.ready_button = pygame.Rect(self.width // 2 - 50, self.height // 2 + 200, 100, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ready_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ready!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ready_button.center)
        self.pantalla.blit(text_surface, text_rect)


class AceptarPartidaMultiplayer:
    def __init__(self, username1, username2, boolean):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Aceptar partida")
        self.retador = username1
        self.player2 = username2
        self.boolean = boolean

        self.label = "El jugador " + self.retador + " quiere empezar una partida"

        self.red_label = "¿Quieres comenzar la rifa?"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (0, 0, 0)
        self.red_label_color = (0, 0, 0)  # Color rojo para el nuevo texto

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            print("se presionó ready")
                            rifa_ventana=rifaWindow(self.retador, self.player2)
                            rifa_ventana.run()

                        if self.back_button.collidepoint(event.pos):
                            from Menu2Jugadores import menu2players
                            if self.boolean == True:
                                back=menu2players(self.retador, self.player2)
                                back.run()
                            else:
                                back=menu2players(self.player2, self.retador)
                                back.run()


            self.pantalla.fill((255,255,255))
            self.draw_text_inputs()
            self.draw_ready_button()
            self.draw_red_text()
            self.draw_backy_button()
            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs(self):
        # Renderizar las etiquetas
        label_surface = self.font.render(self.label, True, self.label_color)
        self.pantalla.blit(label_surface, (self.width//2-150, self.height//2))

    def draw_red_text(self):
        # Renderizar el nuevo texto
        red_label_surface = self.font.render(self.red_label, True, self.red_label_color)
        self.pantalla.blit(red_label_surface, (self.width//2-75, self.height//2+50)) 

    def draw_ready_button(self):
        # Crea el botón en el centro de la ventana
        self.ready_button = pygame.Rect(self.width // 2 +100, self.height // 2 + 200, 100, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ready_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ready!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ready_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_backy_button(self):
        # Crea el botón en el centro de la ventana
        self.back_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 200, 100, 50)
        pygame.draw.rect(self.pantalla, (150, 150, 150), self.back_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Back', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.back_button.center)
        self.pantalla.blit(text_surface, text_rect)
