from pygame import *
import pygame 
from LoginAndRegister import LoginWindow
from MenuSeleccion import Menu
import ctypes

from LoginAndRegister import PasswordRecoveryWindow

from Menu2Jugadores import menu2players

##
#Se sobre escribe la clase de recuperar contraseña para editarla en el caso de 2 jugadores
##
class editBackPassword(PasswordRecoveryWindow):
    def __init__(self, width, height, player1):
        super().__init__(width, height)
        self.player1 = player1
        print(self.player1)

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
                            self.loggeoPlayer2_screen = LoginPlayer2(800,600,self.player1)
                            self.loggeoPlayer2_screen.run()
                elif event.type == pygame.KEYDOWN:
                    for field_data in self.input_data.values():
                        if field_data["active"]:
                            if event.key == pygame.K_BACKSPACE:
                                field_data["text"] = field_data["text"][:-1]
                            else:
                                field_data["text"] += event.unicode

            self.draw_interface()
            self.welcome_window.draw_back_button()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()    


##
# Se sobre escribe la clase de logueo para que acepte a un jugador más
##
class LoginPlayer2(LoginWindow):
    def __init__(self, width, height, player1):
        super().__init__(width, height)
        self.player1 = player1  
        print(self.player1)
        
        self.menu = Menu(self.player1)

        self.player2 = None
        self.input_data = {
            "user_name": {"label": "User Name:", "pos": (150, 270), "rect": pygame.Rect(215, 300, 400, 50), "active": False, "text": ""},
            "user_password": {"label": "Password:", "pos": (150, 370), "rect": pygame.Rect(215, 400, 400, 50), "active": False, "text": ""},
            "info": {"label": "Logueo Player 2", "pos": (350, 90), "rect": pygame.Rect(0, 0, 0, 0), "active": False, "text": ""}
        }
        
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
                            pygame.display.set_caption("Menu de selección")
                            self.menu.run()
                        
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
            self.welcome_window.window.fill((0, 0, 255))
            self.welcome_window.draw_back_button()
            self.draw_entry_button()
            self.draw_text_inputs()
            self.draw_forgot_password_button()
            pygame.display.flip()
        pygame.quit()
        return ""
    

    def show_error_message(self, message):
        ctypes.windll.user32.MessageBoxW(0, message, "Error", 1)

    #Funcion que verifica si los datos ingresados por el usuario coinciden en el .txt
    def handle_login(self):
        # Verificar si el usuario y la contraseña coinciden
        username = self.input_data["user_name"]["text"]
        password = self.input_data["user_password"]["text"]
        if username in self.user_data:
            if username != self.player1:
                if self.user_data[username] == password:
                    print("Loggeado")
                    self.player2 = username  # Almacenar el nombre de usuario
                    self.menu2players = menu2players(self.player1, self.player2)  # Crear una instancia de nivel1
                    self.menu2players.run()
                else:
                    self.show_error_message("Contraseña incorrecta")
            else:
                self.show_error_message("No puede logearse con el mismo usuario")
        else:
            self.show_error_message("El usuario no se encuentra registrado")
    

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
            elif field_name == "info":
                text_surface = font.render('*' * len(field_data["text"]), True, (0, 0, 0))
            else:
                text_surface = font.render(field_data["text"], True, (0, 0, 0))
            self.welcome_window.window.blit(text_surface, (field_data["rect"].x + 5, field_data["rect"].y + 5))
    
    def handle_forgot_password(self):
        #Abre la ventana de recuperacion de contraseña
        password_recovery_window = editBackPassword(self.width,self.height,self.player1)
        password_recovery_window.run()







    