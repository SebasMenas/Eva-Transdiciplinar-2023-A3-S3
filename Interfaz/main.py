import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import seaborn as sns
import numpy as np

#?                          Setup principal de la main_window
main_window = ctk.CTk()                                                                                  #   Asignamos las propiedades de ctk.Ctk a main_window
main_window.title("Proyecto")                                                                            #   Ponemos nombre a la ventanita creada
main_window.geometry("1000x600")                                                                         #   Definimos la resolucion de la ventana
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1] #   Obtenemos el alto y ancho
main_window.resizable(False, False)                                                                      #   Denegamos el ajuste de ventana en el eje x e y
#?                           #####################################

#* Función para ver opción seleccionada
def selected(choice):
    print(choice)

#* Función para generar gráfico
def generate_plot():
    g = 9.8                         # Aceleración debido a la gravedad en m/s^2
    t = np.linspace(0, 2, 100)      # Tiempo en segundos
    h = 0.5 * g * t**2              # Altura en metros (fórmula de la caída libre)

    sns.set(style="darkgrid")       # Configuración de estilo con Seaborn
    
    # Creación del gráfico
    fig, ax = plt.subplots()
    ax.plot(t, h, label="Altura")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Altura (m)")
    ax.set_title("Caída libre de un objeto")
    ax.legend()

    return fig

#* Función para menu de matplotlib
def plot_home():
    toolbar.home()

def plot_movement():
    toolbar.pan()

def plot_zoom():
    toolbar.zoom()

def plot_save():
    toolbar.save_figure()

##################################################################3



graphic_frame = ctk.CTkFrame(main_window, width=740, height=560)    #Frame para el gráfico  "graphic_frame"
graphic_frame.grid(row=0, column=1, pady=20)                        #Posicionamiento del frame para gráficos

buttons_frame = ctk.CTkFrame(main_window, width=200, height=560)    #Frame para Botones/textboxes   "buttons_frame"
buttons_frame.grid(row=0, column=0, padx=20, pady=10)               #Posicionamiento del frame para los botones/texboxes

plot_buttons = ctk.CTkFrame(main_window, width=740, height=200)
plot_buttons.grid(row=1, column=1, padx=20, pady=10)

#*                                                                                                                                   #Todos estos botones están dentro de buttons_frame
#Ocupan filas 0;1                                                                                                                    #Lo mismo para cada botón con estas mismas caracteristicas
txt_1_label = ctk.CTkLabel(buttons_frame, width=5, height=10, text="Posición Inicial:", font=ctk.CTkFont(size=12, weight="bold"))    #Crear texto dentro de buttons_frame
txt_1_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="sew")                                                               #Posicionamiento del texto dentro de buttons_frame
txt_1 = ctk.CTkTextbox(buttons_frame, width=60, height=8, activate_scrollbars=False)                                                 #Textbox para almacenar valores
txt_1.grid(row=1, column=0, padx=2, pady=5, sticky="ne")                                                                             #Posicion de la textbox

b_1 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=[" Km ", "  m  "], command=selected)                         #Segmented button, para 2 botones en 1
b_1.grid(row=1, column=1, padx=2, pady=8, sticky="nw")                                                                               #Posicion y config del segmented button
b_1.set("  m  ")

#Ocupan filas 3;4
txt_2_label = ctk.CTkLabel(buttons_frame, width=5, height=10, text="Velocidad inicial:", font=ctk.CTkFont(size=12, weight="bold"))
txt_2_label.grid(row=3, column=0, columnspan=2, pady=15, sticky="sew")
txt_2 = ctk.CTkTextbox(buttons_frame, width=60, height=8, activate_scrollbars=False)
txt_2.grid(row=4, column=0, padx=2, pady=5, sticky="ne")
b_2 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=["Km/h", " m/s "], command=selected)
b_2.grid(row=4, column=1, padx=2, pady=8, sticky="nw")
b_2.set(" m/s") 

#Ocupan filas 6;7   
txt_3_label = ctk.CTkLabel(buttons_frame, width=5, height=10, text="Aceleración: ", font=ctk.CTkFont(size=12, weight="bold"))
txt_3_label.grid(row=6, column=0, columnspan=2, pady=15, sticky="sew")
txt_3 = ctk.CTkTextbox(buttons_frame, width=60, height=8, activate_scrollbars=False)                              
txt_3.grid(row=7, column=0, padx=2, pady=5, sticky="ne")
b_3 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=["Km/h", " m/s "], command=selected)
b_3.grid(row=7, column=1, padx=2, pady=8, sticky="nw")                                                             
b_3.set("Km/h") 

#Ocupan filas 9;10
txt_4_label = ctk.CTkLabel(buttons_frame, width=5, height=15, text="Algún otra función:", font=ctk.CTkFont(size=12, weight="bold"))
txt_4_label.grid(row=9, column=0, columnspan=2, pady=15, sticky="sew")
txt_4 = ctk.CTkTextbox(buttons_frame, width=60, height=8, activate_scrollbars=False)
txt_4.grid(row=10, column=0, padx=2, pady=5, sticky="e")
b_4 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=[" h "," m "," s "], command=selected)
b_4.grid(row=10, column=1, padx=2, pady=8, sticky="w")
b_4.set(" m ")

####################################################################3

# Generar el gráfico utilizando la función generate_plot()
fig = generate_plot()

# Crear un lienzo de Matplotlib para Tkinter
lienzo = FigureCanvasTkAgg(fig, master=graphic_frame)
lienzo.draw()
lienzo.get_tk_widget().pack()

# Crear una barra de navegación para el lienzo
toolbar = NavigationToolbar2Tk(lienzo, graphic_frame)
toolbar.update()
toolbar.pack()

# Ocultar el menú de Matplotlib en la barra de herramientas
toolbar.pack_forget()

# Crear botones personalizados para matplotlib
btn_home = ctk.CTkButton(plot_buttons, text="Reset Pos.", command=plot_home)
btn_home.grid(column=0, row = 0, padx=5)

btn_zoom = ctk.CTkButton(plot_buttons, text="Zoom", command=plot_zoom)
btn_zoom.grid(column=1, row = 0, padx=5)

btn_movement = ctk.CTkButton(plot_buttons, text="Moverse", command=plot_movement)
btn_movement.grid(column=2,row=0, padx=5)

btn_save = ctk.CTkButton(plot_buttons, text="Guardar", command=plot_save)
btn_save.grid(column=3,row=0, padx=5)



#   Loop principal de la Ventana    #
main_window.mainloop()
