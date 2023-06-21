import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import seaborn as sns
import formula_caidalibre as formula
import formulas_reformadas as reform
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

def sbutton_get(value):
    global u_longitud
    u_longitud = value
    return u_longitud


def Tiempo():
    tiempo = txt_2.get("0.0","end")
    return tiempo

def Velocidad_final():
    velocidad_final = txt_3.get("0.0","end")
    return velocidad_final

def Altura():
    altura =  txt_1.get("0.0","end")
    return altura

def obtener_valores():
    global txt_1
    global txt_1_km_or_m
    u_longitud = txt_1_km_or_m.get()
    altura = txt_1.get("0.0", "end")
    altura = float(altura)
    if u_longitud == "m":
        return altura
    else:
        altura = altura * 1000
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
    eliminar_grafico()
    fig = formula.caida_libre(param1)
    lienzo = FigureCanvasTkAgg(fig, master=grafico_frame)
    toolbar = NavigationToolbar2Tk(lienzo)
    toolbar.update()
    toolbar.pack()
    toolbar.pack_forget()
    return fig, lienzo.draw(), lienzo.get_tk_widget().pack()


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


#def funcion_principal():
#    tiempo = Tiempo()
#    velocidad = Velocidad_final()
#    altura = Altura()
#    print(tiempo)
#    print(velocidad)
#    print(altura)

  #  try:
 #       altura = obtener_valores()
#        grafico = graficar(altura)
#        return grafico
#
#    except:
#        print("Valor inválido")

def funcion_principal():
    user_tiempo = Tiempo()
    user_velocidad = Velocidad_final()
    user_altura = Altura()
    print("user_tiempo: ", user_tiempo)
    if len(user_tiempo) != 0:
            print("dentro del try")
            altura = reform.Altura_Tiempo(user_tiempo)
            print("altura = ",altura)
            grafico = graficar(altura)
            return grafico


    elif len(user_altura) != 0:


# Crear botones personalizados para matplotlib
btn_home = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Reset Pos.",
                         command=lambda: plot_botones(toolbar, "home"))
btn_home.grid(column=0, row=0, padx=5)

btn_zoom = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Zoom",
                         command=lambda: plot_botones(toolbar, "zoom"))
btn_zoom.grid(column=1, row=0, padx=5)

btn_movement = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Moverse",
                             command=lambda: plot_botones(toolbar, "movement"))
btn_movement.grid(column=2, row=0, padx=5)

btn_guardar = ctk.CTkButton(frame_plot_botones, width=10, height=10, text="Guardar",
                            command=lambda: plot_botones(toolbar, "save"))
btn_guardar.grid(column=3, row=0, padx=5)

txt_1_label = ctk.CTkLabel(botones_frame, width=5, height=10, text="Pos. Altura:",font=ctk.CTkFont(size=12, weight="bold"))
txt_1_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="sew")
txt_1 = ctk.CTkTextbox(botones_frame, width=50, height=8, activate_scrollbars=False)
txt_1.grid(row=1, column=0, pady=5, padx=5, sticky="ne")
txt_1_km_or_m = ctk.CTkSegmentedButton(botones_frame, width=10, height=30, values=["Km", "m"], corner_radius=9,border_width=0, command=sbutton_get)
txt_1_km_or_m.grid(row=1, column=1, padx=5, pady=6, sticky="wns")
txt_1_km_or_m.set("m")

txt_2_label = ctk.CTkLabel(botones_frame, width=5, height=10, text="Tiempo",font=ctk.CTkFont(size=12, weight="bold"))
txt_2_label.grid(row=5, column=0, columnspan=2, pady=15, sticky="sew")
txt_2 = ctk.CTkTextbox(botones_frame, width=30, height=8, activate_scrollbars=False)
txt_2.grid(row=6, column=0, pady=5, padx=50, sticky="we",columnspan=2)

txt_3_label = ctk.CTkLabel(botones_frame, width=5, height=10, text="Velocidad Final",font=ctk.CTkFont(size=12, weight="bold"))
txt_3_label.grid(row=7, column=0, columnspan=2, pady=15, sticky="sew")
txt_3 = ctk.CTkTextbox(botones_frame, width=50, height=8, activate_scrollbars=False)
txt_3.grid(row=8, column=0, pady=5, padx=50, sticky="we",columnspan=2)

btn_5 = ctk.CTkButton(botones_frame, width=5, height=15, text="Calcular", font=ctk.CTkFont(size=12, weight="bold"),command=funcion_principal)
btn_5.grid(row=10, column=0, columnspan=2, padx=16, pady=5, sticky="we")

# Loop principal de la Ventana
ventana_principal.mainloop()