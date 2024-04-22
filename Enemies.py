import pygame

class Enemigo:
    enemigos = []
    def __init__(self, pantalla, x, y, stop_y):
        self.pantalla = pantalla
        self.velocidad_bala = 3
        imagen_original = pygame.image.load(r"C:\Users\Usuario\Desktop\GalactaTec\Enemies\Enemie1.png")  # Carga la imagen de la bala
        self.imagen = pygame.transform.scale(imagen_original, (50, 50))  # Ajusta el tamaño de la imagen
        self.rect = self.imagen.get_rect()

        # Ajusta la posición del rectángulo para que la imagen aparezca en la parte superior central de la ventana
        self.rect.centerx = x  # Centra horizontalmente
        self.rect.y = y  # Inicia en la posición y proporcionada

        # Añade una variable de estado para controlar el movimiento
        self.moving = True

        self.stop_y = stop_y  # Añade una variable para la posición y donde se debe detener el enemigo

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
        distancia_x = 50
        distancia_y = 30

        for i in range(lineas):
            for j in range(lineas - i):  # Modifica esta línea para generar más enemigos en las primeras líneas
                x = distancia_x * (2*j - (lineas - i - 1)) + pantalla.get_width() / 2
                y = -distancia_y * i  # Inicia las naves fuera de la ventana
                stop_y = 100 + i * 30  # Cada fila de enemigos se detendrá 50 píxeles más abajo que la anterior
                enemigo = cls(pantalla, x, y, stop_y)
                cls.enemigos.append(enemigo)

    @classmethod
    def actualizar(cls):
        for Enemigo in cls.enemigos:
            Enemigo.movimientoPresentacion()
            Enemigo.dibujarEnemigos()
