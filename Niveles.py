import os
import pygame
from pygame.locals import *
from Bonus import Bonus_de_nivel
from NaveJugador import Nave
pygame.mixer.init()
import random
class nivel1:
    def __init__(self, username):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0,0), pygame.RESIZABLE) #Hace que la ventana se ajuste a
        self.width, self.height = pygame.display.get_surface().get_size()
        
        self.username = username


        self.nave = Nave(self.pantalla, self.username) #Inicializa la clase Nave


        self.input_data = {
            "rifa_winner1": {"label": "Jugador: " + self.username, "pos": (8, 225), "text": ""}
        }

        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga las imágenes del GIF
        self.gif_images = []
        #cambiar para que funcione en cualquier computadora
        for filename in sorted(os.listdir(r"C:\Users\killt\Documents\GitHub\GalactaTec\Animación Fondo")):
            if filename.endswith('.png'):  # Asegúrate de que la extensión coincide con la de tus imágenes
                #cambar para que funcione en cualquier computadora
                imagen = pygame.image.load(os.path.join(r"C:\Users\killt\Documents\GitHub\GalactaTec\Animación Fondo", filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0

    def run(self):
        clock = pygame.time.Clock()
        running = True
        bonus = Bonus_de_nivel(self.pantalla, self.nave)
        bonus_timer = 0
        bonus_interval = random.randint(5000,15000)  # Intervalo de tiempo aleatorio (entre 5 y 15 segundos) entre la aparición de bonus

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Muestra la imagen actual del GIF
            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))

            if pygame.time.get_ticks() - bonus_timer > bonus_interval:
                # Generar un número aleatorio entre 0 y 1 para determinar la probabilidad de que aparezca un bono
                if random.random() < 0.001:  # Umbral de probabilidad de 0.3 (ajustable según desees)
                    bonus.active = True
                    bonus_timer = pygame.time.get_ticks()
                    # Establecer un nuevo intervalo de tiempo aleatorio para la próxima aparición de bono
                    bonus_interval = random.randint(5000, 15000)  # Intervalo de tiempo aleatorio entre 5 y 15 segundos

            if bonus.active:  # Si el bonus está activo, lo actualizamos y dibujamos en cada iteración
                bonus.draw()
                bonus.update()
                bonus.check_collision()

            bonus.draw_bonus_bar()

            # Avanza al siguiente fotograma del GIF cada 100 milisegundos
            if pygame.time.get_ticks() % 100 == 0:
                self.current_image = (self.current_image + 1) % len(self.gif_images)

            # Es una función que verifica que dentro de la clase si existe la foto de perfil
            if hasattr(self, 'imagen_perfil'):
                self.pantalla.blit(self.imagen_perfil, (8, 8))

            self.loadPerfil()
            self.draw_text_inputs()

            keys = pygame.key.get_pressed()
            self.nave.mover(keys)
            self.nave.dibujar()

            pygame.display.flip()
            clock.tick(60)  # Limita el juego a 60 FPS
        pygame.quit()


    def loadPerfil (self):
        # Ruta al directorio para archivos del jugador
        #cambar para que funcione en cualquier computadora
        ruta_directorio_carpetas = r"C:\Users\killt\Documents\GitHub\GalactaTec\User files"
        # Obtiene una lista de todas las carpetas en el directorio
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]

        # Clasifica las carpetas por nombre
        carpetas.sort()
        if self.username in carpetas:
            # Ruta a la carpeta del usuario
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username)
            # Obtiene una lista de todos los archivos en la carpeta del usuario
            archivos = os.listdir(ruta_carpeta_usuario)
            # Busca los archivos que se llamen "perfil"
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                # Carga la imagen
                self.imagen_perfil = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                # Redimensiona la imagen para que se ajuste a la ventana
                self.imagen_perfil = pygame.transform.scale(self.imagen_perfil, (150, 200))

    
    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)
    

