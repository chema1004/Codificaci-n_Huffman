import tkinter as tk
from tkinter import filedialog
from collections import Counter
import shutil

def contar_caracteres_lineas(archivo_entrada, archivo_salida):
    try: 
        with open(archivo_entrada, 'r', encoding='utf-8') as f_in: 
            contenido = f_in.readlines()  # Leer todas las líneas del archivo
            num_lineas = len(contenido)  # Contar las líneas
            contenido = ''.join(contenido)  # Unir todas las líneas en una sola cadena
            frecuencia_caracteres = Counter(contenido)
            caracteres_ordenados = sorted(frecuencia_caracteres.items(), key=lambda x: x[1], reverse=True)  
            
            # Escribir resultados en el archivo de salida
            with open(archivo_salida, 'w', encoding='utf-8') as f_out:
                f_out.write("Caracteres ordenados por frecuencia:\n")
                for caracter, frecuencia in caracteres_ordenados:
                    f_out.write(f"{caracter}: {frecuencia}\n")
                f_out.write(f"Número total de líneas: {num_lineas}\n")
                
            print(f"Resultados guardados en '{archivo_salida}'")
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def cargar_archivo():
    filename = filedialog.askopenfilename()
    print("Archivo seleccionado:", filename)
    return filename

def guardar_resultados(contenido, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as f_out:
        f_out.write(contenido)
    print(f"Resultados guardados en '{archivo_salida}'")

def procesar_archivo():
    archivo_entrada = cargar_archivo()
    if archivo_entrada:
        archivo_salida = 'resultados.txt'
        contar_caracteres_lineas(archivo_entrada, archivo_salida)
        with open(archivo_salida, 'r', encoding='utf-8') as f:
            resultados = f.read()
            guardar_resultados(resultados, archivo_salida)

def descargar_resultados():
    archivo_salida = 'resultados.txt'
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
    if filename:
        shutil.copy(archivo_salida, filename)
        print(f"Resultados guardados como '{filename}'")

root = tk.Tk()
root.title("Contador de Caracteres y Líneas")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

procesar_button = tk.Button(frame, text="Procesar Archivo", command=procesar_archivo)
procesar_button.pack(side=tk.LEFT)

descargar_button = tk.Button(frame, text="Descargar Resultados", command=descargar_resultados)
descargar_button.pack(side=tk.LEFT)

root.mainloop()