import pygame
import random
import os

import os

class Bonus_de_nivel:
    def __init__(self, screen, player):
        # Inicialización de la clase Bonus_de_nivel
        self.screen = screen  # Pantalla en la que se dibujará el bonus
        self.player = player  # Jugador al que se asociará el bonus
        self.active = False  # Estado del bonus (activo o inactivo)
        self.bonus_types = ["expansive_shot", "pursuer_shot", "double_points", "shield",
                            "extra_life"]  # Tipos de bonos disponibles

        # Cargar imágenes de bonos y su versión en blanco y negro
        self.bonus_images = {}
        for bonus_type in self.bonus_types:
            self.load_bonus_images(bonus_type)

        # Cargar y escalar las imágenes de la animación del bonus
        self.bonus_animation = self.load_bonus_animation()

        # Cargar y escalar la imagen del bonus principal
        self.image_path = r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus\diamante.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Obtener el rectángulo de la imagen principal
        self.rect = self.image.get_rect()

        # Generar posición inicial aleatoria en el eje x
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)

        # Posición inicial en el eje y
        self.rect.y = 0

        # Velocidad de desplazamiento del bonus
        self.speed = 2

        # Lista de bonos obtenidos por el jugador
        self.bonus_obtained = []

        # Índice de la imagen actual de la animación del bonus
        self.current_animation_image = 0

        #Indice del bono seleccionando en la barra de bonos
        self.selected_bonus_index = 0

        # Diccionario para almacenar el estado de cada bono
        self.bonus_status = {bonus_type: False for bonus_type in self.bonus_types}

    def load_bonus_images(self, bonus_type):
        # Carga y escala las imágenes de bonos y su versión en blanco y negro
        image_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus", bonus_type + ".png")
        bn_image_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus", bonus_type + "_bn.png")

        image = pygame.image.load(image_path)
        bn_image = pygame.image.load(bn_image_path)

        self.bonus_images[bonus_type] = pygame.transform.scale(image, (100, 100))
        self.bonus_images[bonus_type + "_bn"] = pygame.transform.scale(bn_image, (100, 100))

    def load_bonus_animation(self):
        # Carga y escala las imágenes de la animación del bonus
        bonus_animation = []
        for filename in sorted(os.listdir(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus")):
            if filename.endswith('.png'):
                image_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus", filename)
                image = pygame.image.load(image_path)
                image_escalada = pygame.transform.scale(image, (100, 100))
                bonus_animation.append(image_escalada)
        return bonus_animation

    def show_bonus_animation(self):
        # Mostrar la animación del bonus en la pantalla
        self.screen.blit(self.bonus_animation[self.current_animation_image], (self.player.rect.x, self.player.rect.y))
        self.current_animation_image = (self.current_animation_image + 1) % len(self.bonus_animation)  # Ciclo de animación

    def draw_bonus_bar(self):
        # Dibujar la barra de bonos en la pantalla
        y = self.screen.get_height()  # Iniciar en la parte inferior de la pantalla
        for i, bonus_type in enumerate(self.bonus_types):
            # Obtener la imagen correspondiente al tipo de bono en blanco y negro
            image = pygame.transform.scale(self.bonus_images[bonus_type + "_bn"], (100, 100))
            # Si el bono está seleccionado, dibujar un rectángulo alrededor
            if i == self.selected_bonus_index:
                pygame.draw.rect(self.screen, (255, 255, 255), (self.screen.get_width() - image.get_width(), y - image.get_height(), image.get_width(), image.get_height()), 2)
            # Dibujar la imagen en la pantalla
            self.screen.blit(image, (self.screen.get_width() - image.get_width(), y - image.get_height()))
            y -= image.get_height()  # Mover hacia arriba para el próximo bono

    def move_selection_up(self):
        # Mover la selección hacia arriba en la barra de bonos
        self.selected_bonus_index = (self.selected_bonus_index + 1) % len(self.bonus_types)

    def move_selection_down(self):
        # Mover la selección hacia abajo en la barra de bonos
        self.selected_bonus_index = (self.selected_bonus_index - 1) % len(self.bonus_types)

    def select_bonus(self):
        # Seleccionar el bonus en el que está colocado el cuadrado de la barra de bonus
        selected_bonus_type = self.bonus_types[self.selected_bonus_index]

        # Verificar si el bono seleccionado está activo
        if self.bonus_status[selected_bonus_type]:
            self.bonus_status[selected_bonus_type] = False  # Desactivar el bono después de usarlo
            bn_image_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus",
                                        selected_bonus_type + "_bn.png")
            bn_image = pygame.image.load(bn_image_path)
            self.bonus_images[selected_bonus_type + "_bn"] = pygame.transform.scale(bn_image, (100, 100))

            return selected_bonus_type  # Retornar el tipo de bono seleccionado



    def draw(self):
        # Dibujar el bonus en la pantalla si está activo
        if self.active:
            self.screen.blit(self.image, self.rect)

    def update(self):
        # Actualizar la posición del bonus si está activo y desactivarlo si alcanza el borde inferior de la pantalla
        if self.active:
            self.rect.y += self.speed
            if self.rect.y > self.screen.get_height():
                self.deactivate()

    def check_collision(self):
        # Verificar la colisión entre el jugador y el bonus
        if self.active and self.player.rect.colliderect(self.rect):
            self.play_sound()
            self.activate_bonus()
            self.deactivate()
            self.show_bonus_animation()

            if len(self.bonus_obtained) == len(self.bonus_types):
                self.active = False  # Detiene la aparición de bonos si ya se han obtenido todos

    def activate_bonus(self):
        # Activar un nuevo bonus si no se han obtenido todos los bonos disponibles
        if len(self.bonus_obtained) < len(self.bonus_types):
            available_bonuses = [bonus for bonus in self.bonus_types if bonus not in self.bonus_obtained]
            if available_bonuses:
                self.current_bonus = random.choice(available_bonuses)
                self.bonus_obtained.append(self.current_bonus)

                if self.current_bonus:
                    self.show_bonus_animation()
                    if self.current_bonus == "expansive_shot":
                        self.player.expansive_shot = True
                    elif self.current_bonus == "pursuer_shot":
                        self.player.pursuer_shot = True
                    elif self.current_bonus == "double_points":
                        self.player.double_points = True
                    elif self.current_bonus == "shield":
                        self.player.shield = True
                    elif self.current_bonus == "extra_life":
                        self.player.extra_life = True

                    # Actualizar el estado del bono en el diccionario
                    self.bonus_status[self.current_bonus] = True

                    # Actualizar la imagen correspondiente en la barra de bonos para que se muestre en color
                    bn_image_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus",
                                                self.current_bonus + "_bn.png")
                    color_image_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus",
                                                    self.current_bonus + ".png")
                    bn_image = pygame.image.load(bn_image_path)
                    color_image = pygame.image.load(color_image_path)
                    self.bonus_images[self.current_bonus + "_bn"] = pygame.transform.scale(color_image, (100, 100))
        else:
            self.active = False  # Detiene la aparición de bonos si ya se han obtenido todos    

    def deactivate(self):
        # Desactivar el bonus y reiniciar su posición
        self.active = False
        self.rect.y = 0
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)

    def play_sound(self):
        sonido = pygame.mixer.Sound(r"C:\Users\Usuario\Desktop\GalactaTec-1\imagenes_bonus\sonido_bonus.mp3")
        sonido.set_volume(1.0)  # Ajusta el volumen al máximo
        sonido.play()
