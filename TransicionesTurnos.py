import pygame
from pygame.locals import *

class windowLost1player:
    def __init__(self, username1, username2, vidas, puntos, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas = max(0, vidas)  # Asegura que las vidas no sean menores que 0
        self.puntos = puntos

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas, vas a comenzar el mismo nivel!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)
        self.red_label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3

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
                            juego=nivel1(self.player1, self.player2, self.vidas, self.puntos, None, None, None, None, self.patron1, self.patron2, self.patron3)
                            juego.run()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel1
                        juego=nivel1(self.player1, self.player2, self.vidas, self.puntos, None, None, None, None, self.patron1, self.patron2, self.patron3)
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


class windowLost2players:
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2, Nivel_player1, Nivel_player2, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas_player1 = max(0,vidas_player1)
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = max(0,vidas_player2)
        self.puntos_player2 = puntos_player2

        self.nivel_actual_player1 = Nivel_player1
        self.nivel_actual_player2 = Nivel_player2

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3


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
                            juego=nivel1(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1, self.nivel_actual_player2, self.nivel_actual_player1, self.patron1, self.patron2, self.patron3)
                            juego.run()
                            print("se presionó ready")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel1
                        juego=nivel1(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1, self.nivel_actual_player2, self.nivel_actual_player1,  self.patron1, self.patron2, self.patron3)
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


##################################################################################################################
##################################################################################################################
class windowLost1player_LVL2:
    def __init__(self, username1, username2, vidas, puntos, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas = max(0, vidas)
        self.puntos = puntos

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas, vas a comenzar el mismo nivel!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)
        self.red_label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            from Niveles import nivel2
                            juego=nivel2(self.player1, self.player2, self.vidas, self.puntos, None, None, None, None, self.patron1, self.patron2, self.patron3)
                            juego.run()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel2
                        juego=nivel2(self.player1, self.player2, self.vidas, self.puntos, None, None, None, None, self.patron1, self.patron2, self.patron3)
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


class windowLost2players_LVL2:
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2, Nivel_player1, Nivel_player2, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas_player1 = max(0,vidas_player1)
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = max(0,vidas_player2)
        self.puntos_player2 = puntos_player2

        self.nivel_actual_player1 = Nivel_player1
        self.nivel_actual_player2 = Nivel_player2

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            from Niveles import nivel2
                            juego=nivel2(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1, self.nivel_actual_player2, self.nivel_actual_player1, self.patron1, self.patron2, self.patron3)
                            juego.run()
                            print("se presionó ready")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel2
                        juego=nivel2(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1, self.nivel_actual_player2, self.nivel_actual_player1, self.patron1, self.patron2, self.patron3)
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

##################################################################################################################
##################################################################################################################
class windowLost1player_LVL3:
    def __init__(self, username1, username2, vidas, puntos, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas = max(vidas)
        self.puntos = puntos

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas, vas a comenzar el mismo nivel!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)
        self.red_label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            from Niveles import nivel3
                            juego=nivel3(self.player1, self.player2, self.vidas, self.puntos, None, None, None, None, self.patron1, self.patron2, self.patron3)
                            juego.run()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel3
                        juego=nivel3(self.player1, self.player2, self.vidas, self.puntos, None, None, self.patron1, self.patron2, self.patron3)
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


class windowLost2players_LVL3:
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2, Nivel_player1, Nivel_player2, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Perdiste una vida")
        self.player1 = username1
        self.player2 = username2

        self.vidas_player1 = max(0,vidas_player1)
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = max(0,vidas_player2)
        self.puntos_player2 = puntos_player2

        self.nivel_actual_player1 = Nivel_player1
        self.nivel_actual_player2 = Nivel_player2

        self.label = '¡'+ self.player1 + ", haz perdido una o mas vidas!"

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga la imagen de fondo
        self.fondo = pygame.image.load(r'C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\cambio de turnos.webp')
        # Ajusta la imagen al tamaño de la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.ready_button.collidepoint(event.pos):
                            from Niveles import nivel3
                            juego=nivel3(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1, self.nivel_actual_player2, self.nivel_actual_player1, self.patron1, self.patron2, self.patron3)
                            juego.run()
                            print("se presionó ready")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        from Niveles import nivel3
                        juego=nivel3(self.player2,self.player1,self.vidas_player2,self.puntos_player2, self.vidas_player1, self.puntos_player1, self.nivel_actual_player2, self.nivel_actual_player1, self.patron1, self.patron2, self.patron3)
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