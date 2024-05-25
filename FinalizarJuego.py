import pygame
import sys
from Scores import ScoreWindow
import ctypes
import os

import pygame
import sys
import ctypes
#from MenuSeleccion import Menu
#Para volver al Menu hay que crearlo de otra forma, con una instancia variable igual que el boton back de scores

class FinalizarJuego:
    def __init__(self, username, puntaje):
        pygame.init()
        self.username = username
        self.puntaje = puntaje
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Game Over')
        self.profile_image = self.get_profile_image(self.username)

        self.fuente = pygame.font.Font(None, 74)
        self.fuente_botones = pygame.font.Font(None, 50)

        # Definir los colores
        self.color_texto = (255, 255, 255)
        self.color_fondo = (0, 0, 0)
        self.color_boton = (0, 100, 255)
        self.color_boton_hover = (0, 150, 255)
        self.color_rojo = (255, 0, 0)

        # Definir los botones
        self.boton_menu = pygame.Rect(150, 450, 150, 50)
        self.boton_salir = pygame.Rect(325, 450, 150, 50)
        self.boton_scores = pygame.Rect(500, 450, 150, 50)

        # Verificar si es un nuevo mejor puntaje
        self.nuevo_mejor_puntaje = self.verificar_nuevo_mejor_puntaje()

        # Guardar el puntaje en el archivo scores.txt
        self.guardar_puntaje()

    def user_message(self, message):
        ctypes.windll.user32.MessageBoxW(0, message, "Nuevo Record", 1)

    def verificar_nuevo_mejor_puntaje(self):
        with open(r"C:\Users\Usuario\Desktop\GalactaTec-1\scores.txt", 'r') as file:
            scores = [line.strip().split(',') for line in file]
            scores = [(name, int(score)) for name, score in scores]

        top_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
        return self.puntaje > top_scores[-1][1] if len(top_scores) > 0 else True  # Si no hay puntajes, es un nuevo mejor puntaje

    def guardar_puntaje(self):
        with open(r"C:\Users\Usuario\Desktop\GalactaTec-1\scores.txt", 'a') as file:
            file.write(f"{self.username},{self.puntaje}\n")

        if self.nuevo_mejor_puntaje:
            self.mostrar_mensaje_nuevo_record()

    def mostrar_mensaje_nuevo_record(self):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 10000:  # 10 segundos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.time.get_ticks() % 1000 < 500:  # Parpadeo cada medio segundo
                self.dibujar_pantalla(show_message=True)
            else:
                self.dibujar_pantalla(show_message=False)

        self.user_message("Felicidades, " + self.username + " has establecido un nuevo record en el salón de la fama!")
        self.mostrar_ventana_records()

    def mostrar_ventana_records(self):
        scores_window = ScoreWindow(self.username, self.puntaje)
        scores_window.previous_instance = self
        scores_window.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_menu.collidepoint(event.pos):
                        print("MENU")
                        # Implementa la funcionalidad para ir al menú
                    elif self.boton_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif self.boton_scores.collidepoint(event.pos):
                        scores_window = ScoreWindow(self.username, self.puntaje)
                        scores_window.previous_instance = self
                        scores_window.run()

            self.dibujar_pantalla(self.nuevo_mejor_puntaje)

    def dibujar_pantalla(self, show_message):
        self.pantalla.fill(self.color_fondo)

        # Dibujar imagen de perfil 
        if self.profile_image:
            self.pantalla.blit(self.profile_image, (610, 50))  

        # Mostrar texto de Game Over
        texto_game_over = self.fuente.render('Game Over', True, (255, 0, 0))
        self.pantalla.blit(texto_game_over, (250, 50))

        # Mostrar username y puntaje
        texto_usuario = self.fuente.render(f'Usuario: {self.username}', True, self.color_texto)
        texto_puntaje = self.fuente.render(f'Puntaje: {self.puntaje}', True, self.color_texto)
        self.pantalla.blit(texto_usuario, (200, 200))
        self.pantalla.blit(texto_puntaje, (200, 300))

        # Mostrar mensaje de nuevo record si es necesario
        if show_message:
            mensaje_nuevo_record = self.fuente_botones.render('Nuevo Record!', True, self.color_rojo)
            self.pantalla.blit(mensaje_nuevo_record, (250, 400))

        # Dibujar botones
        self.dibujar_boton(self.boton_menu, 'MENU')
        self.dibujar_boton(self.boton_salir, 'SALIR')
        self.dibujar_boton(self.boton_scores, 'SCORES')

        pygame.display.flip()

    def dibujar_boton(self, rect, texto):
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):
            color = self.color_boton_hover
        else:
            color = self.color_boton

        pygame.draw.rect(self.pantalla, color, rect)
        texto_boton = self.fuente_botones.render(texto, True, self.color_texto)
        self.pantalla.blit(texto_boton, (rect.x + (rect.width - texto_boton.get_width()) // 2, rect.y + (rect.height - texto_boton.get_height()) // 2))

    def get_profile_image(self, username):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec-1\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if username in carpetas:
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, username)
            archivos = os.listdir(ruta_carpeta_usuario)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                imagen_perfil = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                return pygame.transform.scale(imagen_perfil, (80, 80))
        return None





