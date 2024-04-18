import pygame
from pygame import *
import os

class Nave:
    def __init__(self, pantalla, username):
        self.pantalla = pantalla
        self.username = username
        self.velocidad = 5  # Define la velocidad de la nave
        self.imagen = self.loadNave()  # Carga la imagen de la nave
        self.rect = self.imagen.get_rect()
        self.rect.center = (self.pantalla.get_width() / 2, self.pantalla.get_height() / 2)  # Posiciona la nave en el centro de la pantalla

    def mover(self, keys):
        if keys[pygame.K_UP]:  # Mover hacia arriba
            self.rect.y -= self.velocidad
        if keys[pygame.K_DOWN]:  # Mover hacia abajo
            self.rect.y += self.velocidad
        if keys[pygame.K_LEFT]:  # Mover hacia la izquierda
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:  # Mover hacia la derecha
            self.rect.x += self.velocidad

    def dibujar(self):
        self.pantalla.blit(self.imagen, self.rect)

    def loadNave(self):
        # Ruta al directorio para archivos del jugador
        ruta_directorio_carpetas = 'C://Users//Usuario//Desktop//GalactaTec//User files'
        # Obtiene una lista de todas las carpetas en el directorio
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]

        # Clasifica las carpetas por nombre
        carpetas.sort()
        if self.username in carpetas:
            # Ruta a la carpeta del usuario
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username)
            # Obtiene una lista de todos los archivos en la carpeta del usuario
            archivos = os.listdir(ruta_carpeta_usuario)
            # Busca los archivos que se llamen "perfil"
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('nave_espacial')]
            for archivo in archivos_perfil:
                # Carga la imagen
                imagen_nave = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_nave = pygame.transform.scale(imagen_nave, (100, 100))
                return imagen_nave  # Devuelve la imagen cargada

