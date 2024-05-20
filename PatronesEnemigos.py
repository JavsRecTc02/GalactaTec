import random
import math
class PatronesEnemigos:
    def __init__(self):
        self.zigzag_direction = 1
        self.time = 0

    def patron1(self, enemigos):
        velocidad_x = 5
        velocidad_y = 1

        for enemigo in enemigos:
            enemigo.rect.x += self.zigzag_direction * velocidad_x
            enemigo.rect.y += velocidad_y

            # Verificar si el enemigo sale por debajo de la pantalla
            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height  # Reposicionar el enemigo en la parte superior

        if any(enemigo.rect.x >= enemigo.pantalla.get_width() - enemigo.rect.width or enemigo.rect.x <= 0 for enemigo in enemigos):
            self.zigzag_direction *= -1


    def patron2(self, enemigos):
        radius = 100  # Radio del círculo
        speed = 0.05  # Velocidad de rotación
        self.time += speed

        for enemigo in enemigos:
            centro_x = enemigo.inicial_x
            centro_y = enemigo.inicial_y
            enemigo.rect.x = centro_x + radius * math.cos(self.time + enemigo.offset)
            enemigo.rect.y += 1  # Descenso continuo hacia abajo

            # Reaparece arriba manteniendo su comportamiento
            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height
                enemigo.rect.x = centro_x + radius * math.cos(self.time + enemigo.offset)


    def patron_descenso(self, enemigos):
        velocidad_y = 2  # Velocidad de movimiento hacia abajo

        for enemigo in enemigos:
            enemigo.rect.y += velocidad_y

            # Si el enemigo sale de la pantalla por abajo, reaparece arriba
            if enemigo.rect.y > enemigo.pantalla.get_height():
                enemigo.rect.y = -enemigo.rect.height
                enemigo.rect.x = random.randint(0, enemigo.pantalla.get_width() - enemigo.rect.width)
