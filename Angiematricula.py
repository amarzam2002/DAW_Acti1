import tkinter as tk
from tkinter import messagebox

def submit_form():
    messagebox.showinfo("Formulario de Matrícula", "Formulario enviado con éxito!")

window = tk.Tk()
window.title("Formulario de Matrícula")

frame = tk.Frame(window)
frame.pack()

name_label = tk.Label(frame, text="Nombre:")
name_label.pack()
name_entry = tk.Entry(frame)
name_entry.pack()

surname_label = tk.Label(frame, text="Apellido:")
surname_label.pack()
surname_entry = tk.Entry(frame)
surname_entry.pack()

id_label = tk.Label(frame, text="ID de Estudiante:")
id_label.pack()
id_entry = tk.Entry(frame)
id_entry.pack()

submit_button = tk.Button(frame, text="Enviar", command=submit_form)
submit_button.pack()

window.mainloop()
