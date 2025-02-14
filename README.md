# 🖼️ Frames Getter - Extrae Frames de GIFs

Este script permite extraer todos los frames de un archivo GIF y guardarlos como imágenes PNG numeradas de manera consecutiva.

## 🚀 Requisitos

Antes de ejecutar el script, asegúrate de tener instalado **Python 3** y la librería Pillow:

```sh
pip install pillow
```

## 📦 Uso

1. Coloca el GIF que deseas procesar en la misma carpeta del script.
2. Modifica el archivo `frames_Getter.py` y cambia la variable `gif_path` con el nombre de tu GIF.
3. Ejecuta el script:

```sh
python frames_Getter.py
```

Los frames extraídos se guardarán en la carpeta `frames_output/` automáticamente.

## ⚙️ Configuración

Puedes personalizar algunas opciones en el código:

- **`gif_path`** → Ruta del GIF a procesar.
- **`output_folder`** → Carpeta donde se guardarán los frames.
- **`start_number`** → Número inicial para nombrar los archivos PNG.

Ejemplo en el código:

```python
gif_path = "mi_gif.gif"
output_folder = "mis_frames"
start_number = 1
```

## 📌 Ejemplo de salida

Si el GIF tiene 5 frames y `start_number = 100`, los archivos guardados serán:

```
frames_output/100.png
frames_output/101.png
frames_output/102.png
frames_output/103.png
frames_output/104.png
```
## 🔗 Proyecto

Este script lo hice para trabajar mas rapido con otro proyecto, un proyecto de animacion que puedes ver encontrar en el repo de abajo

[🚀(https://github.com/JonaVicesar/Animation-Project)

