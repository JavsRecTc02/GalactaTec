import pygame

class DoublePoint:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.imagenes_auras = [pygame.Surface((90, 90), pygame.SRCALPHA), pygame.transform.scale(pygame.image.load(r'C:\Users\Usuario\Desktop\GalactaTec\imagenes_bonus\aura.png'), (110, 110))]
        self.font = pygame.font.Font(None, 30)  # Define la fuente para el contador
        self.start_ticks = None  # Inicializa el contador en None
        self.active = False

    def draw(self):
        if self.start_ticks is None:  # Si es la primera vez que se dibuja
            self.start_ticks = pygame.time.get_ticks()  # Inicializa el contador en el tiempo actual

        # Calcula los segundos que han pasado desde la activación del contador
        seconds = 16 - (pygame.time.get_ticks() - self.start_ticks) / 1000

        if seconds > 0:  # Si han pasado menos de 15 segundos
            # Dibuja el contador en la pantalla
            text = self.font.render('¡Puntos Dobles por '+str(int(seconds))+' segundos!', True, (255, 0, 0))
            self.screen.blit(text, (10, 270))  # Ajusta la posición según necesites
            image = self.imagenes_auras[1]  # Usa la imagen en el índice 1 de la lista
            self.active = True
        else:
            image = self.imagenes_auras[0]  # Usa la imagen en el índice 0 de la lista
            self.active = False

        # Asumiendo que 'player' tiene atributos 'x' y 'y' que representan su posición
        x = self.player.rect.x  # Aquí se accede al atributo 'rect' del objeto 'player'
        y = self.player.rect.y  # Mueve la imagen 60 píxeles hacia arriba
        self.screen.blit(image, (x, y))
