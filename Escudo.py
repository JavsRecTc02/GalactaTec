import pygame

class Escudo:
    def __init__(self, screen, player, estado):
        self.screen = screen
        self.player = player
        self.imagenes_escudos = [pygame.Surface((100, 100), pygame.SRCALPHA),
                                 pygame.transform.scale(pygame.image.load(r'C:\Users\Usuario\Desktop\GalactaTec-1\Escudo\Escudo1.png'), (100, 100)),
                                 pygame.transform.scale(pygame.image.load(r'C:\Users\Usuario\Desktop\GalactaTec-1\Escudo\Escudo2.png'), (100, 100)),
                                 pygame.transform.scale(pygame.image.load(r'C:\Users\Usuario\Desktop\GalactaTec-1\Escudo\Escudo3.png'), (100, 100))]  # Añade una imagen vacía
        self.estado = estado  # Ajusta el estado inicial
        self.rect = self.imagenes_escudos[self.estado].get_rect()  # Añade un atributo 'rect' a la clase 'Escudo'
        self.hits_fuerte = 0  # Añade un contador para los golpes de balas fuertes

    def update(self):
        # Esto cambiará la imagen que se muestra
        self.estado = (self.estado - 1) % len(self.imagenes_escudos)
        self.rect = self.imagenes_escudos[self.estado].get_rect()  # Actualiza el atributo 'rect' cada vez que se actualiza el estado

    def draw(self):
        # Solo dibuja el escudo si el estado es diferente de 0
        if self.estado != 0:
            # Dibuja la imagen del escudo en frente de la nave del jugador
            imagen_escudo = self.imagenes_escudos[self.estado]
            x = self.player.rect.x  # Aquí se accede al atributo 'rect' del objeto 'player'
            y = self.player.rect.y - imagen_escudo.get_height() / 2 - 50  # Mueve la imagen 60 píxeles hacia arriba
            self.screen.blit(imagen_escudo, (x, y))
            self.rect.topleft = (x, y)  # Actualiza la posición del rectángulo del escudo
