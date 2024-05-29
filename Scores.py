import pygame
from pygame.locals import *
import sys
import os
import csv
import ctypes
from pygame import USEREVENT


class Scores:
    def __init__(self, file_path, username):
        self.player1 = username # este user lo mandamos a la user config
        print(self.player1)
        self.file_path = file_path
        self.scores = self.read_scores()

    def read_scores(self):
        scores = []
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append({'username': row[0], 'score': int(row[1])})
        return scores

    def get_top_scores(self):
        sorted_scores = sorted(self.scores, key=lambda x: x['score'], reverse=True)
        top_scores = sorted_scores[:5]
        if len(top_scores) < 5:
            for i in range(5 - len(top_scores)):
                top_scores.append({'username': 'Disponible', 'score': '-'})
        return top_scores

    def get_profile_image(self, username):
        ruta_directorio_carpetas = r"C:\Users\Javier Tenorio\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if username in carpetas:
            ruta_carpeta_usuari = os.path.join(ruta_directorio_carpetas, username)
            archivos = os.listdir(ruta_carpeta_usuari)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                imagen_perfil = pygame.image.load(os.path.join(ruta_carpeta_usuari, archivo))
                return pygame.transform.scale(imagen_perfil, (50, 50))
        return None


class ScoreWindow:
    def __init__(self,username,previous_instance=None):
        self.previous_instance = previous_instance
        self.player = username
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Top Scores')
        self.clock = pygame.time.Clock()
        self.scores = Scores('scores.txt', self.player)
        self.background = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\scorebg.jpg").convert()

        # Definir las coordenadas y dimensiones del botón
        self.button_rect = pygame.Rect(700, 500, 80, 40)  # Posición y tamaño del botón

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar si se hizo clic en el botón "Back"
                    if self.previous_instance is not None:
                            self.previous_instance.run()  # Llama al método run() de la instancia anterior
                    else:
                        pygame.quit()
                        return

            # Dibuja el fondo
            self.screen.blit(self.background, (0, 0))

            # Dibuja el botón "Back"
            pygame.draw.rect(self.screen, (100, 100, 100), self.button_rect)  # Dibuja el botón en un color gris
            font = pygame.font.Font(None, 24)
            text_surface = font.render('Back', True, (255, 255, 255))  # Renderiza el texto "Back"
            text_rect = text_surface.get_rect(center=self.button_rect.center)  # Centra el texto en el botón
            self.screen.blit(text_surface, text_rect)  # Dibuja el texto en el botón

            # Muestra los puntajes
            self.display_scores(self.scores.get_top_scores())

            pygame.display.flip()
            self.clock.tick(60)

    def display_scores(self, top_scores):
        font = pygame.font.Font(None, 36)
        y = 50
        for i, score in enumerate(top_scores):
            text = f"{i + 1}. {score['username']}: {score['score']}"
            rendered_text = font.render(text, True, (255, 255, 255))
            self.screen.blit(rendered_text, (30, (y+45)))

            profile_image = self.scores.get_profile_image(score['username'])
            if profile_image:
                self.screen.blit(profile_image, (300, (y+45)))  # Ajusta las coordenadas según tu diseño

            y += 80
