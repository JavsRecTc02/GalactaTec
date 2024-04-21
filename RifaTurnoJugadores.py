import pygame
from pygame.locals import *
import os
import random

from Niveles import nivel1

class rifaWindow:
    def __init__(self, username1, username2):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        self.user1 = username1
        self.user2 =  username2

        self.puesto1 = None
        self.puesto2 = None

        #Se realiza la rifa aleatoria de cual de los 2 jugadores tiene el primer turno
        if random.randint(1, 2) == 1:
            self.input_data = {
                "rifa_winner1": {"label": "El jugador " + self.user1 + " iniciará la partida", "pos": (300, 300), "text": ""}
            }
            self.puesto1 = self.user1
            self.puesto2 = self.user2
            return self.puesto1 and self.puesto2


        else:
            self.input_data = {
                "rifa_winner2": {"label": "El jugador " + self.user2 + " iniciará la partida", "pos": (300, 300), "text": ""}
            }
            self.puesto1 = self.user2
            self.puesto2 = self.user1
            return self.puesto1 and self.puesto2

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
                            if self.ready_button.collidepoint(event.pos):
                                print("se presionó")
                                niveles_window = nivel1(self.puesto1, self.puesto2)
                                niveles_window.run()

                                #Aqui se llama la clase que lleve a lo que tenga que llevar


                self.pantalla.fill((255,255,255))
                self.draw_text_inputs()
                self.draw_ready_button()
                pygame.display.flip()

            pygame.quit()
    
    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)

    def draw_ready_button(self):
        # Crea el botón en el centro de la ventana
        self.ready_button = pygame.Rect(self.width // 2 - 50, self.height // 2 + 200, 100, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ready_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ready!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ready_button.center)
        self.pantalla.blit(text_surface, text_rect)
