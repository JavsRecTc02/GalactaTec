import pygame
from pygame.locals import *
import sys
import webbrowser


class ConfigPartida:
    def __init__(self, username1):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("ConfigPartida de selección")
        self.user = username1

        self.input_data = {
                "rifa_winner1": {'label':'¡Bienvenido al menú de GalactaTEC!', "pos": (255, 40), "text": ""}
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
                        if self.Patron1.collidepoint(event.pos):
                            print("se seleccionó patrón 1")

                        if self.Patron2.collidepoint(event.pos):
                            print("se seleccionó patrón 2")

                        if self.Patron3.collidepoint(event.pos):
                            print("se seleccionó patrón 3")

                        if self.Patron4.collidepoint(event.pos):
                            print("se seleccionó patrón 4")

                        if self.Patron5.collidepoint(event.pos):
                            print("se seleccionó patrón 5")
                            
                        if self.Lvl1.collidepoint(event.pos):
                            print("se seleccionó Nivel 1")

                        if self.Lvl2.collidepoint(event.pos):
                            print("se seleccionó Nivel 2")

                        if self.Lvl3.collidepoint(event.pos):
                            print("se seleccionó Nivel 3")

                        if self.Exit_button.collidepoint(event.pos):
                            running = False
                            sys.exit()

                        if self.Help_button.collidepoint(event.pos):
                            running = False
                            print("se presionó Ayuda")
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Usuario\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
                            ConfigPartida.run(self)

                
            self.pantalla.fill((255,255,255))
            self.draw_text_inputs()
            self.draw_Patron1()
            self.draw_Patron2()
            self.draw_Patron3()
            self.draw_Patron4()
            self.draw_Patron5()
            self.draw_Lvl1()
            self.draw_Lvl2()
            self.draw_Lvl3()
            self.draw_Exit_button()
            self.draw_Help_button()

            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)

    def draw_Patron1(self):
        # Crea el botón en el centro de la ventana
        self.Patron1 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 140, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 1', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron2(self):
        # Crea el botón en el centro de la ventana
        self.Patron2 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 80, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 2', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron3(self):
        # Crea el botón en el centro de la ventana
        self.Patron3 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 20, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron3)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 3', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron3.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron4(self):
        # Crea el botón en el centro de la ventana
        self.Patron4 = pygame.Rect(self.width // 2 - 125, self.height // 2 + 40, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron4)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 4', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron4.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron5(self):
        # Crea el botón en el centro de la ventana
        self.Patron5 = pygame.Rect(self.width // 2 - 125, self.height // 2 + 100, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron5)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 5', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron5.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Lvl1(self):
        # Crea el botón en el centro de la ventana
        self.Lvl1 = pygame.Rect(self.width // 2 - 395, self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Lvl1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Nivel 1', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Lvl1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Lvl2(self):
        # Crea el botón en el centro de la ventana
        self.Lvl2 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Lvl2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Nivel 2', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Lvl2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Lvl3(self):
        # Crea el botón en el centro de la ventana
        self.Lvl3 = pygame.Rect(self.width // 2 + 145, self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Lvl3)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Nivel 3', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Lvl3.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Exit_button(self):
        # Crea el botón en el centro de la ventana
        self.Exit_button = pygame.Rect(self.width // 2 - 0, self.height // 2 + 220, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Exit_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salir del juego', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Exit_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Help_button(self):
        # Crea el botón en el centro de la ventana
        self.Help_button = pygame.Rect(self.width // 2 - 260, self.height // 2 + 220, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Help_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ayuda', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Help_button.center)
        self.pantalla.blit(text_surface, text_rect)
