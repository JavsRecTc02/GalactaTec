import pygame
from pygame import *
import os
from PlayerBullets import BasicBullet

class Nave:
    def __init__(self, pantalla, username):
        self.pantalla = pantalla
        self.username = username
        self.velocidad = 100  # Define la velocidad de la nave
        self.imagen = self.loadNave()  # Carga la imagen de la nave
        self.rect = self.imagen.get_rect()
        self.rect.center = (self.pantalla.get_width() / 2, self.pantalla.get_height() - self.rect.height / 2)  # Posiciona la nave en el centro de la pantalla
        self.balas = []  # Lista para almacenar las balas disparadas
        self.sonido_disparo_basico = pygame.mixer.Sound('C://Users//Usuario//Desktop//GalactaTec//Bullets//SonidoBasico.mp3')  # Carga el sonido del disparo basico
        self.sonido_movimiento = pygame.mixer.Sound('C://Users//Usuario//Desktop//GalactaTec//Bullets//MovimientoNave.mp3')
        self.sonido_movimiento.set_volume(0.3)
        pygame.mixer.init()
        self.puntos = 0

        self.imagen_vida = pygame.image.load('C://Users//Usuario//Desktop//GalactaTec//Vidas\Vida1.png')
        self.vidas = 3


    def mover(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.rect.top > 0:  # Mover hacia arriba
                self.rect.y -= self.velocidad
                self.sonido_movimiento.play()
            if event.key == pygame.K_DOWN and self.rect.bottom < self.pantalla.get_height():  # Mover hacia abajo
                self.rect.y += self.velocidad
                self.sonido_movimiento.play()
            if event.key == pygame.K_LEFT and self.rect.left > 0:  # Mover hacia la izquierda
                self.rect.x -= self.velocidad
                self.sonido_movimiento.play()
            if event.key == pygame.K_RIGHT and self.rect.right < self.pantalla.get_width():  # Mover hacia la derecha
                self.rect.x += self.velocidad
                self.sonido_movimiento.play()
            if event.key == pygame.K_SPACE:  # Disparar una bala
                bassic_bullet = BasicBullet(self.pantalla)
                bassic_bullet.rect.center = self.rect.center  # Posiciona la bala en el centro de la nave
                self.balas.append(bassic_bullet)
                self.sonido_disparo_basico.play()  # Reproduce el sonido del disparo
                
                self.incrementar_puntos(200)

    def dibujarBalas(self):
        self.pantalla.blit(self.imagen, self.rect)
        # Dibuja todas las balas
        for bala in self.balas:
            bala.dibujar()
            bala.mover()

    def dibujar_vidas(self):
        self.imagen_vida = pygame.transform.scale(self.imagen_vida, (100, 100))
        # Dibuja la imagen en la parte inferior izquierda de la pantalla con un margen de 10 píxeles
        self.pantalla.blit(self.imagen_vida, (10, self.pantalla.get_height() - self.imagen_vida.get_height() - 10))

        fuente = pygame.font.Font(None, 20)  # Crea una fuente
        texto = fuente.render('Vidas totales: '+str(self.vidas), True, (255, 255, 255))  # Crea un objeto de texto
        self.pantalla.blit(texto, (100, self.pantalla.get_height() - self.imagen_vida.get_height() + 26))  # Dibuja el texto en la pantalla

    def perdidaVidas(self, cantidad):
        self.vidas -= cantidad  #Metodo para bajar la cantidad de vidas de los jugadores

    def ganarVidas(self, cantidad):
        self.vidas += cantidad #Metodo para subir la cantidad de vidas de los jugadores
        if self.vidas == 5:
            self.vidas 

    def loadNave(self):
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
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('nave_espacial')]
            for archivo in archivos_perfil:
                # Carga la imagen
                imagen_nave = pygame.image.load(os.path.join(ruta_carpeta_usuario, archivo))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_nave = pygame.transform.scale(imagen_nave, (100, 100))
                return imagen_nave  # Devuelve la imagen cargada
        
    def incrementar_puntos(self, cantidad):
        self.puntos += cantidad  # Incrementa los puntos

    def dibujar_puntos(self):
        fuente = pygame.font.Font(None, 36)  # Crea una fuente
        texto = fuente.render('Puntos: ' + str(self.puntos), True, (255, 0, 0))  # Crea un objeto de texto
        self.pantalla.blit(texto, (10, 240))  # Dibuja el texto en la pantalla


