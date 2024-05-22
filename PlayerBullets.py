import pygame
from pygame import *

class BasicBullet:
    def __init__(self, screen):
        self.screen = screen
        self.velocidad_bala = 5
        imagen_original = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Bullets\BasicBullet.png")  # Carga la imagen de la bala
        self.imagen = pygame.transform.scale(imagen_original, (50, 50))  # Ajusta el tamaño de la imagen
        self.rect = self.imagen.get_rect()
        self.rect.center = (self.screen.get_width() / 2, self.screen.get_height() - self.rect.height / 2)  # Posiciona la bala en el centro de la pantalla
        self.disparada = True  # La bala se dispara automáticamente al crearse

    def mover(self):
        if self.disparada:  # Si la bala ha sido disparada, moverla hacia arriba
            self.rect.y -= self.velocidad_bala
            if self.rect.y < 0:
                self.disparada = False

    def dibujar(self):
        if self.disparada:
            self.screen.blit(self.imagen, self.rect)




