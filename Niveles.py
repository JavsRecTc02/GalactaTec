import os
import random
import pygame
from pygame.locals import *
from NaveJugador import Nave
from Enemies import Enemigo
from PatronesEnemigos import PatronesEnemigos
from Bonus import Bonus_de_nivel
from Escudo import Escudo
from FinalizarJuego import FinalizarJuego 
from DoublePoints import DoublePoint

from TransicionesTurnos import windowLost1player
from TransicionesTurnos import windowLost1player_LVL2
from TransicionesTurnos import windowLost1player_LVL3

from TransicionesTurnos import windowLost2players
from TransicionesTurnos import windowLost2players_LVL2
from TransicionesTurnos import windowLost2players_LVL3

from Enemies import Enemigo
from Enemies import Enemigo_LVL2
from Enemies import Enemigo_LVL3

import ctypes
#Funcion para las ventanas de Error
def error_message(message):
    ctypes.windll.user32.MessageBoxW(0,message,"Notificación",1)


class nivel1:
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2, Nivel_player1, Nivel_player2, patron1, patron2, patron3):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0, 0),
                                                pygame.RESIZABLE)
        self.width, self.height = pygame.display.get_surface().get_size()
        pygame.mixer.init()

        self.username = username1
        self.username2 = username2

        self.vidas_player1 = vidas_player1
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = vidas_player2
        self.puntos_player2 = puntos_player2

        self.nivel_actual_player1 = Nivel_player1
        self.nivel_actual_player2 = Nivel_player2

        print([self.username,self.username2,self.vidas_player1,self.puntos_player1, self.vidas_player2,self.puntos_player2])
        
        self.nave = Nave(self.pantalla, self.username, self.vidas_player1, self.puntos_player1)  # Inicializa la clase Nave

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
        for filename in sorted(os.listdir(r"C:\Users\Usuario\Desktop\GalactaTec\Animación Fondo")):
            if filename.endswith('.png'):  # Solamente los archivos png
                imagen = pygame.image.load(
                    os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec\Animación Fondo", filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0

        self.volume_up_button = pygame.Rect(70, 625, 50, 50)  # Botón para aumentar el volumen
        self.volume_down_button = pygame.Rect(10, 625, 50, 50)  # Botón para disminuir el volumen

        self.escudo = Escudo(self.pantalla, self.nave, 3)
        self.puntos_dobles = DoublePoint(self.pantalla, self.nave)

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.paused = False  # Cambio aquí: inicializa la variable de pausa

        bonus = Bonus_de_nivel(self.pantalla, self.nave)
        bonus_timer = 0
        bonus_interval = random.randint(5000, 15000)

        bonus_count = 0

        self.loadMusic()

        Enemigo.generar_enemigos(self.pantalla, 6)

        self.escudo_dibujado = False  # Añade esta línea en la inicialización de tu clase
        self.aura =  False

        patrones = PatronesEnemigos()
        while self.running and not self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
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
                        selected_bonus = bonus.select_bonus()
                        if selected_bonus == 'extra_life':
                            if self.nave.vidas >= 4.5:
                                self.nave.ganarVidas(0)
                            else:
                                self.nave.ganarVidas(1)
                        if selected_bonus == 'shield':
                            self.escudo_dibujado = True
                        if selected_bonus ==  'double_points':
                            self.aura = True
                    if event.key == pygame.K_ESCAPE:  # Cambio aquí: agrega el manejo del evento KEYDOWN para la tecla Escape
                        self.paused = not self.paused  # Cambia el estado de pausa
                      
                self.nave.mover(event)
                
            if self.paused:  # Cambio aquí: si el juego está en pausa, salta el resto del bucle
                continue


            pygame.mixer.init()

            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))
                

            if pygame.time.get_ticks() - bonus_timer > bonus_interval:
                if random.random() < 0.01 and bonus_count < 5:
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

            if Enemigo.enemigos:  # Esto retornará False si la lista está vacía
                Enemigo.actualizar(self.nave, self.escudo, self.puntos_dobles) #Aca se manda a la funcion 

            if Enemigo.todos_movimientos_presentacion_terminados():
                if self.patron1 == 1:
                    patrones.patron1(Enemigo.enemigos) #Zigzag

                elif self.patron1 == 2:
                    patrones.patron2(Enemigo.enemigos) #Ciruclos 

                elif self.patron1 == 3:
                    patrones.patron_descenso(Enemigo.enemigos) #Descenso Aleatorio

                elif self.patron1 == 4:
                    patrones.patron3(Enemigo.enemigos) #Columnas divididas

                elif self.patron1 == 5:
                    patrones.patron4(Enemigo.enemigos) #Senoidal
            
            if Enemigo.cambio_turno(self.nave):
                if self.username2 != None:
                    if self.nivel_actual_player2 == 1:
                        pygame.mixer.quit()
                        Enemigo.reiniciar()
                        Enemigo.eliminar_todos_enemigos()
                        ventana=windowLost2players(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()

                    elif self.nivel_actual_player2 == 2:
                        pygame.mixer.quit()
                        Enemigo.reiniciar()
                        Enemigo.eliminar_todos_enemigos()
                        ventana=windowLost2players_LVL2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2,self.patron1, self.patron2, self.patron3)
                        ventana.run()

                    elif self.nivel_actual_player2 == 3:
                        pygame.mixer.quit()
                        Enemigo.reiniciar()
                        Enemigo.eliminar_todos_enemigos()
                        ventana=windowLost2players_LVL3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()

                    elif self.nivel_actual_player2 == 4:
                        error_message(self.username2 + " ya completó los 3 niveles," + self.username + " vas a jugar el mismo nivel")
                        if self.nivel_actual_player1 == 1:
                            pygame.mixer.quit()
                            Enemigo.reiniciar()
                            Enemigo.eliminar_todos_enemigos()
                            ventana=nivel1(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                            ventana.run()

                        elif self.nivel_actual_player1 == 2:
                            pass

                        elif self.nivel_actual_player1  == 3:
                            pass

                else:
                    pygame.mixer.quit()
                    Enemigo.reiniciar()
                    Enemigo.eliminar_todos_enemigos()
                    ventana=windowLost1player(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.patron1, self.patron2, self.patron3)
                    ventana.run()
                continue
                

            if Enemigo.juego_terminado(self.nave):
                if self.username2 != None:
                    print("Dos Jugadores")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, self.username2, self.nave.puntos, self.puntos_player2)
                    juego_terminado.run()
                else:
                    print("Un jugador")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, None, self.nave.puntos, None)
                    juego_terminado.run()
                continue

            if Enemigo.cambio_nivel():
                if self.username2 != None:
                    self.nivel_actual_player1 = 2
                    pygame.mixer.quit()
                    Enemigo.reiniciar()
                    Enemigo.eliminar_todos_enemigos()
                    ventana=nivel2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                    ventana.run()
                else:
                    pygame.mixer.quit()
                    Enemigo.reiniciar()
                    Enemigo.eliminar_todos_enemigos()
                    ventana=nivel2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, None, None, self.patron1, self.patron2, self.patron3)
                    ventana.run()

            if self.escudo_dibujado:
                self.escudo.draw()

            if self.aura:
                self.puntos_dobles.draw()

            pygame.display.flip()
            clock.tick(60)

        if self.game_over:  # Salir del bucle principal si el juego ha finalizado
            print("Juego Finalizado")
            pygame.quit()
            self.running = False
            return  # Salir del método run()


    def loadPerfil1(self):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if
                    os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, self.username)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                self.imagen_perfil1 = pygame.image.load(os.path.join(ruta_carpeta_user, archivo))
                self.imagen_perfil1 = pygame.transform.scale(self.imagen_perfil1, (150, 200))
            self.pantalla.blit(self.imagen_perfil1, (8, 8))

    def loadPerfil2(self):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if
                    os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username2 in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, self.username2)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                self.imagen_perfil2 = pygame.image.load(os.path.join(ruta_carpeta_user, archivo))
                self.imagen_perfil2 = pygame.transform.scale(self.imagen_perfil2, (150, 200))
            self.pantalla.blit(self.imagen_perfil2, (1120, 8))

    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])

    def loadMusic(self):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if
                    os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, self.username)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_cancion = [archivo for archivo in archivos if archivo.startswith('cancion')]
            for archivo in archivos_cancion:
                ruta_cancion = os.path.join(ruta_carpeta_user, archivo)
                #pygame.mixer.init()
                pygame.mixer.music.load(ruta_cancion)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(-1)

###########################################################################################################################
###########################################################################################################################
class nivel2(nivel1):
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2, Nivel_player1, Nivel_player2, patron1, patron2, patron3):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0, 0),
                                                pygame.RESIZABLE)
        self.width, self.height = pygame.display.get_surface().get_size()
        pygame.mixer.init()

        self.username = username1
        self.username2 = username2

        self.vidas_player1 = vidas_player1
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = vidas_player2
        self.puntos_player2 = puntos_player2

        self.nivel_actual_player1 = Nivel_player1
        self.nivel_actual_player2 = Nivel_player2

        print([self.username,self.username2,self.vidas_player1,self.puntos_player1, self.vidas_player2,self.puntos_player2])
        
        self.nave = Nave(self.pantalla, self.username, self.vidas_player1, self.puntos_player1)  # Inicializa la clase Nave

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
        for filename in sorted(os.listdir(r"C:\Users\Usuario\Desktop\GalactaTec\Animación LVL2")):
            if filename.endswith('.png'):  # Solamente los archivos png
                imagen = pygame.image.load(
                    os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec\Animación LVL2", filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0

        self.volume_up_button = pygame.Rect(70, 625, 50, 50)  # Botón para aumentar el volumen
        self.volume_down_button = pygame.Rect(10, 625, 50, 50)  # Botón para disminuir el volumen

        self.escudo = Escudo(self.pantalla, self.nave, 3)
        self.puntos_dobles = DoublePoint(self.pantalla, self.nave)

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.paused = False  # Cambio aquí: inicializa la variable de pausa

        bonus = Bonus_de_nivel(self.pantalla, self.nave)
        bonus_timer = 0
        bonus_interval = random.randint(5000, 15000)

        bonus_count = 0

        self.loadMusic(r'C:\Users\Usuario\Desktop\GalactaTec\Animación LVL2\LVL2.mp3')

        Enemigo_LVL2.generar_enemigos(self.pantalla, 6)

        self.escudo_dibujado = False  # Añade esta línea en la inicialización de tu clase
        self.aura =  False

        patrones = PatronesEnemigos()
        while self.running and not self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
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
                        selected_bonus = bonus.select_bonus()
                        if selected_bonus == 'extra_life':
                            if self.nave.vidas >= 4.5:
                                self.nave.ganarVidas(0)
                            else:
                                self.nave.ganarVidas(1)
                        if selected_bonus == 'shield':
                            self.escudo_dibujado = True
                        if selected_bonus ==  'double_points':
                            self.aura = True
                    if event.key == pygame.K_ESCAPE:  # Cambio aquí: agrega el manejo del evento KEYDOWN para la tecla Escape
                        self.paused = not self.paused  # Cambia el estado de pausa
                      
                self.nave.mover(event)
                
            if self.paused:  # Cambio aquí: si el juego está en pausa, salta el resto del bucle
                continue


            pygame.mixer.init()

            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))
                

            if pygame.time.get_ticks() - bonus_timer > bonus_interval:
                if random.random() < 0.01 and bonus_count < 5:
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

            if Enemigo_LVL2.enemigos:  # Esto retornará False si la lista está vacía
                Enemigo_LVL2.actualizar(self.nave, self.escudo, self.puntos_dobles) #Aca se manda a la funcion 

            if Enemigo_LVL2.todos_movimientos_presentacion_terminados():
                if self.patron2 == 1:
                    patrones.patron1(Enemigo_LVL2.enemigos) #Zigzag
                    
                elif self.patron2 == 2:
                    patrones.patron2(Enemigo_LVL2.enemigos) #Ciruclos 

                elif self.patron2 == 3:
                    patrones.patron_descenso(Enemigo_LVL2.enemigos) #Descenso Aleatorio

                elif self.patron2 == 4:
                    patrones.patron3(Enemigo_LVL2.enemigos) #Columnas divididas

                elif self.patron2 == 5:
                    patrones.patron4(Enemigo_LVL2.enemigos) #Senoidal
            
            if Enemigo_LVL2.cambio_turno(self.nave):
                if self.username2 != None:
                    if self.nivel_actual_player2 == 1:
                        pygame.mixer.quit()
                        Enemigo_LVL2.reiniciar()
                        Enemigo_LVL2.eliminar_todos_enemigos()
                        ventana=windowLost2players(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()
                    elif self.nivel_actual_player2 == 2:
                        pygame.mixer.quit()
                        Enemigo_LVL2.reiniciar()
                        Enemigo_LVL2.eliminar_todos_enemigos()
                        ventana=windowLost2players_LVL2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()
                    elif self.nivel_actual_player2 == 3:
                        pygame.mixer.quit()
                        Enemigo_LVL2.reiniciar()
                        Enemigo_LVL2.eliminar_todos_enemigos()
                        ventana=windowLost2players_LVL3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()

                else:
                    pygame.mixer.quit()
                    Enemigo_LVL2.reiniciar()
                    Enemigo_LVL2.eliminar_todos_enemigos()
                    ventana=windowLost1player_LVL2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.patron1, self.patron2, self.patron3)
                    ventana.run()
                continue
                

            if Enemigo_LVL2.juego_terminado(self.nave):
                if self.username2 != None:
                    print("Dos Jugadores")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, self.username2, self.nave.puntos, self.puntos_player2)
                    juego_terminado.run()
                else:
                    print("Un jugador")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, None, self.nave.puntos, None)
                    juego_terminado.run()
                continue
                

            if Enemigo_LVL2.cambio_nivel():
                if self.username2 != None:
                    self.nivel_actual_player1 = 3
                    pygame.mixer.quit()
                    Enemigo_LVL2.reiniciar()
                    Enemigo_LVL2.eliminar_todos_enemigos()
                    ventana=nivel3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                    ventana.run()
                else:
                    pygame.mixer.quit()
                    Enemigo_LVL2.reiniciar()
                    Enemigo_LVL2.eliminar_todos_enemigos()
                    ventana=nivel3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                    ventana.run()

            if self.escudo_dibujado:
                self.escudo.draw()

            if self.aura:
                self.puntos_dobles.draw()

            pygame.display.flip()
            clock.tick(60)

        if self.game_over:  # Salir del bucle principal si el juego ha finalizado
            print("Juego Finalizado")
            pygame.quit()
            self.running = False
            return  # Salir del método run()   
        
    def loadMusic(self, ruta_cancion):
        #pygame.mixer.init()
        pygame.mixer.music.load(ruta_cancion)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

        

###########################################################################################################################
###########################################################################################################################
class nivel3(nivel1):
    def __init__(self, username1, username2, vidas_player1, puntos_player1, vidas_player2, puntos_player2, Nivel_player1, Nivel_player2, patron1, patron2, patron3):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.pantalla = pygame.display.set_mode((0, 0),
                                                pygame.RESIZABLE)
        self.width, self.height = pygame.display.get_surface().get_size()
        pygame.mixer.init()

        self.username = username1
        self.username2 = username2

        self.vidas_player1 = vidas_player1
        self.puntos_player1 = puntos_player1

        self.vidas_player2 = vidas_player2
        self.puntos_player2 = puntos_player2

        self.nivel_actual_player1 = Nivel_player1
        self.nivel_actual_player2 = Nivel_player2

        print([self.username,self.username2,self.vidas_player1,self.puntos_player1, self.vidas_player2,self.puntos_player2])
        
        self.nave = Nave(self.pantalla, self.username, self.vidas_player1, self.puntos_player1)  # Inicializa la clase Nave

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
        for filename in sorted(os.listdir(r"C:\Users\Usuario\Desktop\GalactaTec\Animación LVL3")):
            if filename.endswith('.png'):  # Solamente los archivos png
                imagen = pygame.image.load(
                    os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec\Animación LVL3", filename))
                # Redimensiona la imagen para que se ajuste a la ventana
                imagen_escalada = pygame.transform.scale(imagen, (self.width, self.height))
                self.gif_images.append(imagen_escalada)
        self.current_image = 0

        self.volume_up_button = pygame.Rect(70, 625, 50, 50)  # Botón para aumentar el volumen
        self.volume_down_button = pygame.Rect(10, 625, 50, 50)  # Botón para disminuir el volumen

        self.escudo = Escudo(self.pantalla, self.nave, 3)
        self.puntos_dobles = DoublePoint(self.pantalla, self.nave)

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.paused = False  # Cambio aquí: inicializa la variable de pausa

        bonus = Bonus_de_nivel(self.pantalla, self.nave)
        bonus_timer = 0
        bonus_interval = random.randint(5000, 15000)

        bonus_count = 0

        self.loadMusic(r'C:\Users\Usuario\Desktop\GalactaTec\Animación LVL3\LVL3.mp3')

        Enemigo_LVL3.generar_enemigos(self.pantalla, 6)

        self.escudo_dibujado = False  # Añade esta línea en la inicialización de tu clase
        self.aura =  False

        patrones = PatronesEnemigos()
        while self.running and not self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
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
                        selected_bonus = bonus.select_bonus()
                        if selected_bonus == 'extra_life':
                            if self.nave.vidas >= 4.5:
                                self.nave.ganarVidas(0)
                            else:
                                self.nave.ganarVidas(1)
                        if selected_bonus == 'shield':
                            self.escudo_dibujado = True
                        if selected_bonus ==  'double_points':
                            self.aura = True
                    if event.key == pygame.K_ESCAPE:  # Cambio aquí: agrega el manejo del evento KEYDOWN para la tecla Escape
                        self.paused = not self.paused  # Cambia el estado de pausa
                      
                self.nave.mover(event)
                
            if self.paused:  # Cambio aquí: si el juego está en pausa, salta el resto del bucle
                continue


            pygame.mixer.init()

            self.pantalla.blit(self.gif_images[self.current_image], (0, 0))
                

            if pygame.time.get_ticks() - bonus_timer > bonus_interval:
                if random.random() < 0.01 and bonus_count < 5:
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

            if Enemigo_LVL3.enemigos:  # Esto retornará False si la lista está vacía
                Enemigo_LVL3.actualizar(self.nave, self.escudo, self.puntos_dobles) #Aca se manda a la funcion 

            
            if Enemigo_LVL3.todos_movimientos_presentacion_terminados():
                if self.patron3 == 1:
                    patrones.patron1(Enemigo_LVL3.enemigos) #Zigzag
                    
                elif self.patron3 == 2:
                    patrones.patron2(Enemigo_LVL3.enemigos) #Ciruclos 

                elif self.patron3 == 3:
                    patrones.patron_descenso(Enemigo_LVL3.enemigos) #Descenso Aleatorio

                elif self.patron3 == 4:
                    patrones.patron3(Enemigo_LVL3.enemigos) #Columnas divididas

                elif self.patron3 == 5:
                    patrones.patron4(Enemigo_LVL3.enemigos) #Senoidal
            
            if Enemigo_LVL3.cambio_turno(self.nave):
                if self.username2 != None:
                    if self.nivel_actual_player2 == 1:
                        pygame.mixer.quit()
                        Enemigo_LVL3.reiniciar()
                        Enemigo_LVL3.eliminar_todos_enemigos()
                        ventana=windowLost2players(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()
                    elif self.nivel_actual_player2 == 2:
                        pygame.mixer.quit()
                        Enemigo_LVL3.reiniciar()
                        Enemigo_LVL3.eliminar_todos_enemigos()
                        ventana=windowLost2players_LVL2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()
                    elif self.nivel_actual_player2 == 3:
                        pygame.mixer.quit()
                        Enemigo_LVL3.reiniciar()
                        Enemigo_LVL3.eliminar_todos_enemigos()
                        ventana=windowLost2players_LVL3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                        ventana.run()
                else:
                    pygame.mixer.quit()
                    Enemigo_LVL3.reiniciar()
                    Enemigo_LVL3.eliminar_todos_enemigos()
                    ventana=windowLost1player_LVL3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.patron1, self.patron2, self.patron3)
                    ventana.run()
                continue
                

            if Enemigo_LVL3.juego_terminado(self.nave):
                if self.username2 != None:
                    print("Dos Jugadores")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, self.username2, self.nave.puntos, self.puntos_player2)
                    juego_terminado.run()
                else:
                    print("Un jugador")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, None, self.nave.puntos, None)
                    juego_terminado.run()
                continue


            if Enemigo_LVL3.cambio_nivel():
                if self.username2 != None:
                    self.nivel_actual_player1 = 4
                    if self.nivel_actual_player1 and self.nivel_actual_player2 == 4:
                        print("Dos jugadores")
                        self.game_over = True
                        pygame.mixer.quit()
                        juego_terminado = FinalizarJuego(self.username, self.username2, self.nave.puntos, None)
                        juego_terminado.run()
                    else:
                        if self.nivel_actual_player2 == 1:
                            pygame.mixer.quit()
                            Enemigo_LVL2.reiniciar()
                            Enemigo_LVL2.eliminar_todos_enemigos()
                            ventana=windowLost2players(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                            ventana.run()
                        elif self.nivel_actual_player2 == 2:
                            pygame.mixer.quit()
                            Enemigo_LVL2.reiniciar()
                            Enemigo_LVL2.eliminar_todos_enemigos()
                            ventana=windowLost2players_LVL2(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                            ventana.run()
                        elif self.nivel_actual_player2 == 3:
                            pygame.mixer.quit()
                            Enemigo_LVL2.reiniciar()
                            Enemigo_LVL2.eliminar_todos_enemigos()
                            ventana=windowLost2players_LVL3(self.username, self.username2, self.nave.vidas, self.nave.puntos, self.vidas_player2, self.puntos_player2, self.nivel_actual_player1, self.nivel_actual_player2, self.patron1, self.patron2, self.patron3)
                            ventana.run()
                else:
                    print("Un jugador")
                    self.game_over = True
                    pygame.mixer.quit()
                    juego_terminado = FinalizarJuego(self.username, None, self.nave.puntos, None)
                    juego_terminado.run()

            if self.escudo_dibujado:
                self.escudo.draw()

            if self.aura:
                self.puntos_dobles.draw()

            pygame.display.flip()
            clock.tick(60)

        if self.game_over:  # Salir del bucle principal si el juego ha finalizado
            print("Juego Finalizado")
            pygame.quit()
            self.running = False
            return  # Salir del método run() 

    def loadMusic(self, ruta_cancion):
        #pygame.mixer.init()
        pygame.mixer.music.load(ruta_cancion)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
 