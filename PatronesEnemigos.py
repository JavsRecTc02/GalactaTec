import math
import random

class PatronesEnemigos:
    def __init__(self):
        self.zigzag_direction = 1
        self.time = 0

#patrón en zigzag
    def patron1(self, enemigos):
        velocidad_x = 5
        velocidad_y = 1

        for enemigo in enemigos:
            enemigo.rect.x += self.zigzag_direction * velocidad_x
            enemigo.rect.y += velocidad_y

            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height

        if any(enemigo.rect.x >= enemigo.pantalla.get_width() - enemigo.rect.width or enemigo.rect.x <= 0 for enemigo in enemigos):
            self.zigzag_direction *= -1

#patrón en circulos
    def patron2(self, enemigos):
        radius = 100
        speed = 0.05
        self.time += speed

        for enemigo in enemigos:
            centro_x = enemigo.inicial_x
            centro_y = enemigo.inicial_y
            enemigo.rect.x = centro_x + radius * math.cos(self.time + enemigo.offset)
            enemigo.rect.y += 1

            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height
                enemigo.rect.x = centro_x + radius * math.cos(self.time + enemigo.offset)

#patrón de spawn superior aleatorio
    def patron_descenso(self, enemigos):
        velocidad_y = 2

        for enemigo in enemigos:
            enemigo.rect.y += velocidad_y

            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height
                enemigo.rect.x = random.randint(0, enemigo.pantalla.get_width() - enemigo.rect.width)

#patrón por división en columnas
    def patron3(self, enemigos):
        velocidad_x = 5
        velocidad_y = 1

        for i, enemigo in enumerate(enemigos):
            if i % 2 == 0:
                enemigo.rect.x += velocidad_x
            else:
                enemigo.rect.x -= velocidad_x
            enemigo.rect.y += velocidad_y

            if enemigo.rect.x > enemigo.pantalla.get_width():
                enemigo.rect.x = -enemigo.rect.width
            elif enemigo.rect.x < -enemigo.rect.width:
                enemigo.rect.x = enemigo.pantalla.get_width()

            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height


#patrón tipo senoidal
    def patron4(self, enemigos):
        velocidad_y = 2
        amplitud = 20
        frecuencia = 0.01
        self.time += frecuencia

        for enemigo in enemigos:
            enemigo.rect.x += amplitud * math.sin(self.time + enemigo.offset)
            enemigo.rect.y += velocidad_y

            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height
