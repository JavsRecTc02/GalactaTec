from MenuSeleccion import Menu
import pygame
from pygame.locals import *
import sys
import webbrowser

from Niveles import nivel1
from RifaTurnoJugadores import AceptarPartidaMultiplayer
from ConfigPartida import ConfigPartida
from Scores import ScoreWindow
from MenuSeleccion import UsersConfig


class menu2players(Menu):
    def __init__(self, username1, username2):
        super().__init__(username1)
        self.player1 = self.user
        self.player2 = username2
        self.width = 1000
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.input_data = {
                "rifa_winner1": {'label':'¡Bienvenido ' + self.player1 +' al menú de GalactaTEC!', "pos": (50, 40), "text": ""},
                "rifa_winner2": {'label':'¡Bienvenido ' + self.player2 + ' al menú de GalactaTEC!', "pos": (550, 40), "text": ""}
            }
        self.scores_window = ScoreWindow(self.player1, self.player2)
        self.scores_window.previous_instance = self #Unica instancia para Scores

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        ##Para el jugador 1
                        if self.configuser_button_player1.collidepoint(event.pos):
                            print("se presionó Configuser de Player1")
                            config_window = UsersConfig(self.player1, self.player2)
                            config_window.previous_instance = self
                            config_window.run()

                        if self.fama_button_player1.collidepoint(event.pos):
                            print("se presionó Fama de player1")
                            self.scores_window.run()

                        if self.ConfigPartida_button_player1.collidepoint(event.pos):
                            config_partida = ConfigPartida(self.player1,self.player2)
                            config_partida.previous_instance = self
                            config_partida.run()
                            print("Se presiono Config Partida")

                        if self.Iniciar_button_player1.collidepoint(event.pos):
                            pantalla_aceptar = AceptarPartidaMultiplayer(self.player1, self.player2, True)
                            pantalla_aceptar.run()

                        if self.Exit_button_player1.collidepoint(event.pos):
                            running = False
                            sys.exit()

                        if self.Help_button_player1.collidepoint(event.pos):
                            running = False
                            print("se presionó Ayuda del player1")
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
                            menu2players.run(self)

                        ##Para el jugador 2
                        if self.configuser_button_player2.collidepoint(event.pos):
                            print("se presionó Configuser de Player2")
                            config_window = UsersConfig(self.player2, self.player1)
                            config_window.previous_instance = self
                            config_window.run()

                        if self.fama_button_player2.collidepoint(event.pos):
                            print("se presionó Fama de player2")
                            self.scores_window.run()

                        if self.ConfigPartida_button_player2.collidepoint(event.pos):
                            config_partida = ConfigPartida(self.player2,self.player1)
                            config_partida.previous_instance = self
                            config_partida.run()
                            print("se presionó Config partida de player2")

                        if self.Iniciar_button_player2.collidepoint(event.pos):
                            pantalla_aceptar = AceptarPartidaMultiplayer(self.player2, self.player1, False)
                            pantalla_aceptar.run()

                        if self.Exit_button_player2.collidepoint(event.pos):
                            running = False
                            sys.exit()

                        if self.Help_button_player2.collidepoint(event.pos):
                            running = False
                            print("se presionó Ayuda del player2")
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
                            menu2players.run(self)

            self.pantalla.fill((255,255,255))
            self.draw_text_inputs()
            self.draw_configuser_button_Player1()
            self.draw_fama_button_Player1()
            self.draw_ConfigPartida_button_Player1()
            self.draw_Inciar_button_Player1()
            self.draw_Exit_button_Player1()
            self.draw_Help_button_Player1()

            ##Btones para el segundo jugador
            self.draw_configuser_button_Player2()
            self.draw_fama_button_Player2()
            self.draw_ConfigPartida_button_Player2()
            self.draw_Inciar_button_Player2()
            self.draw_Exit_button_Player2()
            self.draw_Help_button_Player2()

            
            # Dibujar una línea vertical que divide la pantalla a la mitad
            pygame.draw.line(self.pantalla, (0, 0, 0), (self.width / 2, 0), (self.width / 2, self.height), 1)

            pygame.display.flip()
        pygame.quit()

    def draw_configuser_button_Player1(self):
        # Crea el botón en el centro de la ventana
        self.configuser_button_player1 = pygame.Rect(self.width // 2 - 375 , self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.configuser_button_player1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de user', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.configuser_button_player1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_fama_button_Player1(self):
        # Crea el botón en el centro de la ventana
        self.fama_button_player1 = pygame.Rect(self.width // 2 - 375, self.height // 2 - 140, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.fama_button_player1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salón de la fama', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.fama_button_player1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_ConfigPartida_button_Player1(self):
        # Crea el botón en el centro de la ventana
        self.ConfigPartida_button_player1 = pygame.Rect(self.width // 2 - 375, self.height // 2 - 80, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ConfigPartida_button_player1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de la partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ConfigPartida_button_player1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Inciar_button_Player1(self):
        # Crea el botón en el centro de la ventana
        self.Iniciar_button_player1 = pygame.Rect(self.width // 2 - 375, self.height // 2 - 20, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Iniciar_button_player1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Iniciar partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Iniciar_button_player1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Exit_button_Player1(self):
        # Crea el botón en el centro de la ventana
        self.Exit_button_player1 = pygame.Rect(self.width // 2 - 375, self.height // 2 + 40, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Exit_button_player1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salir del juego', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Exit_button_player1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Help_button_Player1(self):
        # Crea el botón en el centro de la ventana
        self.Help_button_player1 = pygame.Rect(self.width // 2 - 375, self.height // 2 + 100, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Help_button_player1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ayuda', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Help_button_player1.center)
        self.pantalla.blit(text_surface, text_rect)


#######################################################################
##Botones para el segundo jugador
########################################################################
    def draw_configuser_button_Player2(self):
        # Crea el botón en el centro de la ventana
        self.configuser_button_player2 = pygame.Rect(self.width // 2 + 125 , self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.configuser_button_player2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de user', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.configuser_button_player2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_fama_button_Player2(self):
        # Crea el botón en el centro de la ventana
        self.fama_button_player2 = pygame.Rect(self.width // 2 + 125, self.height // 2 - 140, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.fama_button_player2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salón de la fama', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.fama_button_player2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_ConfigPartida_button_Player2(self):
        # Crea el botón en el centro de la ventana
        self.ConfigPartida_button_player2 = pygame.Rect(self.width // 2 + 125, self.height // 2 - 80, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ConfigPartida_button_player2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de la partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ConfigPartida_button_player2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Inciar_button_Player2(self):
        # Crea el botón en el centro de la ventana
        self.Iniciar_button_player2 = pygame.Rect(self.width // 2 + 125, self.height // 2 - 20, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Iniciar_button_player2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Iniciar partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Iniciar_button_player2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Exit_button_Player2(self):
        # Crea el botón en el centro de la ventana
        self.Exit_button_player2 = pygame.Rect(self.width // 2 + 125, self.height // 2 + 40, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Exit_button_player2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salir del juego', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Exit_button_player2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Help_button_Player2(self):
        # Crea el botón en el centro de la ventana
        self.Help_button_player2 = pygame.Rect(self.width // 2 + 125, self.height // 2 + 100, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Help_button_player2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ayuda', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Help_button_player2.center)
        self.pantalla.blit(text_surface, text_rect)