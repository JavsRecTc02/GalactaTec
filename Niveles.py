import os
import random
from Bonus import Bonus_de_nivel
import pygame
from pygame.locals import *
from pygame import *
from NaveJugador import Nave
from Enemies import Enemigo


class nivel1:
    def __init__(self, username1, username2):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0,0), pygame.RESIZABLE) #Hace que la ventana se ajuste a todo el tamaño de la pantalla  
        self.width, self.height = pygame.display.get_surface().get_size()
        pygame.mixer.init()

        self.username = username1
        self.username2 = username2

        self.nave = Nave(self.pantalla, self.username) #Inicializa la clase Nave

        if self.username2 != None:
            self.input_data = {
                "rifa_winner1": {"label": "Jugador: " + self.username, "pos": (8, 225), "text": ""},
                "rifa_winner2": {"label": "Jugador2: " + self.username2, "pos": (1090, 225), "text": ""}
            }
        
        else:
            self.input_data = {
                "rifa_winner1": {"label": "Jugador: " + self.username, "pos": (8, 225), "text": ""}
            }

        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga las imágenes del GIF
        self.gif_images = []
        for filename in sorted(os.listdir(r"C:\Users\Usuario\Desktop\GalactaTec\Animación Fondo")):
            if filename.endswith('.png'):  # Solamente los archivos png
                imagen = pygame.image.load(os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec\Animación Fondo", filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0

        self.volume_slider = pygame.Rect(20, 620, 200, 50)  # Rectangulo para controlar el volumen


    def run(self):
        clock = pygame.time.Clock()
        running = True

        bonus = Bonus_de_nivel(self.pantalla, self.nave)
        bonus_timer = 0
        bonus_interval = random.randint(5000,15000)  # Intervalo de tiempo aleatorio (entre 5 y 15 segundos) entre la aparición de bonus

        # Contador de bonus generados
        bonus_count = 0

        self.loadMusic() # Reproduce la musica de fondo escogida por el usuario

        Enemigo.generar_enemigos(self.pantalla, 6)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.volume_slider.collidepoint(event.pos):
                        volume = ((event.pos[0] - self.volume_slider.x)/self.volume_slider.width)
                        pygame.mixer.music.set_volume(volume) #Permite controlar el volumen con el rectangulo
                elif event.type == pygame.KEYDOWN:  # Verificar si se presionó alguna tecla
                    if event.key == pygame.K_a:  # Verificar si la tecla presionada fue 'a'
                        bonus.move_selection_up()
                    if event.key == pygame.K_z:
                        bonus.move_selection_down()
                    if event.key == pygame.K_x:
                        bonus.select_bonus()
                self.nave.mover(event) #Cada vez que se tocque una tecla se realiza la acción una sola vez



            pygame.mixer.init()

            # Muestra la imagen actual del GIF
            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))

            if pygame.time.get_ticks() - bonus_timer > bonus_interval:
                # Generar un número aleatorio entre 0 y 1 para determinar la probabilidad de que aparezca un bono
                # Solo generar un bono si no se han generado 5 bonus ya
                if random.random() < 0.001 and bonus_count < 5:  # Umbral de probabilidad de 0.3 
                    bonus.active = True
                    bonus_timer = pygame.time.get_ticks()
                    # Establecer un nuevo intervalo de tiempo aleatorio para la próxima aparición de bono
                    bonus_interval = random.randint(5000, 15000)  # Intervalo de tiempo aleatorio entre 5 y 15 segundos
                    bonus_count += 1  # Incrementar el contador de bonus

            if bonus.active:  # Si el bonus está activo, lo actualizamos y dibujamos en cada iteración
                bonus.draw()
                bonus.update()
                bonus.check_collision()
            bonus.draw_bonus_bar()

            self.nave.dibujar_vidas()

            self.nave.dibujar_vidas()

            # Avanza al siguiente fotograma del GIF cada 100 milisegundos
            if pygame.time.get_ticks() % 80 == 0:
                self.current_image = (self.current_image + 1) % len(self.gif_images)

 

            self.nave.dibujarBalas() #Se dibuja la nave

            self.loadPerfil1() #Se dibuja la imagen de perfil
            if self.username2 is not None:
                self.loadPerfil2() #Se dibuja la imagen de perfil del jugador 2 solo si username2 no es None

            self.draw_text_inputs() #Se dibujan los datos que se imprimen en la ventana

            self.nave.dibujar_puntos()

            pygame.draw.rect(self.pantalla, (255, 255, 255), self.volume_slider)

            # Actualiza los enemigos en cada iteración del bucle
            Enemigo.actualizar()

            pygame.display.flip()
            clock.tick(60)  # Limita el juego a 60 FPS
        pygame.quit()


    def loadPerfil1 (self):
        # Ruta al directorio para archivos del jugador
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
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
                self.imagen_perfil1 = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                # Redimensiona la imagen para que se ajuste a la ventana
                self.imagen_perfil1 = pygame.transform.scale(self.imagen_perfil1, (150, 200))

            self.pantalla.blit(self.imagen_perfil1, (8,8))

    def loadPerfil2 (self):
        # Ruta al directorio para archivos del jugador
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        # Obtiene una lista de todas las carpetas en el directorio
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]

        # Clasifica las carpetas por nombre
        carpetas.sort()
        if self.username2 in carpetas:
            # Ruta a la carpeta del usuario
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username2)
            # Obtiene una lista de todos los archivos en la carpeta del usuario
            archivos = os.listdir(ruta_carpeta_usuario)
            # Busca los archivos que se llamen "perfil"
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                # Carga la imagen
                self.imagen_perfil2 = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                # Redimensiona la imagen para que se ajuste a la ventana
                self.imagen_perfil2 = pygame.transform.scale(self.imagen_perfil2, (150, 200))
            self.pantalla.blit(self.imagen_perfil2, (1120, 8))

    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)

    def loadMusic(self):
        # Ruta al directorio para archivos del jugador
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        # Obtiene una lista de todas las carpetas en el directorio
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        # Clasifica las carpetas por nombre
        carpetas.sort()
        if self.username in carpetas:
            # Ruta a la carpeta del usuario
            ruta_carpeta_usuario = os.path.join(ruta_directorio_carpetas, self.username)
            # Obtiene una lista de todos los archivos en la carpeta del usuario
            archivos = os.listdir(ruta_carpeta_usuario)
            # Busca los archivos que se llamen "cancion"
            archivos_cancion = [archivo for archivo in archivos if archivo.startswith('cancion')]
            for archivo in archivos_cancion:
                # Carga la canción
                ruta_cancion = os.path.join(ruta_carpeta_usuario, archivo)
                pygame.mixer.init()  # Inicializa el mixer
                pygame.mixer.music.load(ruta_cancion)
                pygame.mixer.music.set_volume(1.0)  # Ajusta el volumen
                pygame.mixer.music.play(-1)  # El -1 hará que la canción se repita indefinidamente
