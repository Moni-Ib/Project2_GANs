import cv2
import os

input_folder = "../../data/raw/cats_photos"
output_folder = "../../data/raw/cats_sketches"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):

        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Redimensionar
        img = cv2.resize(img, (256, 256))

        # Escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Pencil Sketch 
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256)

        # Bordes (Canny) 
        edges = cv2.Canny(gray, 50, 150)

        # Invertir edges (para fondo blanco)
        edges = 255 - edges

        # Combinar 
        combined = cv2.addWeighted(sketch, 0.7, edges, 0.3, 0)

        # Aumentar contraste 
        combined = cv2.normalize(combined, None, 0, 255, cv2.NORM_MINMAX)

        # Umbral (líneas más negras) 
        _, combined = cv2.threshold(combined, 200, 255, cv2.THRESH_BINARY)

        # Guardar
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, combined)

print("Sketches generados")