from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import pyplot as plt
import formula_caidalibre as formula
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
import seaborn as sns

# Setup principal de la ventana
ventana_principal = ctk.CTk()
ventana_principal.title("Proyecto")
ventana_principal.geometry("1200x600")
ventana_principal.resizable(False, False)
sns.set(style="darkgrid")
ctk.set_appearance_mode("light")

#!##########    Ajuste de tema modo claro
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#ebebeb",foreground="#000", fieldbackground="#cfcfcf", borderwidth=0)
style.configure("Treeview.Heading", background="#1f6aa5", foreground="#FFF", relief=tk.FLAT)
style.map("Treeview.Heading", background=[('active', '#144870'), ('hover', '#144870')])
#!##########    Ajuste de tema modo claro


graph_plot_frame =  ctk.CTkFrame(ventana_principal, width=740, height=520)
graph_plot_frame.grid(row=0, column=1, pady=20, sticky="ew")

grafico_frame = ctk.CTkFrame(graph_plot_frame, width=640, height=480)
grafico_frame.grid(row=0, column=1, pady=20, padx=20, sticky="sew")

botones_frame = ctk.CTkFrame(ventana_principal, width=200, height=560)
botones_frame.grid(row=0, column=0, padx=20, pady=10)

frame_plot_botones = ctk.CTkFrame(graph_plot_frame, width=740, height=200)
frame_plot_botones.grid(row=1, column=1, padx=20, pady=10)

tabla_frame = ctk.CTkFrame(ventana_principal, width=250, height=600)
tabla_frame.grid(row=0, column=2, padx=15, pady=20, sticky="ns")


lienzo = None
toolbar = None
eliminar = False
u_longitud = ""

def get_g():
    values_g = ['Tierra', 'Luna', 'Saturno', 'Neptuno', 'Júpiter']
    values_n = [9.8, 1.62, 10.44, 11.15, 24.79]

    g = g_combo.get()
    
    for i in range(6):
        if values_g[i-1] == g:
            return values_n[i-1]

def sbutton_get(value):
    global u_longitud
    u_longitud = value
    return u_longitud

def obtener_valores():
    global u_longitud
    global txt_1
    global txt_1_km_or_m
    u_longitud = txt_1_km_or_m.get()
    altura = txt_1.get("0.0", "end")
    altura = float(altura)
    if u_longitud == "m":
        return altura
    else:
        altura = altura*1000
        return altura 
    
def eliminar_grafico():
    global lienzo
    if lienzo:
        lienzo.get_tk_widget().pack_forget()
        lienzo = None
        return lienzo

def graficar(param1):
    global lienzo
    global toolbar
    g = get_g()
    eliminar_grafico()
    fig = formula.caida_libre(param1, g, u_longitud)
    lienzo = FigureCanvasTkAgg(fig, master=grafico_frame)
    toolbar = NavigationToolbar2Tk(lienzo)
    toolbar.update()
    toolbar.pack_forget()  # Oculta la toolbar sin eliminarla
    plt.close(fig)
    return fig, lienzo.draw(), lienzo.get_tk_widget().pack_configure(),

def eliminar_tabla():
    global eliminar
    for item in tabla_valores.get_children():
        tabla_valores.delete(item)
    eliminar = False

def tabla_datos(altura):
    global eliminar
    datos  = formula.datos_tabla(altura, get_g())
    alturas = datos[0]
    tiempos = datos[1]
    velocidades = datos[2]
    if eliminar:
        eliminar_tabla()
    for i in range(0,25):
        tabla_valores.insert("", "end", values=(alturas[i], tiempos[i], velocidades[i]))

    eliminar = True

def plot_botones(toolbar, choice):
    if choice == "home":
        toolbar.home()
    elif choice == "movement":
        toolbar.pan()
    elif choice == "zoom":
        toolbar.zoom()
    elif choice == "save":
        toolbar.save_figure()
    else:
        print("Revisar código")

def funcion_principal():
    datos = obtener_valores()
    grafico = graficar(datos)
    tabla_datos(datos)
    return grafico


# Crear botones personalizados para matplotlib
btn_home = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Reset Pos.", command=lambda: plot_botones(toolbar, "home"))
btn_home.grid(column=0, row=0, padx=5)

btn_zoom = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Zoom", command=lambda: plot_botones(toolbar, "zoom"))
btn_zoom.grid(column=1, row=0, padx=5)

btn_movement = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Moverse", command=lambda: plot_botones(toolbar, "movement"))
btn_movement.grid(column=2, row=0, padx=5)

btn_guardar = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Guardar", command=lambda: plot_botones(toolbar, "save"))
btn_guardar.grid(column=3, row=0, padx=5)

txt_1_label = ctk.CTkLabel(botones_frame, width=5, height=10, text="Pos. Inicial:", font=ctk.CTkFont(size=12, weight="bold"))
txt_1_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="sew")

txt_1 = ctk.CTkTextbox(botones_frame, width=50, height=8, activate_scrollbars=False)
txt_1.grid(row=1, column=0, pady=5, padx=5, sticky="ne")

txt_1_km_or_m = ctk.CTkSegmentedButton(botones_frame, width=10, height=30, values=["Km", "m"], corner_radius=9, border_width=0, command=sbutton_get)
txt_1_km_or_m.grid(row=1, column=1, padx=5, pady=6, sticky="wns")
txt_1_km_or_m.set("m")

tabla_valores = ttk.Treeview(tabla_frame, columns=("Altura", "Tiempo", "Velocidad"))
tabla_valores.configure(height=25)
tabla_valores.column("#0", width=0, stretch=tk.NO)
tabla_valores.column("Altura", width=100, )
tabla_valores.column("Tiempo", width=100)
tabla_valores.column("Velocidad", width=100)
tabla_valores.heading("Altura", text="Altura")
tabla_valores.heading("Tiempo", text="Tiempo")
tabla_valores.heading("Velocidad", text="Velocidad")
tabla_valores.configure(style="Custom.Treeview")
tabla_valores.grid(column=0, row=0, pady=17,padx=7,sticky="ns")


g_combo = ctk.CTkLabel(botones_frame, width=5, height=10, text="Tipo de Gravedad:", font=ctk.CTkFont(size=12, weight="bold"))
g_combo.grid(row=2, column=0, columnspan=2, pady=15, sticky="sew")

g_combo = ctk.CTkComboBox(botones_frame, height=20, width=50, values=['Tierra', 'Luna', 'Saturno', 'Neptuno', 'Júpiter'], corner_radius=15, border_width=0)
g_combo.grid(row=3, column=0, columnspan=2, padx=10, pady=15, sticky='new')
g_combo.set('Tierra')

btn_5 = ctk.CTkButton(botones_frame, width=5, height=15, text="Calcular",
                      font=ctk.CTkFont(size=12, weight="bold"), command=funcion_principal)
btn_5.grid(row=4, column=0, columnspan=2, padx=16, pady=25, sticky='new')


def cerrar_ventana():
    ventana_principal.quit()
    ventana_principal.destroy()

# Loop principal de la Ventana
ventana_principal.protocol("WM_DELETE_WINDOW", cerrar_ventana)
ventana_principal.mainloop()