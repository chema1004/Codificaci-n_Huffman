from collections import Counter

def contar_caracteres_lineas(archivo_entrada):
    try: 
        with open(archivo_entrada, 'r', encoding='utf-8') as f_in: 
            contenido = f_in.readlines()  # Leer todas las líneas del archivo
            num_lineas = len(contenido)  # Contar las líneas
            contenido = ''.join(contenido)  # Unir todas las líneas en una sola cadena
            frecuencia_caracteres = Counter(contenido)
            caracteres_ordenados = sorted(frecuencia_caracteres.items(), key=lambda x: x[1], reverse=True)  
            
            # Imprimir resultados en la terminal
            print("Caracteres ordenados por frecuencia:")
            for caracter, frecuencia in caracteres_ordenados:
                if caracter != ' ' and caracter != '\n':  # Ignorar espacios en blanco y saltos de línea
                    print(f"'{caracter}': {frecuencia}")
            print(f"Número total de líneas: {num_lineas}")

    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Uso de la función
nombre_archivo_entrada = 'liibro.txt'
contar_caracteres_lineas(nombre_archivo_entrada)
