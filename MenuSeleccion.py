import pygame
from pygame.locals import *
import sys

from Niveles import nivel1
from RifaTurnoJugadores import rifaWindow

class Menu:
    def __init__(self, username1):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Menu de selección")
        self.user = username1

        self.input_data = {
                "rifa_winner1": {'label':'¡Bienvenido al menú de GalacTEC!', "pos": (255, 40), "text": ""}
            }
        

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (0, 0, 0)

    def run(self):
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.configUsuario_button.collidepoint(event.pos):
                                print("se presionó ConfigUsuario")

                            if self.fama_button.collidepoint(event.pos):
                                print("se presionó Fama")

                            if self.ConfigPartida_button.collidepoint(event.pos):
                                print("se presionó Config partida")

                            if self.Jugador2_Button.collidepoint(event.pos):
                                rifa = rifaWindow(self.user, 'GamerPro777')
                                rifa.run()

                            if self.Partida1_button.collidepoint(event.pos):
                                Nivel1_window = nivel1(self.user, None)
                                Nivel1_window.run()

                            if self.Exit_button.collidepoint(event.pos):
                                running = False
                                sys.exit()

                self.pantalla.fill((255,255,255))
                self.draw_text_inputs()
                self.draw_configUsuario_button()
                self.draw_fama_button()
                self.draw_ConfigPartida_button()
                self.draw_Jugador2_button()
                self.draw_Partida1_button()
                self.draw_Exit_button()
                

                pygame.display.flip()

            pygame.quit()
    
    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)

    def draw_configUsuario_button(self):
        # Crea el botón en el centro de la ventana
        self.configUsuario_button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.configUsuario_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de usuario', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.configUsuario_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_fama_button(self):
        # Crea el botón en el centro de la ventana
        self.fama_button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 140, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.fama_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salón de la fama', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.fama_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_ConfigPartida_button(self):
        # Crea el botón en el centro de la ventana
        self.ConfigPartida_button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 80, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ConfigPartida_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de la partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ConfigPartida_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Jugador2_button(self):
        # Crea el botón en el centro de la ventana
        self.Jugador2_Button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 20, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Jugador2_Button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Iniciar Jugador 2', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Jugador2_Button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Partida1_button(self):
        # Crea el botón en el centro de la ventana
        self.Partida1_button = pygame.Rect(self.width // 2 - 125, self.height // 2 + 40, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Partida1_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Iniciar partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Partida1_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Exit_button(self):
        # Crea el botón en el centro de la ventana
        self.Exit_button = pygame.Rect(self.width // 2 - 125, self.height // 2 + 100, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Exit_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salir del juego', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Exit_button.center)
        self.pantalla.blit(text_surface, text_rect)