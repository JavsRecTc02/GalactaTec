import pygame
from pygame.locals import *
import sys
import webbrowser
#import MenuSeleccion as Menu


class ConfigPartida:
    def __init__(self, player1, player2, patron1, patron2, patron3):
        self.width = 1000
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("ConfigPartida de selección")

        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(r"C:\Users\Usuario\Desktop\GalactaTec\backgrounds\ConfigP.webp")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.player1 = player1
        self.player2 = player2

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 =patron3

        self.lvlselect = 1
        
        
        self.input_data = {
                "rifa_winner1": {'label':'¡Escoge los patrones para los niveles!', "pos": (340, 10), "text": ""}
            }
        
        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        self.Nivel1 = pygame.Rect(self.width // 2 - 400, self.height // 2  - 250, 250, 50)
        self.Nivel2 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 250, 250, 50)
        self.Nivel3 = pygame.Rect(self.width // 2 + 150, self.height // 2 - 250, 250, 50)

        # Agrega una lista de botones de patrones del nivel 1
        self.patron_buttons_LVL1 = [pygame.Rect(self.width // 2 - 310, 125 + i*40, 80, 30) for i in range(5)]
        self.show_patron_buttons_LVL1 = False

        # Agrega una lista de botones de patrones del nivel 2
        self.patron_buttons_LVL2 = [pygame.Rect(self.width // 2 - 35, 125 + i*40, 80, 30) for i in range(5)]
        self.show_patron_buttons_LVL2 = False


        # Agrega una lista de botones de patrones del nivel 3
        self.patron_buttons_LVL3 = [pygame.Rect(self.width // 2 + 230, 125 + i*40, 80, 30) for i in range(5)]
        self.show_patron_buttons_LVL3 = False


        # Agrega un estado para cada patrón
        self.patron_states = [True for _ in range(5)]  # Todos los patrones están activos al inicio

        # Agrega un patrón seleccionado para cada nivel
        self.selected_patron = [None for _ in range(3)]  # Ningún patrón está seleccionado al inicio


        # Actualiza el estado inicial de los patrones según los valores de patron1, patron2 y patron3
        if patron1 is not None:
            self.patron_states[patron1-1] = False
            self.selected_patron[0] = patron1-1
        if patron2 is not None:
            self.patron_states[patron2-1] = False
            self.selected_patron[1] = patron2-1
        if patron3 is not None:
            self.patron_states[patron3-1] = False
            self.selected_patron[2] = patron3-1

    def draw_background(self):
        self.pantalla.blit(self.background_image, (0, 0))
                
    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        
                        if self.Nivel1.collidepoint(event.pos):
                            print("se seleccionó Nivel 1")
                            self.show_patron_buttons_LVL1 = True

                        if self.Nivel2.collidepoint(event.pos):
                            self.show_patron_buttons_LVL2 = True
                            print("se seleccionó Nivel 2")

                        if self.Nivel3.collidepoint(event.pos):
                            self.show_patron_buttons_LVL3 = True
                            print("se seleccionó Nivel 3")


                        # Interactúa con los botones de patrones de todos los niveles
                        for lvl in range(1, 4):
                            if getattr(self, f'show_patron_buttons_LVL{lvl}'):
                                for i, button in enumerate(getattr(self, f'patron_buttons_LVL{lvl}')):
                                    if button.collidepoint(event.pos) and self.patron_states[i]:  # Solo interactúa si el patrón está activo
                                        print(f"Se seleccionó el patrón {i+1}")
                                        if self.selected_patron[lvl-1] is not None:  # Si ya hay un patrón seleccionado para este nivel
                                            self.patron_states[self.selected_patron[lvl-1]] = True  # Reactiva el patrón anterior
                                        self.selected_patron[lvl-1] = i  # Actualiza el patrón seleccionado
                                        self.patron_states[i] = False  # Desactiva el patrón
                                        setattr(self, f'patron{lvl}', i+1)  # Actualiza la variable de patrón correspondiente


                        if self.Back_button.collidepoint(event.pos): #Aca se crea la instancia anterior
                            if self.player2 != None:
                                from Menu2Jugadores import menu2players
                                ventana = menu2players(self.player1, self.player2, self.patron1, self.patron2, self.patron3)
                                ventana.run()

                            else:
                                from MenuSeleccion import Menu
                                ventana = Menu(self.player1, self.patron1, self.patron2, self.patron3)
                                ventana.run()
                            
                        if self.Help_button.collidepoint(event.pos):
                            pass
                            webbrowser.open_new(r'file://C:\Users\Usuario\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')

   
            self.draw_background()
            self.draw_text_inputs()
            self.draw_Niveles()
            self.draw_Back_button()
            self.draw_Help_button()


            # Dibuja los botones de patrones de todos los niveles
            for lvl in range(1, 4):
                if getattr(self, f'show_patron_buttons_LVL{lvl}'):
                    for i, button in enumerate(getattr(self, f'patron_buttons_LVL{lvl}')):
                        color = (0, 0, 0) if self.patron_states[i] else (255, 0, 0)  # Cambia el color si el patrón está inactivo
                        if self.selected_patron[lvl-1] == i:  # Si este patrón está seleccionado para este nivel
                            color = (0, 255, 0)  # Cambia el color a verde
                        pygame.draw.rect(self.pantalla, color, button)  # Dibuja el botón
                        self.pantalla.blit(self.font.render(f'Patron {i+1}', True, (255, 255, 255)), (button.x, button.y))  # Dibuja el texto

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
        # Crea el botón por debajo de los botones del nivel sleccionado
        if self.lvlselect == 1:
            self.Patron1 = pygame.Rect(self.width // 2 - 395, self.height // 2 - 140, 250, 50)
        elif self.lvlselect == 2:
            self.Patron1 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 140, 250, 50)
        elif self.lvlselect == 3:
            self.Patron1 = pygame.Rect(self.width // 2 + 145, self.height // 2 - 140, 250, 50)

        pygame.draw.rect(self.pantalla, self.Patron1_color, self.Patron1)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 1', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron1.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron2(self):
        # Crea el botón por debajo de los botones del nivel sleccionado
        if self.lvlselect == 1:
            self.Patron2 = pygame.Rect(self.width // 2 - 395, self.height // 2 - 80, 250, 50)
        elif self.lvlselect == 2:
            self.Patron2 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 80, 250, 50)
        elif self.lvlselect == 3:
            self.Patron2 = pygame.Rect(self.width // 2 + 145, self.height // 2 - 80, 250, 50)

        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron2)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 2', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron2.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron3(self):
        # Crea el botón por debajo de los botones del nivel sleccionado
        if self.lvlselect == 1:
            self.Patron3 = pygame.Rect(self.width // 2 - 395, self.height // 2 - 20, 250, 50)
        elif self.lvlselect == 2:
            self.Patron3 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 20, 250, 50)
        elif self.lvlselect == 3:
            self.Patron3 = pygame.Rect(self.width // 2 + 145, self.height // 2 - 20, 250, 50)

        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron3)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 3', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron3.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron4(self):
        # Crea el botón por debajo de los botones del nivel sleccionado
        if self.lvlselect == 1:
            self.Patron4 = pygame.Rect(self.width // 2 - 395, self.height // 2 + 40, 250, 50)
        elif self.lvlselect == 2:
            self.Patron4 = pygame.Rect(self.width // 2 - 125, self.height // 2 + 40, 250, 50)
        elif self.lvlselect == 3:
            self.Patron4 = pygame.Rect(self.width // 2 + 145, self.height // 2 + 40, 250, 50)
        
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron4)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 4', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron4.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Patron5(self):
        # Crea el botón por debajo de los botones del nivel sleccionado
        if self.lvlselect == 1:
            self.Patron5 = pygame.Rect(self.width // 2 - 395, self.height // 2 + 100, 250, 50)
        elif self.lvlselect == 2:
            self.Patron5 = pygame.Rect(self.width // 2 - 125, self.height // 2 + 100, 250, 50)
        elif self.lvlselect == 3:
            self.Patron5 = pygame.Rect(self.width // 2 + 145, self.height // 2 + 100, 250, 50)
        
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron5)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('patrón 5', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Patron5.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Niveles(self):
        pygame.draw.rect(self.pantalla, (0,0,0), self.Nivel1)
        pygame.draw.rect(self.pantalla, (0,0,0), self.Nivel2)
        pygame.draw.rect(self.pantalla, (0,0,0), self.Nivel3)

        font = pygame.font.Font(None, 24)
        text_surface1 = font.render('Nivel 1', True, (255, 255, 255))
        text_surface2 = font.render('Nivel 2', True, (255, 255, 255))
        text_surface3 = font.render('Nivel 3', True, (255, 255, 255))

        text_rect1 = text_surface1.get_rect(center=self.Nivel1.center)
        text_rect2 = text_surface2.get_rect(center=self.Nivel2.center)
        text_rect3 = text_surface3.get_rect(center=self.Nivel3.center)

        self.pantalla.blit(text_surface1, text_rect1)
        self.pantalla.blit(text_surface2, text_rect2)
        self.pantalla.blit(text_surface3, text_rect3)

    def draw_Back_button(self):
        # Crea el botón en el centro de la ventana
        self.Back_button = pygame.Rect(self.width // 2 - 0, self.height // 2 + 220, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Back_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Back', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Back_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Help_button(self):
        # Crea el botón en el centro de la ventana
        self.Help_button = pygame.Rect(self.width // 2 - 260, self.height // 2 + 220, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Help_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ayuda', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Help_button.center)
        self.pantalla.blit(text_surface, text_rect)

            
          
