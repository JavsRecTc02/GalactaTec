import pygame
from pygame.locals import *

class WelcomeWindow:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Welcome")

        self.WHITE = (255, 255, 255)
        self.back_button_visible = False

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
        # Define las coordenadas y rectángulos para los campos de entrada
        self.input_data = {
            "user_name": {"label": "User Name:", "pos": (150, 270), "rect": pygame.Rect(215, 300, 175, 50), "active": False, "text": ""},
            "user_password": {"label": "Password:", "pos": (150, 370), "rect": pygame.Rect(215, 400, 175, 50), "active": False, "text": ""}
        }
        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

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
                            #ACA SE MANDARIA A UNA FUNCION QUE COMPRUEBE LOS DATOS Y DESPUES ESA MISMA FUNCION MANDA A LA VENTANA DE JUEGO.
                            print("User Name:", self.input_data["user_name"]["text"])
                            print("User Password:", self.input_data["user_password"]["text"])
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
            "user_name": {"label": "User Name:", "pos": (150, 170), "rect": pygame.Rect(215, 200, 175, 50), "active": False, "text": ""},
            "name": {"label": "Name:", "pos": (150, 70), "rect": pygame.Rect(215, 100, 175, 50), "active": False, "text": ""},
            "user_correo": {"label": "Correo (Gmail):", "pos": (150, 270), "rect": pygame.Rect(215, 300, 175, 50), "active": False, "text": ""},
            "user_password": {"label": "Password:", "pos": (150, 370), "rect": pygame.Rect(215, 400, 175, 50), "active": False, "text": ""}
        }

        # Define la fuente y tamaño de las etiquetas
        self.font = pygame.font.Font(None, 25)
        self.label_color = (255, 255, 255)

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
                            # AQUÍ SE MANDARIA A LA PANTALLA DE LOGIN
                            for field in self.input_data.values():
                                print(field["label"], field["text"])

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
            pygame.display.flip()

        pygame.quit()
        return ""

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

if __name__ == "__main__":
    pygame.font.init()
    welcome_window = WelcomeWindow()
    welcome_window.run()
