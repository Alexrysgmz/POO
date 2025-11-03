from tkinter import *

def hazClic():
    etiqueta.config(
    text="POO con Python",
    bg="darkgreen",
    fg="red",
    cursor="spider",
    )

def regresarValores():
    etiqueta.config(
    text="Bienvenidos a Tkinter",
    bg="lightblue",
    fg="darkblue"
    )
    

ventana=Tk()

ventana.title("Personalizar Widgets u Objetos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=SOLID,
    border=2
)
etiqueta.pack(pady=25)

boton1=Button(ventana,text="Haz clíc aquí...",command=hazClic)
boton1.config(
    bg="blue",
    fg="white",
    width=15,
    # height=4,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="yellow",
    activebackground="red",
)
boton1.pack(pady=15)

boton2=Button(ventana,text="Regresar Valores...",command=regresarValores)
boton2.config(
    bg="red",
    fg="black",
    width=15,
    # height=4,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="red",
)
boton2.pack(pady=15)

ventana.mainloop()