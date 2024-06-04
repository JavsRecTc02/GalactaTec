import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import filedialog
import re
import os
import shutil
import ctypes
import webbrowser

from Email import UsersEmail
from RifaTurnoJugadores import rifaWindow
from MenuSeleccion import Menu

import threading
from control import joystick_check  # Importa la función joystick_check de joystick.py

#Funcion para las ventanas de Error
def error_message(self,message):
    ctypes.windll.user32.MessageBoxW(0,message,"Error",0)

#Ventana de Inicio
class WelcomeWindow:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bienvenido!")

        self.WHITE = (255, 255, 255)
        self.back_button_visible = False
        self.help_button_visible = False

        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\mainwindow.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def draw_background(self):
        self.window.blit(self.background_image, (0, 0))

    #Dibujar los botones de login, register y help
    def draw_buttons(self):
        login_button = pygame.Rect(215, 450, 180, 100)
        pygame.draw.rect(self.window, (0, 0, 0), login_button)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Ingresar', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=login_button.center) 
        self.window.blit(text_surface, text_rect)

        register_button = pygame.Rect(400, 450, 180, 100)
        pygame.draw.rect(self.window, (0, 0, 0), register_button)
        text_surface = font.render('Registrarse', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=register_button.center)
        self.window.blit(text_surface, text_rect)

        help_button = pygame.Rect(0, 550, 120, 50)
        pygame.draw.rect(self.window, (0, 0, 0), help_button)
        text_surface = font.render('Ayuda', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=help_button.center)
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

    def draw_help_button(self):
        help_button = pygame.Rect(0, 550, 120, 50)
        pygame.draw.rect(self.window, (150, 150, 150), help_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ayuda', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=help_button.center)
        self.window.blit(text_surface, text_rect)


    def show_back_button(self):
        self.back_button_visible = True

    def hide_back_button(self):
        self.back_button_visible = False
        
    def show_help_button(self):
        self.help_button_visible = True
    
    def hide_help_button(self):
        self.help_button_visible = False

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
                            pygame.display.set_caption("Ingresar")
                            login_window.run()
                        elif 400 <= x <= 575 and 450 <= y <= 550:
                            register_window = RegisterWindow(self.width, self.height)
                            pygame.display.set_caption("Registrarse")
                            register_window.run()

                        elif 0 <= x <= 120 and 550 <= y <= 600:
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')

            self.window.fill(self.WHITE)
            self.draw_background() 
            self.draw_buttons()
            pygame.display.flip()

        pygame.quit()

#*****************************************************************************************************************************************************
#Clase Login - heredada de la clase welcome_window
#*****************************************************************************************************************************************************
class LoginWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.welcome_window = WelcomeWindow()
        self.welcome_window.show_back_button()
        self.welcome_window.show_help_button()
        self.user_data = self.load_user_data()
        # Define las coordenadas y rectángulos para los campos de entrada
        self.input_data = {
            "user_name": {"label": "Usuario:", "pos": (150, 270), "rect": pygame.Rect(215, 300, 400, 50), "active": False, "text": ""},
            "user_password": {"label": "Contraseña:", "pos": (150, 370), "rect": pygame.Rect(215, 400, 400, 50), "active": False, "text": ""}
        }
        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        # Botón "Olvidaste tu contraseña?"
        self.forgot_password_button_rect = pygame.Rect(215, 450, 200, 30)
        self.forgot_password_button_active = False

        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\iniciar.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def draw_background(self):
        self.welcome_window.window.blit(self.background_image, (0, 0))

    #Funcion para los msj de error
    def error_message(self,message):
        ctypes.windll.user32.MessageBoxW(0,message,"GalactaTec",0)

    # Función que carga los strings de info de cada Javier Tenorio, para verificar 
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
        
    # Bucle de la ventana de inicio de sesión
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

                        # Verificar si se hizo clic en el botón "Olvidaste tu contraseña?"
                        if self.forgot_password_button_rect.collidepoint(event.pos):
                            self.handle_forgot_password()

                        # Verificar si se hizo clic en el botón "Back"
                        elif 520 <= event.pos[0] <= 595 and 520 <= event.pos[1] <= 580:
                            self.welcome_window.hide_back_button()
                            pygame.display.set_caption("Bienvenido!")
                            self.welcome_window.run()

                        elif 0 <= event.pos[0] <= 120 and 550 <= event.pos[1] <= 600:
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')

                        # Verificar si se hizo clic en el botón "Entry"
                        elif self.width - 150 <= event.pos[0] <= self.width - 50 and self.height - 80 <= event.pos[1] <= self.height - 30:
                            self.handle_login()

                elif event.type == KEYDOWN:
                    for field in self.input_data.values():
                        if field["active"]:
                            if event.key == K_BACKSPACE:
                                field["text"] = field["text"][:-1]
                            else:
                                field["text"] += event.unicode

            self.draw_background()
            self.welcome_window.draw_back_button()
            self.welcome_window.draw_help_button()
            self.draw_entry_button()
            self.draw_text_inputs()
            self.draw_forgot_password_button()
            pygame.display.flip()

        pygame.quit()
        return ""
    
    #Funcion que verifica si los datos ingresados por el Javier Tenorio coinciden en el .txt
    def handle_login(self):
        # Verificar si el Javier Tenorio y la contraseña coinciden
        username = self.input_data["user_name"]["text"]
        password = self.input_data["user_password"]["text"]
        if username in self.user_data:
            if self.user_data[username] == password:
                self.username = username  # Almacenar el nombre de Javier Tenorio
                self.menu = Menu(self.username, 1, 2, 3)  # Crear una instancia de nivel1
                self.menu.run()
                print("Loggeado")
                 # Aquí puedes continuar con la lógica para iniciar sesión
            else:
                self.error_message("Contraseña incorrecta")
                print("Contraseña incorrecta")
        else:
            self.error_message("El usuario no se encuentra registrado")
            print("El usuario no se encuentra registrado")

    def handle_forgot_password(self):
        #Abre la ventana de recuperacion de contraseña
        password_recovery_window = PasswordRecoveryWindow(self.width, self.height)
        password_recovery_window.run()

    def draw_entry_button(self):
        entry_button = pygame.Rect(self.width - 150, self.height - 80, 100, 50)
        pygame.draw.rect(self.welcome_window.window, (0, 0, 0), entry_button)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Ingresar', True, (255, 255, 255))
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

    def draw_forgot_password_button(self):
        pygame.draw.rect(self.welcome_window.window, (0, 0, 0), self.forgot_password_button_rect)
        font = pygame.font.Font(None, 20)
        text_surface = font.render("Olvidaste tu contraseña?", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.forgot_password_button_rect.center)
        self.welcome_window.window.blit(text_surface, text_rect)

#*****************************************************************************************************************************************************
#Clase con ventans modificables para la recuperacion de contraseña
#*****************************************************************************************************************************************************
class PasswordRecoveryWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.welcome_window = WelcomeWindow()
        self.welcome_window.show_back_button()
        self.user_email_changepsw_instance = None
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.email_to_change_password = None
        self.input_data = {
            "user_email": {"label": "Correo electrónico:", "pos": (150, 270), "rect": pygame.Rect(215, 300, 400, 50), "active": False, "text": ""}
        }
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)
        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\recuperacion.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    #Funcion para los msj de error
    def error_message(self,message):
        ctypes.windll.user32.MessageBoxW(0,message,"GalactaTec",0)

    def draw_background(self):
        self.welcome_window.window.blit(self.background_image, (0, 0))

    def is_email_registered(self, email):
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[2] == email:  # El correo electrónico es el tercer elemento
                    return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.send_email_button_rect.collidepoint(event.pos):
                        self.handle_send_email()
                    for field_name, field_data in self.input_data.items():
                        if field_data["rect"].collidepoint(event.pos):
                            field_data["active"] = True
                        else:
                            field_data["active"] = False
                    #Boton back
                    if 520 <= event.pos[0] <= 595 and 520 <= event.pos[1] <= 580:
                            self.login_screen = LoginWindow(self.width, self.height)
                            self.login_screen.run()
                    #Boton help
                    elif 0 <= event.pos[0] <= 120 and 550 <= event.pos[1] <= 600:
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
                elif event.type == pygame.KEYDOWN:
                    for field_data in self.input_data.values():
                        if field_data["active"]:
                            if event.key == pygame.K_BACKSPACE:
                                field_data["text"] = field_data["text"][:-1]
                            else:
                                field_data["text"] += event.unicode

            self.draw_interface()
            self.welcome_window.draw_back_button()
            self.welcome_window.draw_help_button()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def draw_interface(self):
        self.draw_background()
        for field_name, field_data in self.input_data.items():
            pygame.draw.rect(self.screen, (255, 255, 255), field_data["rect"])
            pygame.draw.rect(self.screen, (0, 0, 0), field_data["rect"], 2)
            label_surface = self.font.render(field_data["label"], True, self.label_color)
            self.screen.blit(label_surface, field_data["pos"])
            font = pygame.font.Font(None, 36)
            text_surface = font.render(field_data["text"], True, (0, 0, 0))
            self.screen.blit(text_surface, (field_data["rect"].x + 5, field_data["rect"].y + 5))
        
        self.draw_send_email_button()
        

    def draw_send_email_button(self):
        self.send_email_button_rect = pygame.Rect(self.width - 150, self.height - 80, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), self.send_email_button_rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Enviar correo', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.send_email_button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_send_email(self):
        email = self.input_data["user_email"]["text"]
        if self.is_email_registered(email):
            print("Correo encontrado en la base de datos. Enviando correo de recuperación...")
            self.error_message("Correo encontrado en la base de datos. Enviando correo de recuperación...")
            self.email_to_change_password = email
            print("Email :", self.email_to_change_password)
            self.change_password()
        else:
            self.error_message("Error: El correo electrónico no está registrado en la base de datos.")
            print("El correo electrónico no está registrado en la base de datos.")

    def change_password(self):
        if not self.validate_changepassword():
            self.login_screen = LoginWindow(self.width, self.height)
            self.login_screen.run()
        else:
            print("Se cambiará la contraseña.")
            pygame.display.update()  # Actualizar la ventana actual

            # Crear una instancia de PasswordRecoveryWindow si aún no existe
            if not hasattr(self, 'change_password_view'):
                self.change_password_view = PasswordRecoveryWindow(800, 600)

            # Llamar a show_change_password_interface en la instancia existente
            self.change_password_view.show_change_password_interface(self.email_to_change_password)
            self.change_password_view.run()

    def validate_changepassword(self):
        user_correo = self.input_data["user_email"]["text"]
        if self.user_email_changepsw_instance is None:
            self.user_email_changepsw_instance = UsersEmail(user_correo)
            self.user_email_changepsw_instance.generate_verification_code()

        self.user_email_changepsw_instance.verify_email()
        return self.user_email_changepsw_instance.verified_email

    def show_change_password_interface(self, user_email):
        self.email_to_change_password = user_email
        print(self.email_to_change_password)
        running = True
        password = ''
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.handle_confirm_button_click(password)
                    else:
                        password += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.confirm_button_rect.collidepoint(event.pos):
                        self.handle_confirm_button_click(password)

            self.draw_change_password_interface(password)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def draw_confirm_button(self):
        self.confirm_button_rect = pygame.Rect(350, 500, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), self.confirm_button_rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Confirmar', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.confirm_button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_change_password_interface(self, password):
        self.draw_background()
        pygame.draw.rect(self.screen, (255, 255, 255), (215, 400, 400, 50))
        pygame.draw.rect(self.screen, (0, 0, 0), (215, 400, 400, 50), 2)
        label_surface = self.font.render("Nueva contraseña:", True, self.label_color)
        self.screen.blit(label_surface, (150, 370))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(password, True, (0, 0, 0))
        self.screen.blit(text_surface, (220, 405))
        self.draw_confirm_button()

    def handle_confirm_button_click(self, password):
        # Crear una instancia de RegisterWindow
        register_window = RegisterWindow(800, 600)

        # Llamar al método validate_password de RegisterWindow
        if register_window.validate_password(password):
            print("La contraseña es válida. Se procederá con el cambio de contraseña.")
            self.update_password(self.email_to_change_password,password)
        else:
            self.error_message("Error: No cumple con los caracteres necesarios, al menos 7 caracters, una mayúscula, un símbolo especial, un número y una minúscula ")
            print("La contraseña no cumple con los requisitos necesarios, .")

    def update_password(self, email, new_password):
    # Leer el archivo "users.txt" y almacenar las líneas en una lista
        with open("users.txt", "r") as file:
            lines = file.readlines()
        # Buscar la línea correspondiente al Javier Tenorio con el correo electrónico proporcionado
        for i, line in enumerate(lines):
            parts = line.strip().split(",")
            if parts[2] == email:  # El correo electrónico es el tercer elemento
                print("Contraseña anterior:", parts[-1])
                # Actualizar la contraseña en la línea encontrada
                parts[-1] = new_password  # La contraseña es el último elemento
                print("Nueva contraseña:", new_password)
                lines[i] = ",".join(parts) + "\n"  # Unir los elementos de parts en una cadena y asignar a lines[i]
                break
        else:
            print("No se encontró ningún usuario con el correo electrónico proporcionado:", email)
            self.error_message("Error: No se encontró ningún usuario con el correo electrónico proporcionado:", email)
            #return  # Salir de la función si no se encuentra el usuario
    # Escribir las líneas actualizadas de vuelta al archivo
        with open("users.txt", "w") as file:
            file.writelines(lines)
        print("¡Cambio de contraseña exitoso!")
        login_window = LoginWindow(self.width, self.height) #Se regresa a la ventana de Login
        pygame.display.set_caption("Login")
        login_window.run()

#*****************************************************************************************************************************************************
#Clase Register 
#*****************************************************************************************************************************************************
class RegisterWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.welcome_window = WelcomeWindow()
        self.welcome_window.show_back_button()
        # Crea una instancia de UsersEmail
        self.user_email_instance = None

        # Define las coordenadas para las etiquetas y los rectángulos de entrada
        self.input_data = {
            "user_name": {"label": "Usuario:", "pos": (150, 170), "rect": pygame.Rect(150, 200, 500, 50), "active": False, "text": ""},
            "name": {"label": "Nombre:", "pos": (150, 70), "rect": pygame.Rect(150, 100, 500, 50), "active": False, "text": ""},
            "user_correo": {"label": "Correo (Gmail):", "pos": (150, 270), "rect": pygame.Rect(150, 300, 500, 50), "active": False, "text": ""},
            "user_password": {"label": "Contraseña:", "pos": (150, 370), "rect": pygame.Rect(150, 400, 500, 50), "active": False, "text": ""}
        }

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

        self.background_image = pygame.image.load(r"C:\Users\Javier Tenorio\Desktop\GalactaTec\backgrounds\registro.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        # Botones para subir imágenes y canciones
        self.spaceship_image_button_rect = pygame.Rect(170, 520, 80, 50)
        self.profile_image_button_rect = pygame.Rect(270, 520, 80, 50)
        self.user_song_button_rect = pygame.Rect(370, 520, 80, 50)
        self.spaceship_image_button_active = False
        self.profile_image_button_active = False
        self.user_song_button_active = False

    def draw_background(self):
        self.welcome_window.window.blit(self.background_image, (0, 0))

    def error_message(self,message):
            ctypes.windll.user32.MessageBoxW(0,message,"GalactaTec",0)

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
                            pygame.display.set_caption("Bienvenido!")
                            self.welcome_window.run()
                        #Verificar si hizo clic en el botón "Help"
                        elif 0 <= event.pos[0] <= 120 and 550 <= event.pos[1] <= 600:
                            #Colocar la dirección en la que se encuentra el pdf ---> file://C:\path\to\file.pdf
                            webbrowser.open_new(r'file://C:\Users\Javier Tenorio\Desktop\GalactaTec\Manual_de_ayuda_GalactaTec_prefinal.pdf')
                        # Verificar si se hizo clic en el botón "Submit"
                        elif self.width - 150 <= event.pos[0] <= self.width - 50 and self.height - 80 <= event.pos[1] <= self.height - 30:
                            for field in self.input_data.values():
                                print(field["label"], field["text"])
                            if not self.user_already_exists():
                                print("Error: El usuario ya se encuentra registrado en la base de datos")
                            elif not self.validate_password(self.input_data["user_password"]["text"]):
                                print("Password incomplete")
                            elif not self.files_selected():
                                self.error_message("Error: Por favor seleccione todos los archivos necesarios")
                                print("Please select all required files.")
                            elif not self.validate_email():
                                 self.backregis_screen = RegisterWindow(self.width, self.height)
                                 self.backregis_screen.run()
                            else:
                                # Guardar los datos en el archivo .txt
                                self.save_user_data()
                                # Crear carpetas para el usuario y guardar imágenes y canciones
                                self.create_user_folder()
                                self.save_images_and_song()
                                self.error_message("usuario registrado exitosamente en la base de datos")
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

            self.draw_background()
            self.welcome_window.draw_back_button()
            self.welcome_window.draw_help_button()
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
        text_surface = font.render('Registrarse', True, (255, 255, 255))
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
        button_texts = ["Nave", "Perfil", "Música"]
        for i, text in enumerate(button_texts):
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=upload_buttons[i].center)
            self.welcome_window.window.blit(text_surface, text_rect)

    #Funciones para guardar datos y verificacion de Javier Tenorio ya registrado
    def user_already_exists(self):
        # Verificar si el User ya existe
        user_name = self.input_data["user_name"]["text"]
        user_correo = self.input_data["user_correo"]["text"]   

        if not user_correo.endswith("@gmail.com"):
            self.error_message("Error : Correo electrónico inválido,asegurese que sea una dirección de Gmail")
            print("Invalid email address. Must be use a Gmail address")
            return False 
            
        # Verificar si ya existe un Javier Tenorio con el mismo nombre de Javier Tenorio o correo electrónico
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == user_name or data[2] == user_correo:
                    self.error_message("Error: El usuario o correo electrónico ya se encuentra registrado en la base de datos")
                    return False

        return True
    
    #Verificacion de Correo
    def validate_email(self):
        user_correo = self.input_data["user_correo"]["text"]

        # Usa la misma instancia de UsersEmail si ya está creada (Singleton)
        if self.user_email_instance is None:
            self.user_email_instance = UsersEmail(user_correo)
            self.user_email_instance.generate_verification_code()

        # Llama a verify_email en la instancia creada
        self.user_email_instance.verify_email()
        return self.user_email_instance.verified_email

    #Verificacion de contraseña
    def validate_password(self, password):
        regex = re.compile(r'^(?=.*[A-Z])(?=.*[!@#$%^&*()\-_])(?=.*[0-9])(?=.*[a-z]).{7,}$')

        # Verificar longitud mínima de 7 caracteres
        if len(password) < 7:
            self.error_message("Error: Contraseña demasiado corta, longitud mínima de 7 caracteres")
            print("Contraseña demasiado corta, longitud mínima de 7 caracteres")
            return False
        
        # Verificar al menos una mayúscula, un símbolo especial, un número y una minúscula
        elif not regex.match(password):
            self.error_message("Error: La contraseña no cumple con los caracteres necesarios, al menos una mayúscula, un símbolo especial, un número y una minúscula")
            print("No cumple con los caracteres necesarios, al menos una mayúscula, un símbolo especial, un número y una minúscula ")
            return False
        else:
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

    def files_selected(self):
    # Verificar si se han seleccionado los tres archivos requeridos
        return hasattr(self, 'spaceship_image_path') and hasattr(self, 'profile_image_path') and hasattr(self, 'user_song_path')

    #Funcion que crea las carpetas con el nombre de Javier Tenorio en /User file/username
    def create_user_folder(self):
        # Obtener el nombre de Javier Tenorio
        user_name = self.input_data["user_name"]["text"]
        # Crear la carpeta User files si no existe
        user_files_folder = os.path.join(os.getcwd(), "User files")
        if not os.path.exists(user_files_folder):
            os.makedirs(user_files_folder)
        # Crear la carpeta del Javier Tenorio dentro de User files
        user_folder = os.path.join(user_files_folder, user_name)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

    #Funcion que almacena las imagenes y sonidos dentro de la carpeta
    def save_images_and_song(self):
        # Obtener el nombre de Javier Tenorio
        user_name = self.input_data["user_name"]["text"]
        # Ruta donde se guardará la carpeta del Javier Tenorio
        user_folder = os.path.join(os.getcwd(), "User files", user_name)
        # Verificar si se han seleccionado imágenes y una canción
        if self.spaceship_image_path and self.profile_image_path and self.user_song_path:
            # Copiar las imágenes y la canción a la carpeta del Javier Tenorio
            shutil.copy(self.spaceship_image_path, os.path.join(user_folder, 'nave_espacial.png'))
            shutil.copy(self.profile_image_path, os.path.join(user_folder, 'perfil.png'))
            shutil.copy(self.user_song_path, os.path.join(user_folder, 'cancion.mp3'))

            print("Images and song saved successfully.")
            welcome_window = WelcomeWindow()
            pygame.display.set_caption("Welcome")
            welcome_window.run()
        else:
            self.error_message("Error: Porfavor ingrese todos los datos necesarios, incluidos los archivos correspondientes")
            print("Please select all images and the song before submitting.")


if __name__ == "__main__": 
    pygame.font.init()
    welcome_window = WelcomeWindow()
    
    # Crea un hilo para la función joystick_check
    joystick_thread = threading.Thread(target=joystick_check)
    
    # Inicia el hilo
    joystick_thread.start()
    
    # Ejecuta el juego principal
    welcome_window.run()
    
    # Espera a que termine el hilo del joystick antes de terminar el programa
    joystick_thread.join()