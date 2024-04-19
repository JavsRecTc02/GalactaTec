import tkinter as tk
from tkinter import messagebox

#Creación de una clase para abrir las ventanas de cada botón 
class MainwindowFunctions:

    def __init__(self):
        pass

    def display_help():
        #poner dercción del pdf cuando esté
        messagebox.showinfo("Placeholder", "Hello, world!") #placeholder

    def StartGame1P():
        messagebox.showinfo("Placeholder", "Hello, world!") #placeholder
    
    def StartGame2P():
        messagebox.showinfo("Placeholder", "Hello, world!") #placeholder

    def ShowGameConfig():
        messagebox.showinfo("Placeholder", "Hello, world!") #placeholder

    def ShowUserConfig():
        messagebox.showinfo("Placeholder", "Hello, world!") #placeholder

    def ShowFameRoom():
        messagebox.showinfo("Placeholder", "Hello, world!") #placeholder
        
    
# Creación de la ventana principal
root = tk.Tk()
root.title("Menú")
root.geometry('1280x720')
root.resizable(False, False)


#Creación de los botones
        
#Botón para cerrar el juego
close_button = tk.Button(root, text="Cerrar juego", command=root.destroy)
close_button.pack(side="bottom", padx=20, pady= 20)

#Botón para mostrar la ayuda
help_button = tk.Button(root, text="Ayuda", command=MainwindowFunctions.display_help)
help_button.pack(side="bottom", padx=40, pady=40)

#Botón para entrar a la configuración de usuario
config_user_button = tk.Button(root, text="Editar configuración de usuario", command=MainwindowFunctions.ShowUserConfig)
config_user_button.pack(side="bottom", padx=40, pady= 40)

#Botón para entrar a la configuración de la partida
config_game_button = tk.Button(root, text="Editar configuración de la partida", command=MainwindowFunctions.ShowGameConfig)
config_game_button.pack(side="bottom", padx=40, pady= 40)

#Botón para entrar al salón de la fama y ver récords
FameRoom_button = tk.Button(root, text="Salón de la fama", command=MainwindowFunctions.ShowFameRoom)
FameRoom_button.pack(side="bottom", padx=40, pady= 40)

#Botón para iniciar una partida multijugador
two_player_button = tk.Button(root, text="Empezar partida para dos jugadores", command=MainwindowFunctions.StartGame2P)
two_player_button.pack(side="bottom", padx=40, pady= 40)

#Botón para iniciar una partida de un solo jugador
singleplayer_button = tk.Button(root, text="Empezar partida para un jugador", command=MainwindowFunctions.StartGame1P)
singleplayer_button.pack(side="bottom", padx=40, pady= 40)




# Iniciar la ventana
root.mainloop()
