import cv2
from tkinter import filedialog
import tkinter as tk
import os

# Definir la fuente de texto
tipotexto = ("Comic Sans MS", 12, "italic")

# Función para procesar la imagen y mostrarla


def procesarImagen(imagen):
    imagenModificada = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    colorInvertido = cv2.bitwise_not(imagenModificada)
    desenfoque = cv2.GaussianBlur(colorInvertido, (21, 21), 0)
    desenfoqueInvertido = cv2.bitwise_not(desenfoque)
    dibujo = cv2.divide(imagenModificada, desenfoqueInvertido, scale=256.0)
    cv2.imshow('Dibujo Modificado', dibujo)

# Función para cargar una imagen desde el archivo


def cargarImagen(ruta):
    imagen = cv2.imread(ruta)
    return imagen

# Función para procesar la imagen seleccionada


def procesarSeleccion(imagen):
    cv2.imshow('La imagen original', imagen)
    procesarImagen(imagen)

# Función para cerrar todas las ventanas de OpenCV


def cerrarVentanasOpenCV():
    cv2.destroyAllWindows()


# Crear una ventana de tkinter
ventana = tk.Tk()
ventana.geometry("400x330")
ventana.title('Procesador de Imágenes')

# Obtener la carpeta actual del script
carpetaDeTodosLosArchivos = os.path.dirname(__file__)

# Establecer el icono de la ventana
iconoPath = os.path.join(carpetaDeTodosLosArchivos, "perropepsi.ico")
if os.path.exists(iconoPath):
    ventana.iconbitmap(iconoPath)

# Lista de rutas de imágenes predefinidas
rutasImagenes = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg', 'e.jpg', 'f.jpg']

# Crear botones gráficos para representar las imágenes
botonesImagenes = []
aumentarPlace = 10
for ruta in rutasImagenes:
    imagen = cargarImagen(ruta)
    boton = tk.Button(ventana, text=f'Imagen {len(botonesImagenes) + 1}', font=tipotexto,
                      command=lambda img=imagen: procesarSeleccion(img))
    botonesImagenes.append(boton)
    boton.place(x=10, y=0 + aumentarPlace)
    aumentarPlace += 42

# Botón para salir
botonSalir = tk.Button(ventana, font=tipotexto, text='Salir', command=lambda: [
                       cerrarVentanasOpenCV(), ventana.destroy()])
botonSalir.place(x=150, y=255)

# Etiqueta al pie de la ventana
etiqueta = tk.Label(ventana, background="Brown1",
                    text="~ VictoriaVMC", font=tipotexto, justify=tk.CENTER)
etiqueta.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

ventana.mainloop()
