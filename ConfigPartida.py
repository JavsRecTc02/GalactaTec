import pygame
from pygame.locals import *
import sys
import webbrowser
#import MenuSeleccion as Menu


class ConfigPartida:
    def __init__(self, username1,previous_instance=None):
        self.previous_instance = previous_instance
        self.width = 1000
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("ConfigPartida de selección")
        self.user = username1
        self.lvlselect = 1
        
        
        self.input_data = {
                "rifa_winner1": {'label':'¡Bienvenido al menú de GalactaTEC!', "pos": (255, 40), "text": ""}
            }
        
        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (0, 0, 0)

        
    def run(self):

        print(Patrones.InitialSet(self)) #Este print sirve para que no se caiga el programa al ponerle valores iniciales a los patrones, pero causa que cada que se entre a este menu se reinicien

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.Patron1.collidepoint(event.pos):
                            Patrones.Patron1(self)
                            print("se seleccionó patrón 1")

                        if self.Patron2.collidepoint(event.pos):
                            Patrones.Patron2(self)
                            print("se seleccionó patrón 2")

                        if self.Patron3.collidepoint(event.pos):
                            Patrones.Patron3(self)
                            print("se seleccionó patrón 3")

                        if self.Patron4.collidepoint(event.pos):
                            Patrones.Patron4(self)
                            print("se seleccionó patrón 4")

                        if self.Patron5.collidepoint(event.pos):
                            Patrones.Patron5(self)
                            print("se seleccionó patrón 5")
                            
                        if self.Lvl1.collidepoint(event.pos):
                            self.lvlselect = 1
                            print("se seleccionó Nivel 1")

                        if self.Lvl2.collidepoint(event.pos):
                            self.lvlselect = 2
                            print("se seleccionó Nivel 2")

                        if self.Lvl3.collidepoint(event.pos):
                            self.lvlselect = 3
                            print("se seleccionó Nivel 3")

                        if self.Back_button.collidepoint(event.pos): #Aca se crea la instancia anterior
                            running = False
                            if self.previous_instance is not None:
                                    self.previous_instance.run()  # Llama al método run() de la instancia anterior
                            else:
                                pygame.quit()
                                return
                            
                        if self.Help_button.collidepoint(event.pos):
                            running = False
                            print("se presionó Ayuda")
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            print("nivel 1 tiene el patron:" , Patrones.GetPatron(self))    
                            print("nivel 2 tiene el patron:" , Patrones.GetPatron(self))
                            print("nivel 3 tiene el patron:" , Patrones.GetPatron(self))  
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
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
            self.draw_Back_button()
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
        # Crea el botón por debajo de los botones del nivel sleccionado
        if self.lvlselect == 1:
            self.Patron1 = pygame.Rect(self.width // 2 - 395, self.height // 2 - 140, 250, 50)
        elif self.lvlselect == 2:
            self.Patron1 = pygame.Rect(self.width // 2 - 125, self.height // 2 - 140, 250, 50)
        elif self.lvlselect == 3:
            self.Patron1 = pygame.Rect(self.width // 2 + 145, self.height // 2 - 140, 250, 50)

        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Patron1)
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

    def Getconfig(self):
        #print(Patrones.GetPatron(self))
        self.nivel1 = Patrones.GetPatron(self)
        self.nivel2 = Patrones.GetPatron(self)
        self.nivel3 = Patrones.GetPatron(self)

        if self.lvlselect == 1:
            self.nivel1 = Patrones.GetPatron(self)
            print (self.nivel1)
        
        elif self.lvlselect == 2:
            self.nivel1 = Patrones.GetPatron(self)
            print (self.nivel2)

        elif self.lvlselect == 3:
            self.nivel1 = Patrones.GetPatron(self)
            print (self.nivel3)
            
          

class Patrones:
    
    def __init__(self):
        self.patron1 = True
        self.patron2 = False
        self.patron3 = False
        self.patron4 = False
        self.patron5 = False
        self.PatronSeleccionado = 1
    
    def InitialSet(self):
        self.patron1 = True
        self.patron2 = False
        self.patron3 = False
        self.patron4 = False
        self.patron5 = False

    def Patron1(self):
        self.patron1 = True
        self.patron2 = False
        self.patron3 = False
        self.patron4 = False
        self.patron5 = False

    def Patron2(self):
        self.patron1 = False
        self.patron2 = True
        self.patron3 = False
        self.patron4 = False
        self.patron5 = False

    def Patron3(self):
        self.patron1 = False
        self.patron2 = False
        self.patron3 = True
        self.patron4 = False
        self.patron5 = False
    
    def Patron4(self):
        self.patron1 = False
        self.patron2 = False
        self.patron3 = False
        self.patron4 = True
        self.patron5 = False

    def Patron5(self):
        self.patron1 = False
        self.patron2 = False
        self.patron3 = False
        self.patron4 = False
        self.patron5 = True
    
    def GetPatron(self):

        if self.patron1 == True:
            self.PatronSeleccionado = 1
        
        elif self.patron2 == True:
            self.PatronSeleccionado = 2
        
        elif self.patron3 == True:
            self.PatronSeleccionado = 3

        elif self.patron4 == True:
            self.PatronSeleccionado = 4

        elif self.patron5 == True:
            self.PatronSeleccionado = 5

        else:
            print ("error")

        return self.PatronSeleccionado
        """
        print (self.patron1)
        print (self.patron2)
        print (self.patron3)
        print (self.patron4)
        print (self.patron5)
        print(self.PatronSeleccionado)"""