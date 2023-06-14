# import pygame as py
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import seaborn as sns
import formula_caidalibre as formula

# ?                          Setup principal de la main_window
ventana_principal = ctk.CTk()  # Asignamos las propiedades de ctk.Ctk a main_window
ventana_principal.title("Proyecto")  # Ponemos nombre a la ventanita creada
ventana_principal.geometry("1000x600")  # Definimos la resolucion de la ventana
ventana_principal.resizable(False, False)  # Denegamos el ajuste de ventana en el eje x e y
sns.set(style="darkgrid")  # Configuración de estilo con Seaborn
# ?                           #####################################


grafico_frame = ctk.CTkFrame(ventana_principal, width=740, height=560)  # Frame para el gráfico  "graphic_frame"
grafico_frame.grid(row=0, column=1, pady=20)  # Posicionamiento del frame para gráficos

botones_frame = ctk.CTkFrame(ventana_principal, width=200, height=560)  # Frame para Botones/textboxes   "buttons_frame"
botones_frame.grid(row=0, column=0, padx=20, pady=10)  # Posicionamiento del frame para los botones/texboxes
# Frame de dimensiones 200x560
plot_botones = ctk.CTkFrame(ventana_principal, width=740, height=200)
plot_botones.grid(row=1, column=1, padx=20, pady=10)

lienzo = None


# Resto del código...
# TODO: Proximamente implementar
# * Función para ver opción seleccionada

def toolbar(action):
    global toolbar
    action(toolbar)
    toolbar.update()
    toolbar.pack()
    toolbar.pack_forget()

def plot_reset_pos():
    print(f"plot_home")

def plot_movimiento():
    print("plot_movement")

def plot_zoom():
    print("plot_zoom")

def plot_guardar():
    print("plot_save")



def obtener_valores():
   global txt_1
   altura = txt_1.get()
   print(altura)
   return float(altura)
    

def graficar(param1):
    # Crear un lienzo de Matplotlib para Tkinter
    fig = formula.caida_libre(param1)
    lienzo = FigureCanvasTkAgg(fig, master=grafico_frame)
    lienzo.draw()
    lienzo.get_tk_widget().pack()

    # Crear una barra de navegación para el lienzo
    toolbar = NavigationToolbar2Tk(lienzo)
    toolbar.update()
    toolbar.pack()
    toolbar.pack_forget()
    return fig, lienzo.draw(), lienzo.get_tk_widget().pack()




def funcion_principal():
    temp = obtener_valores()
    try:
        graficar(temp)
        return graficar
    except:
        print("Valor invalido")

# Crear botones personalizados para matplotlib
btn_home = ctk.CTkButton(plot_botones,width=10, height=10, text="Reset Pos.", command=plot_movimiento)
btn_home.grid(column=0, row=0, padx=5)

btn_zoom = ctk.CTkButton(plot_botones,width=10, height=10, text="Zoom", command=plot_zoom)
btn_zoom.grid(column=1, row=0, padx=5)

btn_movement = ctk.CTkButton(plot_botones,width=10, height=10, text="Moverse", command=plot_movimiento)
btn_movement.grid(column=2, row=0, padx=5)

btn_guardar = ctk.CTkButton(plot_botones,width=10, height=10, text="Guardar", command=plot_guardar)
btn_guardar.grid(column=3, row=0, padx=5)


txt_1_label = ctk.CTkLabel(botones_frame, width=5, height=10, text="Altura:",font=ctk.CTkFont(size=12, weight="bold"))          # Crear texto dentro de buttons_frame
txt_1_label.grid(row=0, column=0, columnspan=2, pady=15,sticky="sew")                                            # Posicionamiento del texto dentro de botones_frame
txt_1 = ctk.CTkEntry(botones_frame, width=60, height=8, corner_radius=0)  # Textbox para almacenar valores
txt_1.grid(row=1, column=0, padx=2, pady=5, sticky="ne")                  # Posicion de la textbox

btn_5 = ctk.CTkButton(botones_frame, width=60, height=10,command=print(txt_1.get()))  # Segmented button, para 2 botones en 1
btn_5.grid(row=1, column=1, padx=2, pady=8, sticky="nw")                
btn_5 = ctk.CTkButton(botones_frame, width=5, height=15, text="Calcular", font=ctk.CTkFont(size=12, weight="bold"),command=funcion_principal)
btn_5.grid(column=0, columnspan=2, rowspan=2, row=12, padx=16, sticky='ew')






# !   Loop principal de la Ventana    #
ventana_principal.mainloop()                                                                        
