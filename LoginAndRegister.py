import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import filedialog
import re
import os
import shutil

import Niveles
from RifaTurnoJugadores import rifaWindow

#Ventana de Inicio
class WelcomeWindow:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Welcome")
        pygame.mixer.init()

        self.WHITE = (255, 255, 255)
        self.back_button_visible = False
    #Dibujar los botones de login y register
    def draw_buttons(self):
        login_button = pygame.Rect(215, 450, 180, 100)
        pygame.draw.rect(self.window, (0, 0, 0), login_button)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Login', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=login_button.center)
        self.window.blit(text_surface, text_rect)

        register_button = pygame.Rect(400, 450, 180, 100)
        pygame.draw.rect(self.window, (0, 0, 0), register_button)
        text_surface = font.render('Register', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=register_button.center)
        self.window.blit(text_surface, text_rect)

        if self.back_button_visible:
            self.draw_back_button()

    def draw_back_button(self):
        back_button = pygame.Rect(520, 520, 100, 50)
        pygame.draw.rect(self.window, (150, 150, 150), back_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Back', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=back_button.center)
        self.window.blit(text_surface, text_rect)

    def show_back_button(self):
        self.back_button_visible = True

    def hide_back_button(self):
        self.back_button_visible = False

    def run(self):  #Eventos de click
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if 215 <= x <= 390 and 450 <= y <= 550:
                            login_window = LoginWindow(self.width, self.height)
                            pygame.display.set_caption("Login")
                            login_window.run()
                        elif 400 <= x <= 575 and 450 <= y <= 550:
                            register_window = RegisterWindow(self.width, self.height)
                            pygame.display.set_caption("Register")
                            register_window.run()

            self.window.fill(self.WHITE)
            self.draw_buttons()
            pygame.display.flip()

        pygame.quit()

#Clase Login - heredada de la clase welcome_window
class LoginWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.welcome_window = WelcomeWindow()
        self.welcome_window.show_back_button()
        self.user_data = self.load_user_data()
        # Define las coordenadas y rectángulos para los campos de entrada
        self.input_data = {
            "user_name": {"label": "User Name:", "pos": (150, 270), "rect": pygame.Rect(215, 300, 400, 50), "active": False, "text": ""},
            "user_password": {"label": "Password:", "pos": (150, 370), "rect": pygame.Rect(215, 400, 400, 50), "active": False, "text": ""}
        }
        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

    #Funcion que carga los strings de info de cada user, para verificar 
    def load_user_data(self):
        user_data = {}
        with open("users.txt", "r") as file:
            for line in file:
                # Dividir la línea en cuatro partes
                parts = line.strip().split(",")
                username = parts[0]
                password = parts[3]  # La contraseña es el cuarto elemento
                user_data[username] = password
            return user_data
        
    #Bucle de la ventana de login
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for field in self.input_data.values():
                            if field["rect"].collidepoint(event.pos):
                                field["active"] = True
                            else:
                                field["active"] = False
                        # Verificar si se hizo clic en el botón "Back"
                        if 520 <= event.pos[0] <= 595 and 520 <= event.pos[1] <= 580:
                            self.welcome_window.hide_back_button()
                            pygame.display.set_caption("Welcome")
                            return "back"
                        # Verificar si se hizo clic en el botón "Entry"
                        elif self.width - 150 <= event.pos[0] <= self.width - 50 and self.height - 80 <= event.pos[1] <= self.height - 30:
                            #Verificar si el username y contrasena coinciden
                            username = self.input_data["user_name"]["text"]
                            password = self.input_data["user_password"]["text"]
                            if username in self.user_data:
                                if self.user_data[username] == password:
                                    print("Loggeado")

                                    #mandaria a la la clase main del juego
                                    niveles_window = Niveles.nivel1(username)
                                    niveles_window.run()

                                    #En teoría esta clase lleva a las opciones que hace gabriel
                                    #y de esas al juego, de momento se pone asi para probar el juego
                                    
                                else:
                                    print("Contraseña incorrecta")
                            else:
                                print("El usuario no se encuentra registrado")

                elif event.type == KEYDOWN:
                    for field in self.input_data.values():
                        if field["active"]:
                            if event.key == K_BACKSPACE:
                                field["text"] = field["text"][:-1]
                            else:
                                field["text"] += event.unicode

            self.welcome_window.window.fill((0, 0, 255))
            self.welcome_window.draw_back_button()
            self.draw_entry_button()
            self.draw_text_inputs()
            pygame.display.flip()

        pygame.quit()
        return ""

    def draw_entry_button(self):
        entry_button = pygame.Rect(self.width - 150, self.height - 80, 100, 50)
        pygame.draw.rect(self.welcome_window.window, (0, 0, 0), entry_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Entry', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=entry_button.center)
        self.welcome_window.window.blit(text_surface, text_rect)

    def draw_text_inputs(self):
        for field_name, field_data in self.input_data.items():
            # Dibujar los campos de entrada
            pygame.draw.rect(self.welcome_window.window, (255, 255, 255), field_data["rect"])
            pygame.draw.rect(self.welcome_window.window, (0, 0, 0), field_data["rect"], 2)
            # Renderizar las etiquetas
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.welcome_window.window.blit(label_surface, field_data["pos"])
            # Renderizar el texto de entrada
            font = pygame.font.Font(None, 36)
            if field_name == "user_password":
                text_surface = font.render('*' * len(field_data["text"]), True, (0, 0, 0))
            else:
                text_surface = font.render(field_data["text"], True, (0, 0, 0))
            self.welcome_window.window.blit(text_surface, (field_data["rect"].x + 5, field_data["rect"].y + 5))

#Clase Register - heredada de la clase welcome_window
class RegisterWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.welcome_window = WelcomeWindow()
        self.welcome_window.show_back_button()

        # Define las coordenadas para las etiquetas y los rectángulos de entrada
        self.input_data = {
            "user_name": {"label": "User Name:", "pos": (150, 170), "rect": pygame.Rect(150, 200, 500, 50), "active": False, "text": ""},
            "name": {"label": "Name:", "pos": (150, 70), "rect": pygame.Rect(150, 100, 500, 50), "active": False, "text": ""},
            "user_correo": {"label": "Correo (Gmail):", "pos": (150, 270), "rect": pygame.Rect(150, 300, 500, 50), "active": False, "text": ""},
            "user_password": {"label": "Password:", "pos": (150, 370), "rect": pygame.Rect(150, 400, 500, 50), "active": False, "text": ""}
        }

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Botones para subir imágenes y canciones
        self.spaceship_image_button_rect = pygame.Rect(170, 520, 80, 50)
        self.profile_image_button_rect = pygame.Rect(270, 520, 80, 50)
        self.user_song_button_rect = pygame.Rect(370, 520, 80, 50)
        self.spaceship_image_button_active = False
        self.profile_image_button_active = False
        self.user_song_button_active = False

    
    #Bucle de la ventana de register
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for field in self.input_data.values():
                            if field["rect"].collidepoint(event.pos):
                                field["active"] = True
                            else:
                                field["active"] = False
                        # Verificar si se hizo clic en el botón "Back"
                        if 520 <= event.pos[0] <= 595 and 520 <= event.pos[1] <= 580:
                            self.welcome_window.hide_back_button()
                            pygame.display.set_caption("Welcome")
                            return "back"
                        # Verificar si se hizo clic en el botón "Submit"
                        elif self.width - 150 <= event.pos[0] <= self.width - 50 and self.height - 80 <= event.pos[1] <= self.height - 30:
                            # AQUÍ SE MANDARÍA A LA PANTALLA DE LOGIN
                            for field in self.input_data.values():
                                print(field["label"], field["text"])
                            if self.user_already_exists():
                                print("User already exists.")
                            elif not self.validate_password(self.input_data["user_password"]["text"]):
                                print("Password incomplete")
                            else:
                                # Guardar los datos en el archivo .txt
                                self.save_user_data()
                                # Crear carpetas para el usuario y guardar imágenes y canciones
                                self.create_user_folder()
                                self.save_images_and_song()
                                print("User registered successfully.")

                        # Verificar si se hizo clic en el botón "Spaceship Image"
                        elif self.spaceship_image_button_rect.collidepoint(event.pos):
                            self.select_file("spaceship_image")

                        # Verificar si se hizo clic en el botón "Profile Image"
                        elif self.profile_image_button_rect.collidepoint(event.pos):
                            self.select_file("profile_image")

                        # Verificar si se hizo clic en el botón "User Song"
                        elif self.user_song_button_rect.collidepoint(event.pos):
                            self.select_file("user_song")

                elif event.type == KEYDOWN:
                    for field in self.input_data.values():
                        if field["active"]:
                            if event.key == K_BACKSPACE:
                                field["text"] = field["text"][:-1]
                            else:
                                field["text"] += event.unicode

            self.welcome_window.window.fill((255, 0, 0))
            self.welcome_window.draw_back_button()
            self.draw_submit_button()
            self.draw_text_register_inputs()
            self.draw_upload_buttons()
            pygame.display.flip()

        pygame.quit()
        return ""
    
    #boton de submit
    def draw_submit_button(self):
        submit_button = pygame.Rect(self.width - 150, self.height - 80, 100, 50)
        pygame.draw.rect(self.welcome_window.window, (0, 0, 0), submit_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Submit!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=submit_button.center)
        self.welcome_window.window.blit(text_surface, text_rect)

    def draw_text_register_inputs(self):
        # Dibuja los campos de entrada de texto y las etiquetas
        for field in self.input_data.values():
            # Dibuja el rectángulo del campo de entrada
            pygame.draw.rect(self.welcome_window.window, (255, 255, 255), field["rect"])
            pygame.draw.rect(self.welcome_window.window, (0, 0, 0), field["rect"], 2)
            # Renderiza el texto del campo de entrada
            font = pygame.font.Font(None, 36)
            text_surface = font.render(field["text"], True, (0, 0, 0))
            self.welcome_window.window.blit(text_surface, (field["rect"].x + 5, field["rect"].y + 5))
            # Renderiza la etiqueta
            label_surface = self.font.render(field["label"], True, self.label_color)
            self.welcome_window.window.blit(label_surface, field["pos"])

    def draw_upload_buttons(self):
        # Dibuja los botones de carga de imágenes y canciones
        upload_buttons = [self.spaceship_image_button_rect, self.profile_image_button_rect, self.user_song_button_rect]
        button_colors = [(255, 255, 255)] * 3  # Color inicial de los botones
        if self.spaceship_image_button_active:
            button_colors[0] = (200, 200, 200)  # Cambia el color del botón activo
        elif self.profile_image_button_active:
            button_colors[1] = (200, 200, 200)  # Cambia el color del botón activo
        elif self.user_song_button_active:
            button_colors[2] = (200, 200, 200)  # Cambia el color del botón activo

        for button, color in zip(upload_buttons, button_colors):
            pygame.draw.rect(self.welcome_window.window, color, button)
            pygame.draw.rect(self.welcome_window.window, (0, 0, 0), button, 2)

        # Renderiza el texto de los botones
        font = pygame.font.Font(None, 20)
        button_texts = ["Spaceship", "Profile", "FavSong"]
        for i, text in enumerate(button_texts):
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=upload_buttons[i].center)
            self.welcome_window.window.blit(text_surface, text_rect)

    #Funciones para guardar datos y verificacion de usuario ya registrado
    def user_already_exists(self):
        # Verificar si el usuario ya existe
        user_name = self.input_data["user_name"]["text"]
        user_correo = self.input_data["user_correo"]["text"]

        # Verificar si ya existe un usuario con el mismo nombre de usuario o correo electrónico
        # Supongamos que tenemos una lista de usuarios existentes en un archivo de texto llamado "users.txt"
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == user_name or data[2] == user_correo:
                    return True
        return False
    
    #Verificacion de contraseña
    def validate_password(self, password):
        # Verificar longitud mínima de 7 caracteres
        if len(password) < 7:
            print("Contraseña demasiado corta, longitud mínima de 7 caracteres")
            return False
        
        # Verificar al menos una mayúscula, un símbolo especial, un número y una minúscula
        regex = re.compile(r'^(?=.*[A-Z])(?=.*[!@#$%^&*()-_])(?=.*[0-9])(?=.*[a-z]).{7,}$')
        if not regex.match(password):
            print("No cumple con los caracteres necesarios, al menos una mayúscula, un símbolo especial, un número y una minúscula ")
            return False
        
        return True
    
    #Guarda name,user_name, correo y password en .txt
    def save_user_data(self):
        # Guardar los datos del usuario en el archivo de texto "users.txt"
        user_name = self.input_data["user_name"]["text"]
        name = self.input_data["name"]["text"]
        user_correo = self.input_data["user_correo"]["text"]
        user_password = self.input_data["user_password"]["text"]

        with open("users.txt", "a") as file:
            file.write(f"{user_name},{name},{user_correo},{user_password}\n")

    #funcion para seleccionar en path las imagenes o canciones seleccionadas
    def select_file(self, file_type):
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

    #Funcion que crea las carpetas con el nombre de usuario en /User file/username
    def create_user_folder(self):
        # Obtener el nombre de usuario
        user_name = self.input_data["user_name"]["text"]
        # Crear la carpeta User files si no existe
        user_files_folder = os.path.join(os.getcwd(), "User files")
        if not os.path.exists(user_files_folder):
            os.makedirs(user_files_folder)
        # Crear la carpeta del usuario dentro de User files
        user_folder = os.path.join(user_files_folder, user_name)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

    #Funcion que almacena las imagenes y sonidos dentro de la carpeta
    def save_images_and_song(self):
        # Obtener el nombre de usuario
        user_name = self.input_data["user_name"]["text"]
        # Ruta donde se guardará la carpeta del usuario
        user_folder = os.path.join(os.getcwd(), "User files", user_name)
        # Verificar si se han seleccionado imágenes y una canción
        if self.spaceship_image_path and self.profile_image_path and self.user_song_path:
            # Copiar las imágenes y la canción a la carpeta del usuario
            shutil.copy(self.spaceship_image_path, os.path.join(user_folder, 'nave_espacial.png'))
            shutil.copy(self.profile_image_path, os.path.join(user_folder, 'perfil.png'))
            shutil.copy(self.user_song_path, os.path.join(user_folder, 'cancion.mp3'))

            print("Images and song saved successfully.")
            welcome_window = WelcomeWindow()
            pygame.display.set_caption("Welcome")
            welcome_window.run()
        else:
            print("Please select all images and the song before submitting.")


if __name__ == "__main__":
    pygame.font.init()
    welcome_window = WelcomeWindow()
    welcome_window.run()
