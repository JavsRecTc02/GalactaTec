import pygame
from pygame.locals import *
import sys
import os
import csv
import webbrowser
from pygame import USEREVENT
import tkinter as tk
from tkinter import filedialog
import shutil
from Scores import ScoreWindow
from Niveles import nivel1
from RifaTurnoJugadores import rifaWindow
from ConfigPartida import ConfigPartida


class Menu:
    def __init__(self, username1, patron1, patron2, patron3):
        self.width = 800
        self.height = 600
        self.pantalla = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Menu de selección")
        self.user = username1

        self.input_data = { "rifa_winner1": {'label':'¡Bienvenido al menú de GalactaTEC!', "pos": (255, 65), "text": "", "color": (255,255,255)} }

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(r"C:\Users\Usuario\Desktop\GalactaTec\backgrounds\Menu_seleccion1.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.patron1 = patron1
        self.patron2 = patron2
        self.patron3 = patron3

        print(self.patron1, self.patron2, self.patron3)

    def draw_background(self):
        self.pantalla.blit(self.background_image, (0, 0))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.configuser_button.collidepoint(event.pos):
                            print("se presionó Configuser")
                            config = UsersConfig(self.user)
                            config.previous_instance = self
                            config.run()

                        if self.fama_button.collidepoint(event.pos):
                            scores_window = ScoreWindow(self.user)
                            scores_window.previous_instance = self
                            scores_window.run()


                        if self.ConfigPartida_button.collidepoint(event.pos):
                            config_partida = ConfigPartida(self.user, None, self.patron1, self.patron2, self.patron3)
                            config_partida.run()

                        if self.Jugador2_Button.collidepoint(event.pos):
                            from LoginPlayer2 import LoginPlayer2  
                            LoginPLayer2_window = LoginPlayer2(800, 600, self.user, self.patron1, self.patron2, self.patron3)
                            LoginPLayer2_window.run()


                        if self.Partida1_button.collidepoint(event.pos):
                            Nivel1_window = nivel1(self.user, None, 3, 0, 0, None, None, None, self.patron1, self.patron2, self.patron3)
                            Nivel1_window.run()

                        if self.Exit_button.collidepoint(event.pos):
                            running = False
                            pygame.quit()
                            sys.exit()

                        if self.Help_button.collidepoint(event.pos):
                            running = False
                            print("se presionó Ayuda")
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Usuario\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
                            Menu.run(self)
                            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        Nivel1_window = nivel1(self.user, None, 3, 0, 0, None, None, None, self.patron1, self.patron2, self.patron3)
                        Nivel1_window.run()

            self.draw_background()
            self.draw_text_inputs()
            self.draw_configuser_button()
            self.draw_fama_button()
            self.draw_ConfigPartida_button()
            self.draw_Jugador2_button()
            self.draw_Partida1_button()
            self.draw_Exit_button()
            self.draw_Help_button()
                

            pygame.display.flip()

        pygame.quit()
    
    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.pantalla.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)

    def draw_configuser_button(self):
        # Crea el botón en el centro de la ventana
        self.configuser_button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 200, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.configuser_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de Jugador', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.configuser_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_fama_button(self):
        # Crea el botón en el centro de la ventana
        self.fama_button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 140, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.fama_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salón de la fama', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.fama_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_ConfigPartida_button(self):
        # Crea el botón en el centro de la ventana
        self.ConfigPartida_button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 80, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.ConfigPartida_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Configuración de la partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.ConfigPartida_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Jugador2_button(self):
        # Crea el botón en el centro de la ventana
        self.Jugador2_Button = pygame.Rect(self.width // 2 - 125, self.height // 2 - 20, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Jugador2_Button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Iniciar Jugador 2', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Jugador2_Button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Partida1_button(self):
        # Crea el botón en el centro de la ventana
        self.Partida1_button = pygame.Rect(self.width // 2 - 125, self.height // 2 + 40, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Partida1_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Iniciar partida', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Partida1_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Exit_button(self):
        # Crea el botón en el centro de la ventana
        self.Exit_button = pygame.Rect(self.width // 2 - 125, self.height // 2 + 160, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Exit_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Salir del juego', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Exit_button.center)
        self.pantalla.blit(text_surface, text_rect)

    def draw_Help_button(self):
        # Crea el botón en el centro de la ventana
        self.Help_button = pygame.Rect(self.width // 2 - 125, self.height // 2 + 100, 250, 50)
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.Help_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ayuda', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.Help_button.center)
        self.pantalla.blit(text_surface, text_rect)


#VENTANA DE CONFIGURACION DEL user
class UsersConfig:
    def __init__(self, username,previous_instance=None):
        self.previous_instance = previous_instance
        #,previous_instance=None
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Configuración de user')
        self.clock = pygame.time.Clock()
        self.username = username
        self.font = pygame.font.Font(None, 30)
        self.data = self.load_user_data()
        self.editing_arch = False
        self.editing = None  # Variable para rastrear qué dato se está editando
        self.new_value = None  # Variable para almacenar el nuevo valor ingresado por el user
        self.profile_image = self.get_profile_image(self.username)
        self.ship_image = self.get_ship_image(self.username)
        self.profile_image_path = None
        self.spaceship_image_path = None
        self.user_song_path = None

        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(r"C:\Users\Usuario\Desktop\GalactaTec\backgrounds\ConfigPlayer.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # Rectángulos para botones de editar y confirmar/cancelar
        self.username_edit_rect = pygame.Rect(100, 120, 60, 30)
        self.nombre_edit_rect = pygame.Rect(100, 170, 60, 30)
        self.correo_edit_rect = pygame.Rect(100, 220, 60, 30)
        self.perfil_edit_rect = pygame.Rect(100, 220, 60, 30)
        self.spaceship_edit_rect = pygame.Rect(100, 220, 60, 30)
        self.song_edit_rect = pygame.Rect(100, 220, 60, 30)
        self.song_play_rect = pygame.Rect(100, 220, 60, 30)
        self.song_stop_rect = pygame.Rect(100, 220, 60, 30)
        self.confirm_button_rect = pygame.Rect(50, 500, 100, 50)
        self.cancel_button_rect = pygame.Rect(200, 500, 100, 50)
        self.confirm_arch_button_rect = pygame.Rect(50, 500, 100, 50)
        self.cancel_arch_button_rect = pygame.Rect(200, 500, 100, 50)

        # Configurar posiciones de los botones
        self.set_button_positions()

    def draw_background(self):
        self.screen.blit(self.background_image, (0, 0))


    def load_user_data(self):
    # Cargar los datos del user desde el archivo users.txt
        user_data = {}
        with open('users.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    username, nombre, correo, password = parts[:4]
                    user_data[username] = {'username': username, 'nombre': nombre, 'correo': correo, 'password': password}
        return user_data

    def set_button_positions(self):
        # Establecer posiciones de los botones según las necesidades
        self.username_edit_rect.topleft = (100, 70)
        self.nombre_edit_rect.topleft = (100, 170)
        self.correo_edit_rect.topleft = (100, 270)
        self.perfil_edit_rect.topleft = (510, 70)
        self.spaceship_edit_rect.topleft = (510, 170)
        self.song_edit_rect.topleft = (510, 270)
        self.song_play_rect.topleft = (510, 320)
        self.song_stop_rect.topleft = (580, 320)
        self.confirm_button_rect.topleft = (100, 400)
        self.cancel_button_rect.topleft = (200, 400)
        self.confirm_arch_button_rect.topleft = (510, 400)
        self.cancel_arch_button_rect.topleft = (620, 400)
        self.button_rect = pygame.Rect(700, 500, 80, 40)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.editing is not None:        #Si se esta editando un .txt
                        if self.confirm_button_rect.collidepoint(event.pos):
                            self.confirm_edit()
                        elif self.cancel_button_rect.collidepoint(event.pos):
                            self.cancel_edit()

                    elif self.editing_arch is not False: #Si se esta editando un archivo
                        if self.confirm_arch_button_rect.collidepoint(event.pos):
                            self.confirm_arch_edit()
                        elif self.cancel_arch_button_rect.collidepoint(event.pos):
                            self.cancel_edit()

                    elif self.username_edit_rect.collidepoint(event.pos):
                        self.start_editing('username')
                    elif self.nombre_edit_rect.collidepoint(event.pos):
                        self.start_editing('nombre')
                    elif self.correo_edit_rect.collidepoint(event.pos):
                        self.start_editing('correo')

                    elif self.perfil_edit_rect.collidepoint(event.pos):
                        #logica para subir una nueva  imagen de perfil
                        self.editing_arch = True
                        self.edit_select_file("profile_image")
                        print("editar perfil")

                    elif self.song_edit_rect.collidepoint(event.pos):
                        #logica para subir una nueva cancion
                        self.editing_arch = True
                        self.edit_select_file("user_song")
                        print ("editar musica")

                    elif self.song_play_rect.collidepoint(event.pos):
                        self.get_song_player()

                    elif self.song_stop_rect.collidepoint(event.pos):
                        self.stop_song()

                    elif self.spaceship_edit_rect.collidepoint(event.pos):
                        #logica para subir una nueva imagen de nave
                        self.editing_arch = True
                        self.edit_select_file("spaceship_image")
                        print("editar nave")

                    elif self.button_rect.collidepoint(event.pos): #BOTON PARA VOLVER ATRAS
                        if self.previous_instance is not None:
                                self.previous_instance.run()  # Llama al método run() de la instancia anterior
                        else:
                            pygame.quit()
                            return

                elif event.type == pygame.KEYDOWN:
                    if self.editing is not None:
                        if event.key == pygame.K_RETURN:
                            self.confirm_edit()
                        elif event.key == pygame.K_ESCAPE:
                            self.cancel_edit()
                        else:
                            # Agregar caracteres a la nueva entrada de texto
                            if event.key == pygame.K_BACKSPACE:
                                self.new_value = self.new_value[:-1]
                            else:
                                self.new_value += event.unicode

            self.draw_background()
            self.draw_user_data()
            pygame.display.flip()
            self.clock.tick(60)

    def get_profile_image(self, username):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if username in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, username)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                imagen_perfil = pygame.image.load(os.path.join(ruta_carpeta_user, archivo))
                return pygame.transform.scale(imagen_perfil, (80, 80))
        return None
    
    def get_ship_image(self, username):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if username in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, username)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('nave_espacial')]
            for archivo in archivos_perfil:
                imagen_perfil = pygame.image.load(os.path.join(ruta_carpeta_user, archivo))
                return pygame.transform.scale(imagen_perfil, (80, 80))
        return None
    
    def get_song_player(self):
        ruta_directorio_carpetas = r"C:\Users\Usuario\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if self.username in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, self.username)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_cancion = [archivo for archivo in archivos if archivo.startswith('cancion')]
            for archivo in archivos_cancion:
                ruta_cancion = os.path.join(ruta_carpeta_user, archivo)
                pygame.mixer.init()  # Inicializa el mixer
                pygame.mixer.music.load(ruta_cancion)
                pygame.mixer.music.set_volume(1.0)  # Ajusta el volumen
                pygame.mixer.music.play(-1)  # El -1 hará que la canción se repita indefinidamente

    #Funcion para detener la musica
    def stop_song(self):
        pygame.mixer.quit()

    def edit_select_file(self,file_type):
        root = tk.Tk()
        root.withdraw()  # Oculta la ventana principal de tkinter

        file_path = filedialog.askopenfilename()  # Abre un cuadro de diálogo para seleccionar un archivo
        if file_path:  # Verifica si se seleccionó un archivo
            if file_type == "spaceship_image":
                self.spaceship_image_path = file_path
            elif file_type == "profile_image":
                self.profile_image_path = file_path
            elif file_type == "user_song":
                self.user_song_path = file_path

    def save_images_and_song(self):
    # Obtener el nombre de user
        user_name = self.username
        # Ruta donde se guardará la carpeta del user
        user_folder = os.path.join(os.getcwd(), "User files", user_name)
        # Guardar los nuevos archivos
        if self.spaceship_image_path:
            shutil.copy(self.spaceship_image_path, os.path.join(user_folder, 'nave_espacial.png'))
        if self.profile_image_path:
            shutil.copy(self.profile_image_path, os.path.join(user_folder, 'perfil.png'))
        if self.user_song_path:
            shutil.copy(self.user_song_path, os.path.join(user_folder, 'cancion.mp3'))

        self.profile_image = self.get_profile_image(user_name)
        self.ship_image = self.get_ship_image(user_name)
        


    def draw_user_data(self):
        if self.username in self.data:

            jugador_label = self.font.render('Perfil', True, (255, 255, 255))
            self.screen.blit(jugador_label, (510, 50))  # Ajusta las coordenadas según tu diseño

            nave_label = self.font.render('Nave', True, (255, 255, 255))
            self.screen.blit(nave_label, (510, 150))  # Ajusta las coordenadas según tu diseño

            musica_label = self.font.render('Música', True, (255, 255, 255))
            self.screen.blit(musica_label, (510, 250)) 

            user_info = self.data[self.username]
            # Mostrar los datos del user en la ventana
            username_text = f'Usuario: {self.username}'
            username_rendered = self.font.render(username_text, True, (255, 255, 255))
            username_rect = username_rendered.get_rect(topleft=(100, 50))
            self.screen.blit(username_rendered, username_rect)

            nombre_text = f'Nombre: {user_info["nombre"]}'
            nombre_rendered = self.font.render(nombre_text, True, (255, 255, 255))
            nombre_rect = nombre_rendered.get_rect(topleft=(100, 150))
            self.screen.blit(nombre_rendered, nombre_rect)

            correo_text = f'Correo: {user_info["correo"]}'
            correo_rendered = self.font.render(correo_text, True, (255, 255, 255))
            correo_rect = correo_rendered.get_rect(topleft=(100, 250))
            self.screen.blit(correo_rendered, correo_rect)

            # Dibujar botón de editar para nombre, correo y user
            pygame.draw.rect(self.screen, (0, 0, 0), self.username_edit_rect)
            font = pygame.font.Font(None, 20)
            edit_username_text = font.render("Editar", True, (255, 255, 255))
            edit_username_rect = edit_username_text.get_rect(center=self.username_edit_rect.center)
            self.screen.blit(edit_username_text, edit_username_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.nombre_edit_rect)
            edit_nombre_text = font.render("Editar", True, (255, 255, 255))
            edit_nombre_rect = edit_nombre_text.get_rect(center=self.nombre_edit_rect.center)
            self.screen.blit(edit_nombre_text, edit_nombre_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.correo_edit_rect)
            edit_correo_text = font.render("Editar", True, (255, 255, 255))
            edit_correo_rect = edit_correo_text.get_rect(center=self.correo_edit_rect.center)
            self.screen.blit(edit_correo_text, edit_correo_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.perfil_edit_rect)
            edit_perfil_image = font.render("Editar", True, (255, 255, 255))
            edit_perfil_rect = edit_perfil_image.get_rect(center=self.perfil_edit_rect.center)
            self.screen.blit(edit_perfil_image, edit_perfil_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.song_edit_rect)
            edit_song_image = font.render("Editar", True, (255, 255, 255))
            edit_song_rect = edit_song_image.get_rect(center=self.song_edit_rect.center)
            self.screen.blit(edit_song_image, edit_song_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.song_play_rect)
            edit_song_play = font.render("Play", True, (255, 255, 255))
            play_song_rect = edit_song_play.get_rect(center=self.song_play_rect.center)
            self.screen.blit(edit_song_play, play_song_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.song_stop_rect)
            edit_song_stop = font.render("Stop", True, (255, 255, 255))
            stop_song_rect = edit_song_stop.get_rect(center=self.song_stop_rect.center)
            self.screen.blit(edit_song_stop, stop_song_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), self.spaceship_edit_rect)
            edit_spaceship_image = font.render("Editar", True, (255, 255, 255))
            edit_spaceship_image_rect = edit_spaceship_image.get_rect(center=self.spaceship_edit_rect.center)
            self.screen.blit(edit_spaceship_image, edit_spaceship_image_rect)

            pygame.draw.rect(self.screen, (100, 100, 100), self.button_rect)  # Dibuja el botón en un color gris
            font = pygame.font.Font(None, 24)
            text_surface = font.render('Back', True, (255, 255, 255))  # Renderiza el texto "Back"
            text_rect = text_surface.get_rect(center=self.button_rect.center)  # Centra el texto en el botón
            self.screen.blit(text_surface, text_rect)  # Dibuja el texto en el botón

            # Dibujar imagen de perfil si está disponible
            if self.profile_image:
                self.screen.blit(self.profile_image, (610, 50))  # Ajusta las coordenadas según tu diseño

            if self.ship_image:
                self.screen.blit(self.ship_image, (610,150))

            # Dibujar botones de confirmar/cancelar si se está editando los ARCHIVOS
            if self.editing_arch is not False:
                pygame.draw.rect(self.screen, (0, 255, 0), self.confirm_arch_button_rect)
                confirm_arch_text = self.font.render('Confirmar', True, (255, 255, 255))
                confirm_arch_rect = confirm_arch_text.get_rect(center=self.confirm_arch_button_rect.center)
                self.screen.blit(confirm_arch_text, confirm_arch_rect)

                pygame.draw.rect(self.screen, (255, 0, 0), self.cancel_arch_button_rect)
                cancel_arch_text = self.font.render('Cancelar', True, (255, 255, 255))
                cancel_arch_rect = cancel_arch_text.get_rect(center=self.cancel_arch_button_rect.center)
                self.screen.blit(cancel_arch_text, cancel_arch_rect)


            # Dibujar botones de confirmar/cancelar si se está editando los .TXT
            if self.editing is not None:
                pygame.draw.rect(self.screen, (0, 255, 0), self.confirm_button_rect)
                confirm_text = self.font.render('Confirmar', True, (255, 255, 255))
                confirm_rect = confirm_text.get_rect(center=self.confirm_button_rect.center)
                self.screen.blit(confirm_text, confirm_rect)

                pygame.draw.rect(self.screen, (255, 0, 0), self.cancel_button_rect)
                cancel_text = self.font.render('Cancelar', True, (255, 255, 255))
                cancel_rect = cancel_text.get_rect(center=self.cancel_button_rect.center)
                self.screen.blit(cancel_text, cancel_rect)

                 # Mostrar la nueva entrada de texto
                if self.editing == 'username':
                    new_text = self.font.render(self.new_value, True, (0, 0, 0))
                    new_rect = new_text.get_rect(topleft=(self.username_edit_rect.left + 70, self.username_edit_rect.top + 5))
                    self.screen.blit(new_text, new_rect)
                elif self.editing == 'nombre':
                    new_text = self.font.render(self.new_value, True, (0, 0, 0))
                    new_rect = new_text.get_rect(topleft=(self.nombre_edit_rect.left + 70, self.nombre_edit_rect.top + 5))
                    self.screen.blit(new_text, new_rect)
                elif self.editing == 'correo':
                    new_text = self.font.render(self.new_value, True, (0, 0, 0))
                    new_rect = new_text.get_rect(topleft=(self.correo_edit_rect.left + 70, self.correo_edit_rect.top + 5))
                    self.screen.blit(new_text, new_rect)

        else:
            # Si el user no existe en los datos, mostrar un mensaje de error
            error_text = 'user no encontrado'
            rendered_text = self.font.render(error_text, True, (255, 0, 0))
            text_rect = rendered_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(rendered_text, text_rect)

    def start_editing(self, field):
        self.editing = field
        self.new_value = self.data[self.username][field]
        
    def confirm_edit(self):
        new_username = None  # Inicializamos con None
        if self.editing is not None and self.new_value is not None:
            # Actualizar el valor en los datos del user
            if self.editing == 'username':
                old_username = self.username
                self.data[self.new_value] = self.data.pop(old_username)
                self.username = self.new_value
                new_username = self.new_value  # Almacenar el nuevo nombre de user

                # Renombrar la carpeta asociada al nombre de user
                old_folder_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec\User files", old_username)
                new_folder_path = os.path.join(r"C:\Users\Usuario\Desktop\GalactaTec\User files", self.new_value)
                os.rename(old_folder_path, new_folder_path)
            else:
                self.data[self.username][self.editing] = self.new_value
            # Guardar los cambios en el archivo users.txt
            with open('users.txt', 'w') as file:
                for username, info in self.data.items():
                    line = ','.join([username, info['nombre'], info['correo'], info['password']])
                    file.write(line + '\n')

        self.editing = None
        self.new_value = None
        print (new_username)  # Devolver el nuevo nombre de user

    def confirm_arch_edit(self):
        self.save_images_and_song()
        self.editing_arch = False

    def cancel_edit(self):
        self.editing_arch = False
        self.editing = None
        self.new_value = None



