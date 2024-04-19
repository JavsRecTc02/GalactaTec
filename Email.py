import pygame
import random
import yagmail

class UsersEmail:
    def __init__(self, user_correo):
        self.user_email = user_correo
        self.code_verify = None
        self.verified_email = False

    def generate_verification_code(self):
        # Generar un número aleatorio de 5 cifras
        self.code_verify = str(random.randint(10000, 99999))

    def validate_code(self, verification_window):
        user_input = verification_window.entry_text
        if user_input == self.code_verify:
            print("El código es correcto.")
            self.verified_email = True
            verification_window.close()
        else:
            print("El código ingresado es incorrecto. Intente de nuevo.")

    def verify_email(self):
        email = 'teamaltf4galactatec@gmail.com'
        password_gmail = 'vatn mhkd enws ldrw'
        user_email = self.user_email
        yag = yagmail.SMTP(user=email, password=password_gmail)

        destiny = [user_email]
        # Datos que contiene el Email, con HTML se pueden agregar hasta imágenes 
        asunto = 'Welcome. New User Galacta TEC'
        messagge = f'Código de verificación: {self.code_verify}'  # Usar el código generado
        html = '<h1>Codigo de verificacion</h1.'

        print("Codigo de verificacion enviado :))")

        yag.send(destiny, asunto, messagge)

        verification_window = VerificationWindow(self.code_verify, self)
        verification_window.run()

class VerificationWindow:
    def __init__(self, verification_code, user_instance):
        self.verification_code = verification_code
        self.user_instance = user_instance
        self.screen = pygame.display.set_mode((400, 200))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.entry_text = ""
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.user_instance.validate_code(self)
                    elif event.key == pygame.K_BACKSPACE:
                        self.entry_text = self.entry_text[:-1]
                    else:
                        self.entry_text += event.unicode

            self.screen.fill((0, 0, 255))  # Fondo azul
            self.draw_text()
            pygame.display.flip()
            self.clock.tick(60)

    def draw_text(self):
        text_surface = self.font.render("Ingrese el código de verificación:", True, (255, 255, 255))  # Texto blanco
        self.screen.blit(text_surface, (20, 20))
        entry_surface = self.font.render(self.entry_text, True, (255, 255, 255))  # Texto blanco
        self.screen.blit(entry_surface, (20, 80))
        enter_msg_surface = self.font.render("Presione Enter para enviar", True, (255, 255, 255))  # Texto blanco
        self.screen.blit(enter_msg_surface, (20, 150))

    def close(self):
        self.running = False
