import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def deshacer():
    """Esta funcion deshace un cambio en el archivo de texto"""
    txt_edicion.edit_undo()


def rehacer():
    """Esta funcion rehace un cambio en el archivo de texto"""
    txt_edicion.edit_redo()


def abrir_archivo():
    """Esta funcion nos permite acceder de manera grafica a cualquier archivo 
    de tipo texto (osea que terminen en .txt) y extraer su informacion para
    reemplazar la que este en el widget de texto.
    En caso de que no se seleccione ningun archivo no se ejecutara nada."""
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*"),]
    )
    if not filepath:
        return
    txt_edicion.delete("1.0", tk.END)
    with open(filepath, "r", encoding="utf-8") as archivo_entrada:
        texto = archivo_entrada.read()
        txt_edicion.insert(tk.END, texto)
        ventana.title(f"Editor de texto - {filepath}")


def eliminar_label():
    """El proposito de esta funcion es sencillo, eliminara un mensaje de error
    si se intenta guardar sin seleccionar un archivo."""
    error.destroy()

    
def guardar_archivo():
    """Esta funcion permite actualizar la informacion de un archivo, si no se
    ha seleccionado un archivo muestra en la interfaz un mensaje de error"""
    try:
        with open(filepath, "w", encoding="utf-8") as archivo:
            texto = txt_edicion.get("1.0", tk.END)  
            archivo.write(texto)
    except:
        mensaje = "Error \nNo se ha seleccionado ningun archivo."
        error.config(text=mensaje)
        ventana.after(3000, eliminar_label)


def guardar_como():
    """Esta funcion permite crear un archivo para guardar la informacion del 
    widget de texto. Si no se selecciona un archivo no se ejecutara nada"""
    global filepath
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as archivo_salida:
        texto = txt_edicion.get("1.0", tk.END)
        archivo_salida.write(texto)
        ventana.title(f"Editor de texto - {filepath}")


#Creacion de la ventana
ventana = tk.Tk()
ventana.title("Editor de texto")
ventana.rowconfigure(0, minsize=800, weight=1)
ventana.columnconfigure(1, minsize=800, weight=1)

#Creacion de un frame que va a contener los botones y el espacio restante
#se utilizara para el widget de texto
txt_edicion = tk.Text(ventana, undo=True)
frm_botones = tk.Frame(master=ventana, relief=tk.RAISED, bd=2)

#Creacion de los botones 
bt_abrir = tk.Button(master=frm_botones, text="Abrir", command=abrir_archivo)
bt_guardar = tk.Button(master=frm_botones, text="Guardar", command=guardar_archivo)
bt_guardar_como = tk.Button(master=frm_botones, text="Guardar como...", command=guardar_como)
bt_deshacer = tk.Button(master=frm_botones, text="Deshacer", command=deshacer)
bt_rehacer = tk.Button(master=frm_botones, text="Rehacer", command=rehacer)

#Asignar el espacio de los botones 
bt_abrir.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
bt_guardar.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
bt_guardar_como.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
bt_deshacer.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
bt_rehacer.grid(row=4, column=0, sticky="ew", padx=5)

error = tk.Label(master=frm_botones, text="", wraplength=100)
error.grid(row=5, column=0, pady=100, sticky="s")

#Asignar el espacio para el frame y el widget de texto
frm_botones.grid(row=0, column=0, sticky="ns")
txt_edicion.grid(row=0, column=1, sticky="nsew")

ventana.mainloop()