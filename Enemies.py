import math

import pygame
import math

class Enemigo:
    enemigos = []

    def __init__(self, pantalla, x, y, stop_y):
        self.pantalla = pantalla
        self.velocidad_bala = 1
        imagen_original = pygame.image.load(r"C:\Users\killt\Desktop\proyecto_principios\Enemies\Enemie1.png")
        self.imagen = pygame.transform.scale(imagen_original, (50, 50))
        self.rect = self.imagen.get_rect()

        self.rect.centerx = x
        self.rect.y = y
        self.moving = True
        self.stop_y = stop_y

        self.inicial_x = x
        self.inicial_y = y
        self.offset = (self.rect.x + self.rect.y) % (2 * math.pi)

    def movimientoPresentacion(self):
        if self.moving:
            self.rect.y += self.velocidad_bala
            if self.rect.y >= self.stop_y:
                self.moving = False

    def dibujarEnemigos(self):
        self.pantalla.blit(self.imagen, self.rect)

    @classmethod
    def generar_enemigos(cls, pantalla, lineas):
        distancia_x = 100
        distancia_y = 150

        for i in range(lineas - 1, -1, -1):
            for j in range(i + 1):
                x = distancia_x * (2 * j - i) + pantalla.get_width() / 2
                y = -distancia_y * i
                stop_y = 100 + (lineas - i - 1) * 30
                enemigo = cls(pantalla, x, y, stop_y)
                cls.enemigos.append(enemigo)

    @classmethod
    def actualizar(cls):
        for enemigo in cls.enemigos:
            enemigo.movimientoPresentacion()
            enemigo.dibujarEnemigos()

    @classmethod
    def todos_movimientos_presentacion_terminados(cls):
        return all(not enemigo.moving for enemigo in cls.enemigos)
