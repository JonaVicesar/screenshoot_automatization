from PIL import Image
import os

def extract_gif_frames(gif_path, output_folder, start_number=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    
    with Image.open(gif_path) as gif:
        
        cantidad_frames = gif.n_frames
        print(f"Total de frames en el GIF: {cantidad_frames}")

        for frame in range(cantidad_frames):
           
            gif.seek(frame)
 
            frame_actual = gif.copy()

            frame_filename = f"{start_number + frame}.png"
            frame_path = os.path.join(output_folder, frame_filename)

            frame_actual.save(frame_path, 'PNG')
            print(f"Guardado: {frame_filename}")

if __name__ == "__main__":
    # Ruta al archivo GIF
    gif_path = "16.gif"
    # Carpeta donde se guardarán los frames
    output_folder = "frames_output"
    # Número inicial para nombrar los frames
    start_number = 183
    
    extract_gif_frames(gif_path, output_folder, start_number)