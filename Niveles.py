import os
import pygame
from pygame.locals import *
from NaveJugador import Nave

class nivel1:
    def __init__(self, username):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0,0), pygame.RESIZABLE) #Hace que la ventana se ajuste a todo el tamaño de la pantalla  
        self.width, self.height = pygame.display.get_surface().get_size()
        pygame.mixer.init()
        
        self.username = username

        self.nave = Nave(self.pantalla, self.username) #Inicializa la clase Nave

        self.input_data = {
            "rifa_winner1": {"label": "Jugador: " + self.username, "pos": (8, 225), "text": ""}
        }

        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Carga las imágenes del GIF
        self.gif_images = []
        for filename in sorted(os.listdir('C://Users//Usuario//Desktop//GalactaTec//Animación Fondo')):
            if filename.endswith('.png'):  # Asegúrate de que la extensión coincide con la de tus imágenes
                imagen = pygame.image.load(os.path.join('C://Users//Usuario//Desktop//GalactaTec//Animación Fondo', filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0


    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                self.nave.mover(event) #Cada vez que se tocque una tecla se mueve una sola vez

            # Muestra la imagen actual del GIF
            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))

            # Avanza al siguiente fotograma del GIF cada 100 milisegundos
            if pygame.time.get_ticks() % 100 == 0:
                self.current_image = (self.current_image + 1) % len(self.gif_images)

            #Es una función que verifica que dentro de la clase si existe la foto de perfil
            if hasattr(self, 'imagen_perfil'):
                self.pantalla.blit(self.imagen_perfil, (8, 8))
            

            self.nave.dibujarBalas() #Se dibuja la nave

            self.loadPerfil() #Se dibuja la imagen de perfil
            self.draw_text_inputs() #Se dibujan los datos que se imprimen en la ventana

            self.nave.dibujar_puntos()

            self.nave.dibujar_vidas()
            
            pygame.display.flip()
            clock.tick(60)  # Limita el juego a 60 FPS
        pygame.quit()


    def loadPerfil (self):
        # Ruta al directorio para archivos del jugador
        ruta_directorio_carpetas = 'C://Users//Usuario//Desktop//GalactaTec//User files'
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
    

