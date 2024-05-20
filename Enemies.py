import pygame
import math

class Enemigo:
    enemigos = []

    def __init__(self, pantalla, x, y, stop_y):
        self.pantalla = pantalla
        self.velocidad_bala = 1
        imagen_original = pygame.image.load(
            r"C:\Users\killt\Desktop\proyecto_principios\Enemies\Enemie1.png")  # Carga la imagen del enemigo
        self.imagen = pygame.transform.scale(imagen_original, (50, 50))  # Ajusta el tamaño de la imagen
        self.rect = self.imagen.get_rect()

        # Ajusta la posición del rectángulo para que la imagen aparezca en la parte superior central de la ventana
        self.rect.centerx = x  # Centra horizontalmente
        self.rect.y = y  # Inicia en la posición y proporcionada

        # Añade una variable de estado para controlar el movimiento
        self.moving = True
        self.stop_y = stop_y  # Añade una variable para la posición y donde se debe detener el enemigo

        # Almacenar la posición inicial para el patrón circular
        self.inicial_x = x
        self.inicial_y = y
        self.offset = (self.rect.x + self.rect.y) % (2 * math.pi)  # Offset para el patrón circular

    def movimientoPresentacion(self):
        # Si el enemigo está en movimiento, actualiza su posición
        if self.moving:
            self.rect.y += self.velocidad_bala
            # Si el enemigo ha llegado a la posición deseada, detén el movimiento
            if self.rect.y >= self.stop_y:  # Usa la variable stop_y para determinar dónde se debe detener el enemigo
                self.moving = False

    def dibujarEnemigos(self):
        self.pantalla.blit(self.imagen, self.rect)

    @classmethod
    def generar_enemigos(cls, pantalla, lineas):
        distancia_x = 100
        distancia_y = 150

        for i in range(lineas - 1, -1, -1):  # Invierte el orden de generación
            for j in range(i + 1):  # Modifica esta línea para invertir la formación de los enemigos
                x = distancia_x * (2 * j - i) + pantalla.get_width() / 2
                y = -distancia_y * i  # Inicia las naves fuera de la ventana
                stop_y = 100 + (
                            lineas - i - 1) * 30  # Cada fila de enemigos se detendrá 50 píxeles más abajo que la anterior
                enemigo = cls(pantalla, x, y, stop_y)
                cls.enemigos.append(enemigo)

    @classmethod
    def actualizar(cls):
        for enemigo in cls.enemigos:
            enemigo.movimientoPresentacion()
            enemigo.dibujarEnemigos()
