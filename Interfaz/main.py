import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import seaborn as sns
import formula_caidalibre as formula


# Setup principal de la ventana
ventana_principal = ctk.CTk()
ventana_principal.title("Proyecto")
ventana_principal.geometry("1000x600")
ventana_principal.resizable(False, False)
sns.set(style="darkgrid")

grafico_frame = ctk.CTkFrame(ventana_principal, width=740, height=560)
grafico_frame.grid(row=0, column=1, pady=20)

botones_frame = ctk.CTkFrame(ventana_principal, width=200, height=560)
botones_frame.grid(row=0, column=0, padx=20, pady=10)

frame_plot_botones = ctk.CTkFrame(ventana_principal, width=740, height=200)
frame_plot_botones.grid(row=1, column=1, padx=20, pady=10)

lienzo = None
toolbar = None
def get_g():
    values_g = ['Tierra', 'Luna', 'Saturno', 'Neptuno', 'Júpiter']
    values_n = [9.8, 1.6, 10.44, 11.15, 24.79]

    g = g_combo.get()
        
    for i in values_g, values_n:
        if i[0] == g:

            return i[1]
            break

def sbutton_get(value):
    global u_longitud
    u_longitud = value
    return u_longitud

def obtener_valores():
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
    fig = formula.caida_libre(param1, g)
    lienzo = FigureCanvasTkAgg(fig, master=grafico_frame)
    toolbar = NavigationToolbar2Tk(lienzo)
    toolbar.update()
    toolbar.pack()
    toolbar.pack_forget()
    return fig, lienzo.draw(), lienzo.get_tk_widget().grid(padx=40, pady=40)

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
    try:
        altura = obtener_valores()
        grafico = graficar(altura)
        return grafico

    except:
        print("Valor inválido")


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

checkbx_g = ctk.CTkLabel(botones_frame, width=5, height=10, text="Tipo de Gravedad:", font=ctk.CTkFont(size=12, weight="bold"))
checkbx_g.grid(row=2, column=0, columnspan=2, pady=15, sticky="sew")

g_combo = ctk.CTkComboBox(botones_frame, height=20, width=50, values=['Tierra', 'Luna', 'Saturno', 'Neptuno', 'Júpiter'], corner_radius=15, border_width=0)
g_combo.grid(row=3, column=0, columnspan=2, padx=10, pady=15, sticky='new')
g_combo.set('Tierra')

btn_5 = ctk.CTkButton(botones_frame, width=5, height=15, text="Calcular",
                      font=ctk.CTkFont(size=12, weight="bold"), command=funcion_principal)
btn_5.grid(row=4, column=0, columnspan=2, padx=16, pady=25, sticky='new')


# Loop principal de la Ventana
ventana_principal.mainloop()
