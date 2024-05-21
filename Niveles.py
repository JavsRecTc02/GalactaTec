import os
import random
import pygame
from pygame.locals import *
from NaveJugador import Nave
from Enemies import Enemigo
from PatronesEnemigos import PatronesEnemigos
from Bonus import Bonus_de_nivel

class nivel1:
    def __init__(self, username1, username2):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0, 0),
                                                pygame.RESIZABLE)
        self.width, self.height = pygame.display.get_surface().get_size()
        pygame.mixer.init()

        self.username = username1
        self.username2 = username2

        self.nave = Nave(self.pantalla, self.username)  # Inicializa la clase Nave

        if self.username2 != None:
            self.input_data = {
                "rifa_winner1": {"label": "Jugador: " + self.username, "pos": (8, 225), "text": ""},
                "rifa_winner2": {"label": "Jugador2: " + self.username2, "pos": (1090, 225), "text": ""},
                "subir": {"label": "+", "pos": (90, 640), "text": ""},
                "bajar": {"label": "-", "pos": (32, 640), "text": ""}
            }

        else:
            self.input_data = {
                "rifa_winner1": {"label": "Jugador: " + self.username, "pos": (8, 225), "text": ""},
                "subir": {"label": "+", "pos": (90, 640), "text": ""},
                "bajar": {"label": "-", "pos": (32, 640), "text": ""}
            }

        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga las imágenes del GIF
        self.gif_images = []
        for filename in sorted(os.listdir(r"C:\Users\killt\Desktop\proyecto_principios\Animación Fondo")):
            if filename.endswith('.png'):  # Solamente los archivos png
                imagen = pygame.image.load(
                    os.path.join(r"C:\Users\killt\Desktop\proyecto_principios\Animación Fondo", filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0

        self.volume_up_button = pygame.Rect(70, 625, 50, 50)  # Botón para aumentar el volumen
        self.volume_down_button = pygame.Rect(10, 625, 50, 50)  # Botón para disminuir el volumen

    def run(self):
        clock = pygame.time.Clock()
        running = True

        bonus = Bonus_de_nivel(self.pantalla, self.nave)
        bonus_timer = 0
        bonus_interval = random.randint(5000, 15000)

        bonus_count = 0

        self.loadMusic()

        Enemigo.generar_enemigos(self.pantalla, 6)

        patrones = PatronesEnemigos()
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.volume_up_button.collidepoint(event.pos):
                        volume = min(pygame.mixer.music.get_volume() + 0.1, 1)
                        pygame.mixer.music.set_volume(volume)
                    elif self.volume_down_button.collidepoint(event.pos):
                        volume = max(pygame.mixer.music.get_volume() - 0.1, 0)
                        pygame.mixer.music.set_volume(volume)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        bonus.move_selection_up()
                    if event.key == pygame.K_z:
                        bonus.move_selection_down()
                    if event.key == pygame.K_x:
                        if bonus.select_bonus() == 'vida':
                            self.nave.ganarVidas(1)
                self.nave.mover(event)

            pygame.mixer.init()

            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))

            if pygame.time.get_ticks() - bonus_timer > bonus_interval:
                if random.random() < 0.001 and bonus_count < 5:
                    bonus.active = True
                    bonus_timer = pygame.time.get_ticks()
                    bonus_interval = random.randint(5000, 15000)
                    bonus_count += 1

            if bonus.active:
                bonus.draw()
                bonus.update()
                bonus.check_collision()
            bonus.draw_bonus_bar()

            self.nave.dibujar_vidas()

            if pygame.time.get_ticks() % 80 == 0:
                self.current_image = (self.current_image + 1) % len(self.gif_images)

            self.nave.dibujarBalas()

            self.loadPerfil1()
            if self.username2 is not None:
                self.loadPerfil2()

            self.nave.dibujar_puntos()

            pygame.draw.rect(self.pantalla, (0, 0, 0), self.volume_up_button)
            pygame.draw.rect(self.pantalla, (0, 0, 0), self.volume_down_button)

            self.draw_text_inputs()

            Enemigo.actualizar()

            if Enemigo.todos_movimientos_presentacion_terminados():
                #patrones.patron_descenso(Enemigo.enemigos)
                #patrones.patron3(Enemigo.enemigos)
                patrones.patron4(Enemigo.enemigos)

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def loadPerfil1(self):
        ruta_directorio_carpetas = r"C:\Users\killt\Desktop\proyecto_principios\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if
                    os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username in carpetas:
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username)
            archivos = os.listdir(ruta_carpeta_usuario)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                self.imagen_perfil1 = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                self.imagen_perfil1 = pygame.transform.scale(self.imagen_perfil1, (150, 200))
            self.pantalla.blit(self.imagen_perfil1, (8, 8))

    def loadPerfil2(self):
        ruta_directorio_carpetas = r"C:\Users\killt\Desktop\proyecto_principios\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if
                    os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username2 in carpetas:
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username2)
            archivos = os.listdir(ruta_carpeta_usuario)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                self.imagen_perfil2 = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                self.imagen_perfil2 = pygame.transform.scale(self.imagen_perfil2, (150, 200))
            self.pantalla.blit(self.imagen_perfil2, (1120, 8))

    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])

    def loadMusic(self):
        ruta_directorio_carpetas = r"C:\Users\killt\Desktop\proyecto_principios\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if
                    os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username in carpetas:
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username)
            archivos = os.listdir(ruta_carpeta_usuario)
            archivos_cancion = [archivo for archivo in archivos if archivo.startswith('cancion')]
            for archivo in archivos_cancion:
                ruta_cancion = os.path.join(ruta_carpeta_usuario, archivo)
                pygame.mixer.init()
                pygame.mixer.music.load(ruta_cancion)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(-1)
