import pygame
import math
import random

from NaveJugador import Nave
from PlayerBullets import BasicBullet

class Bala:
    def __init__(self, pantalla, x, y, fuerte=False):
        self.pantalla = pantalla
        self.fuerte = fuerte
        if fuerte:
            imagen_path = r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Bullets\PowerBullet.png"
        else:
            imagen_path = r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Bullets\EnemyBullet1.png"
        imagen_original = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(imagen_original, (50, 50))
        self.rect = self.imagen.get_rect(center=(x, y))
        self.velocidad = 8
    
    def mover(self):
        self.rect.y += self.velocidad

    def dibujar(self):
        self.pantalla.blit(self.imagen, self.rect)


class Enemigo:
    enemigos = []
    balas = []
    balas_fuertes_usadas = set()
    ultimo_disparo = pygame.time.get_ticks()
    tiempo_entre_disparos = 1000  # Milisegundos entre cada disparo
    tiempo_final_presentacion = 0
    espera_para_disparar = 2000  # 2000 milisegundos = 2 segundos
    altura_maxima_disparo = 0  # Se calculará al generar enemigos
    orden_disparo = []
    indice_actual_disparo = 0

    def __init__(self, pantalla, x, y, stop_y):
        self.pantalla = pantalla
        self.velocidad_bala = 8
        imagen_original = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Enemies\Enemie1.png")
        self.imagen = pygame.transform.scale(imagen_original, (50, 50))
        self.rect = self.imagen.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.moving = True
        self.stop_y = stop_y
        self.inicial_x = x
        self.inicial_y = y
        self.offset = (self.rect.x + self.rect.y) % (2 * math.pi)
        self.uso_fuerte = False

        # Cargar los sonidos
        self.sonido_disparo_basico = pygame.mixer.Sound(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Bullets\SonidoBasico.mp3")
        self.sonido_disparo_fuerte = pygame.mixer.Sound(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Bullets\SonidoFuerte.mp3")

    def movimientoPresentacion(self):
        if self.moving:
            self.rect.y += self.velocidad_bala
            if self.rect.y >= self.stop_y:
                self.moving = False

    def dibujarEnemigos(self):
        self.pantalla.blit(self.imagen, self.rect)

    def disparar(self):
        if not self.uso_fuerte:
            fuerte = random.random() < 0.90  # Aqui se cambia la probabilidad de que sea proyectil fuerte
            if fuerte:
                self.uso_fuerte = True
                Enemigo.balas_fuertes_usadas.add(self)
                self.sonido_disparo_fuerte.play()  # Reproduce el sonido fuerte
            else:
                self.sonido_disparo_basico.play()  # Reproduce el sonido básico
            bala = Bala(self.pantalla, self.rect.centerx, self.rect.bottom, fuerte=fuerte)
        else:
            bala = Bala(self.pantalla, self.rect.centerx, self.rect.bottom)
            self.sonido_disparo_basico.play()  # Reproduce el sonido básico si ya se usó el fuerte
        Enemigo.balas.append(bala)

    @classmethod
    def generar_enemigos(cls, pantalla, lineas):
        distancia_x = 100
        distancia_y = 150
        cls.altura_maxima_disparo = pantalla.get_height() * 3 / 4

        for i in range(lineas - 1, -1, -1):
            for j in range(i + 1):
                x = distancia_x * (2 * j - i) + pantalla.get_width() / 2
                y = -distancia_y * i
                stop_y = 100 + (lineas - i - 1) * 30
                enemigo = cls(pantalla, x, y, stop_y)
                cls.enemigos.append(enemigo)

        cls.orden_disparo = list(range(len(cls.enemigos)))
        random.shuffle(cls.orden_disparo)
        cls.indice_actual_disparo = 0

    @classmethod
    def actualizar(cls, nave_jugador):
        explosion_nave = pygame.mixer.Sound(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\Bullets\ExplosionNave.mp3")
        for enemigo in cls.enemigos[:]:
            enemigo.movimientoPresentacion()
            enemigo.dibujarEnemigos()

            # Comprobar colisión entre enemigos y la nave del jugador
            if enemigo.rect.colliderect(nave_jugador.rect):
                nave_jugador.perdidaVidas(1)
                # Opcional: eliminar el enemigo después de la colisión
                cls.enemigos.remove(enemigo)
                explosion_nave.play()
                cls.orden_disparo = list(range(len(cls.enemigos)))
                random.shuffle(cls.orden_disparo)

        # Verificar si todos los movimientos de presentación han terminado
        if cls.todos_movimientos_presentacion_terminados():
            # Si es la primera vez que se detecta el fin de la presentación, registrar el tiempo actual
            if cls.tiempo_final_presentacion == 0:
                cls.tiempo_final_presentacion = pygame.time.get_ticks()

            # Controlar los disparos secuenciales después de la espera
            tiempo_actual = pygame.time.get_ticks()
        
            if tiempo_actual - cls.tiempo_final_presentacion > cls.espera_para_disparar:
                if tiempo_actual - cls.ultimo_disparo > cls.tiempo_entre_disparos:
                    cls.ultimo_disparo = tiempo_actual
                    # Usar el operador módulo para asegurarnos de que el índice esté dentro del rango
                    cls.indice_actual_disparo %= len(cls.enemigos)
                    enemigo_para_disparar = cls.enemigos[cls.orden_disparo[cls.indice_actual_disparo]]
                    print("cls.indice_actual_disparo:", cls.indice_actual_disparo)
                    print("len(cls.orden_disparo):", len(cls.orden_disparo))
                    print("len(cls.enemigos):", len(cls.enemigos))
                    # Incrementar el índice después de usarlo
                    cls.indice_actual_disparo += 1
                    if not enemigo_para_disparar.moving and enemigo_para_disparar.rect.y <= cls.altura_maxima_disparo:
                        enemigo_para_disparar.disparar()
                    else:
                        # Si el índice actual está fuera de rango, reiniciar el índice y mezclar el orden de disparo
                        cls.indice_actual_disparo = 0
                        random.shuffle(cls.orden_disparo)

        # Mover y dibujar balas
        for bala in cls.balas[:]:
            bala.mover()
            bala.dibujar()

        # Comprobar colisión entre balas y la nave del jugador
            if bala.rect.colliderect(nave_jugador.rect):
                if bala.fuerte:
                    nave_jugador.perdidaVidas(nave_jugador.vidas)  # Resta todas las vidas
                else:
                    nave_jugador.perdidaVidas(0.5)
                # Eliminar la bala después de la colisión
                
                cls.balas.remove(bala)

    # Comprobar colisiones entre balas del jugador y los enemigos
        for bala_jugador in nave_jugador.balas[:]:
            cantidad = 200 #Aca se podria poner cuando debe cambiar la cantidad y asi 
            for enemigo in cls.enemigos[:]:  # Iterar sobre una copia de la lista de enemigos
                if bala_jugador.rect.colliderect(enemigo.rect):
                    # Eliminar el enemigo y la bala del jugador
                    cls.enemigos.remove(enemigo)
                    explosion_nave.play()
                    nave_jugador.incrementar_puntos(cantidad)
                    #cls.indice_actual_disparo -= 1
                    nave_jugador.balas.remove(bala_jugador)
                    cls.orden_disparo = list(range(len(cls.enemigos)))
                    break  # Salir del bucle interno después de manejar una colisión

    @classmethod
    def todos_movimientos_presentacion_terminados(cls):
        return all(not enemigo.moving for enemigo in cls.enemigos)
