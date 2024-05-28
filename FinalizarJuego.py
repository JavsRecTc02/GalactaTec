import pygame
import sys
import os
import ctypes
from Scores import ScoreWindow

class FinalizarJuego:
    def __init__(self, player1, player2, score1, score2):
        pygame.init()
        self.player1 = player1
        self.puntaje1 = score1
        self.player2 = player2
        self.puntaje2 = score2

        self.pantalla = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Partida Finalizada')
        
        self.profile_image1 = self.get_profile_image(self.player1)
        self.profile_image2 = self.get_profile_image(self.player2) if self.player2 else None

        self.fuente = pygame.font.Font(None, 54)
        self.fuente_botones = pygame.font.Font(None, 50)

        # Definir los colores
        self.color_texto = (255, 255, 255)
        self.color_fondo = (0, 0, 0)
        self.color_boton = (0, 100, 255)
        self.color_boton_hover = (0, 150, 255)
        self.color_rojo = (255, 0, 0)

        # Definir los botones
        self.boton_menu = pygame.Rect(150, 500, 150, 50)
        self.boton_salir = pygame.Rect(325, 500, 150, 50)
        self.boton_scores = pygame.Rect(500, 500, 150, 50)

        # Verificar si es un nuevo mejor puntaje
        self.nuevo_mejor_puntaje1 = self.verificar_nuevo_mejor_puntaje(self.puntaje1)
        self.nuevo_mejor_puntaje2 = self.verificar_nuevo_mejor_puntaje(self.puntaje2) if self.player2 and self.puntaje2 else False

        # Guardar los puntajes en el archivo scores.txt
        self.guardar_puntaje(self.player1, self.puntaje1)
        if self.player2 and self.puntaje2:
            self.guardar_puntaje(self.player2, self.puntaje2)

    def user_message(self, message):
        ctypes.windll.user32.MessageBoxW(0, message, "Nuevo Record", 1)

    def verificar_nuevo_mejor_puntaje(self, score):
        if score is None:
            return False
        try:
            with open(r"C:\Users\Usuario\Desktop\GalactaTec\scores.txt", 'r') as file:
                scores = [line.strip().split(',') for line in file]
                scores = [(name, int(score)) for name, score in scores]
        except FileNotFoundError:
            scores = []

        top_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
        return score > top_scores[-1][1] if len(top_scores) > 0 else True

    def guardar_puntaje(self, user, score):
        if user and score is not None:
            with open(r"C:\Users\Usuario\Desktop\GalactaTec\scores.txt", 'a') as file:
                file.write(f"{user},{score}\n")

        if user == self.player1 and self.nuevo_mejor_puntaje1:
            self.mostrar_mensaje_nuevo_record(self.player1)
        elif user == self.player2 and self.nuevo_mejor_puntaje2:
            self.mostrar_mensaje_nuevo_record(self.player2)

    def mostrar_mensaje_nuevo_record(self, player):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 5000:  # 5 segundos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.time.get_ticks() % 1000 < 500:  # Parpadeo cada medio segundo
                self.dibujar_pantalla(show_message=True, player=player)
            else:
                self.dibujar_pantalla(show_message=False, player=player)

        self.user_message(f"Felicidades, {player} has establecido un nuevo record en el salón de la fama!")
        self.mostrar_ventana_records(player)

    def mostrar_ventana_records(self, player):
        scores_window = ScoreWindow(player, self.puntaje1 if player == self.player1 else self.puntaje2)
        scores_window.previous_instance = self
        scores_window.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_menu.collidepoint(event.pos):
                        print("MENU")
                        # Implementa la funcionalidad para ir al menú
                    elif self.boton_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif self.boton_scores.collidepoint(event.pos):
                        scores_window = ScoreWindow(self.player1, self.puntaje1)
                        scores_window.previous_instance = self
                        scores_window.run()

            self.dibujar_pantalla(self.nuevo_mejor_puntaje1 or self.nuevo_mejor_puntaje2)

    def dibujar_pantalla(self, show_message, player=None):
        self.pantalla.fill(self.color_fondo)

        # Mostrar texto de Game Over
        texto_game_over = self.fuente.render('Game Over', True, (255, 0, 0))
        self.pantalla.blit(texto_game_over, (250, 50))

        # Ordenar jugadores por puntaje
        jugadores = [(self.player1, self.puntaje1, self.profile_image1)]
        if self.player2 and self.puntaje2:
            jugadores.append((self.player2, self.puntaje2, self.profile_image2))
        jugadores.sort(key=lambda x: x[1], reverse=True)

        # Centrar nombres, puntajes e imágenes de perfil en la pantalla
        y_offset = 120
        for player_name, score, profile_image in jugadores:
            if profile_image:
                self.pantalla.blit(profile_image, (150, y_offset))
            
            texto_user = self.fuente.render(f'user: {player_name}', True, self.color_texto)
            texto_puntaje = self.fuente.render(f'puntaje: {score}', True, self.color_texto)
            self.pantalla.blit(texto_user, (250, y_offset))
            self.pantalla.blit(texto_puntaje, (250, y_offset + 100))
            y_offset += 200

        # Mostrar mensaje de nuevo record si es necesario
        if show_message and player:
            mensaje_nuevo_record = self.fuente_botones.render(f'Nuevo Record! {player}', True, self.color_rojo)
            self.pantalla.blit(mensaje_nuevo_record, (500, 50))

        # Dibujar botones
        self.dibujar_boton(self.boton_menu, 'MENU')
        self.dibujar_boton(self.boton_salir, 'SALIR')
        self.dibujar_boton(self.boton_scores, 'SCORES')

        pygame.display.flip()

    def dibujar_boton(self, rect, texto):
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):
            color = self.color_boton_hover
        else:
            color = self.color_boton

        pygame.draw.rect(self.pantalla, color, rect)
        texto_boton = self.fuente_botones.render(texto, True, self.color_texto)
        self.pantalla.blit(texto_boton, (rect.x + (rect.width - texto_boton.get_width()) // 2, rect.y + (rect.height - texto_boton.get_height()) // 2))

    def get_profile_image(self, player):
        if not player:
            return None
        ruta_directorio_carpetas = r"C:\Users\Javier Tenorio\Desktop\GalactaTec\User files"
        carpetas = [nombre for nombre in os.listdir(ruta_directorio_carpetas) if os.path.isdir(os.path.join(ruta_directorio_carpetas, nombre))]
        carpetas.sort()
        if player in carpetas:
            ruta_carpeta_user = os.path.join(ruta_directorio_carpetas, player)
            archivos = os.listdir(ruta_carpeta_user)
            archivos_perfil = [archivo for archivo in archivos if archivo.startswith('perfil')]
            for archivo in archivos_perfil:
                imagen_perfil = pygame.image.load(os.path.join(ruta_carpeta_user, archivo))
                return pygame.transform.scale(imagen_perfil, (80, 80))
        return None

    
#Para probar la ventana y si funciona lo de records
#if __name__ == "__main__":
 #   pygame.font.init()
 #   puntaje1 = 1000
 #   puntaje2 = 14000
 #   nombre1 = "blasfEma"
 #   nombre2 = "TheEmanuel"

    #test_window = FinalizarJuego(nombre1, nombre2, puntaje1, puntaje2)
    #test_window.run()