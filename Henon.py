import tkinter as tk
import tkinter.messagebox as messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def henon(a, b, x0, y0, iterations):
    x = [x0]
    y = [y0]

    for i in range(iterations):
        xn = y[i] + 1 - a * x[i]**2
        yn = b * x[i]
        x.append(xn)
        y.append(yn)



    binary_values = []
    for i in range(len(x)):
        binary_values.append(str(int(x[i] >= y[i])))

    binary_text = " ".join(binary_values)
    binary_textbox.delete("1.0", tk.END)
    binary_textbox.insert(tk.END, binary_text)

    # Guardar los números binarios en un archivo de texto
    with open("archivo_cifrado.txt", "w") as file:
        file.write(binary_text)

    # Mostrar mensaje de éxito al guardar el archivo
    messagebox.showinfo("Archivo cifrado","Cifrado correctamente")

def validate_float(entry):
    try:
        float(entry.get())
        return True
    except ValueError:
        return False

def validate_int(entry):
    try:
        int(entry.get())
        return True
    except ValueError:
        return False

def plot_henon():
    if not validate_float(a_entry) or not validate_float(b_entry) \
            or not validate_float(x0_entry) or not validate_float(y0_entry) \
            or not validate_int(iterations_entry):
        messagebox.showerror("Error", "Invalid input! Please enter numeric values.")
        return

    a = float(a_entry.get())
    b = float(b_entry.get())
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
    iterations = int(iterations_entry.get())

# Mensaje de errores
    if a < -1.5 or a > 1.5:
        messagebox.showerror("Error", "Valor (a) fuera del rango")
        return
    if b < 0.1 or b > 0.4:
        messagebox.showerror("Error", "Valor (b) fuera del rango")
        return

    henon(a, b, x0, y0, iterations)

# Crear la ventana principal
window = tk.Tk()
window.title("Atractor de Henón")
window.geometry("500x400")
window.configure(background="white")

# Crear el marco para los valores binarios
binary_frame = tk.Frame(window, bg="white")
binary_frame.pack(pady=10)

# Crear el menú desplegable para editar las variables
menu_frame = tk.Frame(window, bg="white")
menu_frame.pack(pady=10)

a_label = tk.Label(menu_frame, text="a:", font=("Arial", 12), bg="white")
a_label.grid(row=0, column=0, padx=5)
a_entry = tk.Entry(menu_frame, font=("Arial", 12))
a_entry.grid(row=0, column=1)
a_entry.insert(0, "0.0")

a_info_label = tk.Label(menu_frame, text="Rango aceptado: -1.5 a 1.5", font=("Arial", 10), bg="white")
a_info_label.grid(row=0, column=2)

b_label = tk.Label(menu_frame, text="b:", font=("Arial", 12), bg="white")
b_label.grid(row=1, column=0, padx=5)
b_entry = tk.Entry(menu_frame, font=("Arial", 12))
b_entry.grid(row=1, column=1)
b_entry.insert(0, "0.1")

b_info_label = tk.Label(menu_frame, text="Rango aceptado: 0.1 a 0.4", font=("Arial", 10), bg="white")
b_info_label.grid(row=1, column=2)

x0_label = tk.Label(menu_frame, text="x0:", font=("Arial", 12), bg="white")
x0_label.grid(row=2, column=0, padx=5)
x0_entry = tk.Entry(menu_frame, font=("Arial", 12))
x0_entry.grid(row=2, column=1)
x0_entry.insert(0, "0.1")


y0_label = tk.Label(menu_frame, text="y0:", font=("Arial", 12), bg="white")
y0_label.grid(row=3, column=0, padx=5)
y0_entry = tk.Entry(menu_frame, font=("Arial", 12))
y0_entry.grid(row=3, column=1)
y0_entry.insert(0, "0.1")


iterations_label = tk.Label(menu_frame, text="Iteraciones:", font=("Arial", 12), bg="white")
iterations_label.grid(row=4, column=0, padx=5)
iterations_entry = tk.Entry(menu_frame, font=("Arial", 12))
iterations_entry.grid(row=4, column=1)
iterations_entry.insert(0, "1")


# Crear el marco para la caja de texto
textbox_frame = tk.Frame(window, bg="gray")
textbox_frame.pack(pady=10)

# Crear la caja de texto para los valores binarios
binary_textbox = tk.Text(textbox_frame, height=5, width=40, font=("Arial", 12))
binary_textbox.pack()

# Función para guardar los números binarios en un archivo de texto
def save_binary_values():
    binary_values = binary_textbox.get("1.0", tk.END)
    with open("binary_values.txt", "w") as file:
        file.write(binary_values)
    messagebox.showinfo("Archivo Guardado", "Guardado correctamente")

# Crear el botón para graficar
plot_button = tk.Button(window, text="Codificar", command=plot_henon, width=7, height=1, font=("Arial", 12))
plot_button.pack(pady=10)


# Crear el botón para guardar los números binarios
save_button = tk.Button(window, text="Guardar", command=save_binary_values, width=7, height=1, font=("Arial", 12))
save_button.pack(pady=10)


# Ejecutar la ventana principal
window.mainloop()