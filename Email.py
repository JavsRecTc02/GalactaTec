import pygame
import random
import yagmail
import threading
import time
import ctypes

class UsersEmail:
    def __init__(self, user_correo):
        self.user_email = user_correo
        self.code_verify = None
        self.verified_email = False
        self.code_sent_time = None
        self.expiration_time = 300  # 5 minutos en segundos

    def email_message(self,message):
            ctypes.windll.user32.MessageBoxW(0,message,"GalactaTec",1)

    def generate_verification_code(self):
        # Generar un número aleatorio de 5 cifras
        self.code_verify = str(random.randint(10000, 99999))
        self.code_sent_time = time.time()  # Tiempo actual en segundos

    def validate_code(self, verification_window):
        user_input = verification_window.entry_text
        if user_input == self.code_verify:
            self.email_message("Error : Codigo de verificacion exitoso.")
            print("El código es correcto.")
            self.verified_email = True
            verification_window.close()
        else:
            self.email_message("Error: El código ingresado es incorrecto. Intente de nuevo.")
            print("El código ingresado es incorrecto. Intente de nuevo.")

    def verify_email(self):
        email = 'teamaltf4galactatec@gmail.com'
        password_gmail = 'vatn mhkd enws ldrw'
        user_email = self.user_email
        yag = yagmail.SMTP(user=email, password=password_gmail)

        destiny = [user_email]
        # Datos que contiene el Email, con HTML se pueden agregar hasta imágenes 
        asunto = 'Hello GalactaTEC user'
        mesagge = 'Utilice este código para verificar su correo electrónico o restablecer su contraseña'  # Usar el código generado
        html = f'<h1>Código de verificación</h1><p>{self.code_verify}</p>'

        print("Codigo de verificacion enviado al Email: ", user_email + ", tiempo de expiracion 5 minutos.")
        self.email_message("Codigo de verificacion enviado exitosamente, tiempo de expiracion 5 minutos.")

        yag.send(destiny, asunto, [mesagge,html])

        verification_window = VerificationWindow(self.code_verify, self)

        # Iniciar el hilo para manejar la expiración del código
        expiration_thread = threading.Thread(target=self.check_code_expiration, args=(verification_window,))
        expiration_thread.start()

        verification_window.run()

    def check_code_expiration(self, verification_window):
        start_time = time.time()
        while time.time() < start_time + self.expiration_time:
            remaining_time = int(start_time + self.expiration_time - time.time())
            verification_window.update_timer(remaining_time)
            print(f"Tiempo restante: {remaining_time} segundos", end='\r')
            time.sleep(1)
        print("\nEl código de verificación ha expirado. Por favor, inténtelo de nuevo.")
        self.email_message("Error: El código de verificación ha expirado. Por favor, inténtelo de nuevo.")
        self.verified_email = False
        verification_window.close()

class VerificationWindow:
    def __init__(self, verification_code, user_instance):
        self.verification_code = verification_code
        self.user_instance = user_instance
        self.screen_width = 600
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)
        self.entry_font = pygame.font.SysFont("arial", 20)
        self.entry_text = ""
        self.remaining_time = user_instance.expiration_time
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

            self.screen.fill((245, 245, 245))  # Fondo gris claro
            self.draw_timer()
            self.draw_text()
            pygame.display.flip()
            self.clock.tick(60)

    def update_timer(self, remaining_time):
        self.remaining_time = remaining_time

    def draw_timer(self):
        timer_text = f"Tiempo restante: {self.remaining_time // 60} min {self.remaining_time % 60} seg"
        timer_surface = self.font.render(timer_text, True, (50, 50, 50))
        timer_rect = timer_surface.get_rect(topright=(self.screen_width - 10, 10))
        self.screen.blit(timer_surface, timer_rect)

    def draw_text(self):
        text_surface = self.font.render("Ingrese el código de verificación:", True, (50, 50, 50))  # Texto gris oscuro
        text_rect = text_surface.get_rect(midtop=(self.screen_width/2, 100))
        self.screen.blit(text_surface, text_rect)
        
        entry_rect = pygame.Rect(self.screen_width/4, 150, self.screen_width/2, 40)
        pygame.draw.rect(self.screen, (255, 255, 255), entry_rect)  # Fondo blanco de la entrada de texto
        entry_surface = self.entry_font.render(self.entry_text, True, (50, 50, 50))  # Texto gris oscuro
        entry_surface_rect = entry_surface.get_rect(center=entry_rect.center)
        self.screen.blit(entry_surface, entry_surface_rect)

        enter_msg_surface = self.font.render("Presione Enter para enviar", True, (50, 50, 50))  # Texto gris oscuro
        enter_msg_rect = enter_msg_surface.get_rect(midtop=(self.screen_width/2, 250))
        self.screen.blit(enter_msg_surface, enter_msg_rect)

    def close(self):
        self.running = False
