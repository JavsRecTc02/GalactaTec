import pygame
import sys
from pynput.keyboard import Controller
import pygame
import sys
import ctypes
from pynput.keyboard import Controller, Key
# Intenta cargar diferentes versiones de XInput
try:
    XInputSetState = ctypes.windll.xinput1_4.XInputSetState
except AttributeError:
    try:
        XInputSetState = ctypes.windll.xinput1_3.XInputSetState
    except AttributeError:
        try:
            XInputSetState = ctypes.windll.xinput1_2.XInputSetState
        except AttributeError:
            try:
                XInputSetState = ctypes.windll.xinput1_1.XInputSetState
            except AttributeError:
                XInputSetState = ctypes.windll.xinput9_1_0.XInputSetState

class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort), ("wRightMotorSpeed", ctypes.c_ushort)]

def set_vibration(left_motor, right_motor, duration):
    vibration = XINPUT_VIBRATION(int(left_motor * 65535), int(right_motor * 65535))
    XInputSetState(0, ctypes.byref(vibration))
    pygame.time.wait(duration)
    vibration = XINPUT_VIBRATION(0, 0)
    XInputSetState(0, ctypes.byref(vibration))

#Funcion para las ventanas de Error
def error_message(message):
    ctypes.windll.user32.MessageBoxW(0,message,"Error",1)

def joystick_check():
    pygame.init()
    pygame.joystick.init()

    # Verifica si hay mandos conectados
    if pygame.joystick.get_count() == 0:
        error_message("No se detecto ningun mando")
        sys.exit()

    # Conecta el primer mando (índice 0)
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Muestra información del mando
    print("Nombre del mando:", joystick.get_name())
    print("Número de ejes:", joystick.get_numaxes())
    print("Número de botones:", joystick.get_numbuttons())
    print("Número de hats:", joystick.get_numhats())

    # Inicializa el controlador de teclado
    keyboard = Controller()

    # Loop principal para verificar el mando
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Eje {event.axis} valor: {event.value}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Botón {event.button} presionado")
                if event.button == 0:  # Supongamos que el botón 0 es A
                    keyboard.press('z')  # Simula la pulsación de la tecla 'a'
                    keyboard.release('z')  # Libera la tecla 'a'
                elif event.button == 1:
                    keyboard.press('x')  # Simula la pulsación de la tecla 'a'
                    keyboard.release('x')  # Libera la tecla 'a'
                elif event.button == 3:
                    keyboard.press('a')  # Simula la pulsación de la tecla 'z'
                    keyboard.release('a')  # Libera la tecla 'a'
                elif event.button == 5:
                    keyboard.press(Key.space)
                    keyboard.release(Key.space)
                elif event.button == 6:
                    keyboard.press('1')
                    keyboard.release('1')
                elif event.button == 7:
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)



            elif event.type == pygame.JOYBUTTONUP:
                print(f"Botón {event.button} liberado")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} valor: {event.value}")
                if event.value[0] == -1:  # HAT movido a la izquierda
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                elif event.value[0] == 1:  # HAT movido a la derecha
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                elif event.value[1] == -1:  # HAT movido hacia abajo
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                elif event.value[1] == 1:  # HAT movido hacia arriba
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)

        pygame.time.wait(10)  # Pequeña espera para evitar uso excesivo de CPU

    pygame.quit()


