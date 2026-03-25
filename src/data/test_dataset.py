import cv2
import os
import numpy as np

input_folder = '../../dataset/raw/cats_test'
output_folder = '../../dataset/processed/test2'

os.makedirs(output_folder, exist_ok=True)

count = 0
max_test = 100 

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        
        if count >= max_test:
            break
        
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

       
        img = cv2.resize(img, (256, 256))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256)

        edges = cv2.Canny(gray, 50, 150)
        edges = 255 - edges

        combined = cv2.addWeighted(sketch, 0.7, edges, 0.3, 0)

        combined = cv2.normalize(combined, None, 0, 255, cv2.NORM_MINMAX)

        _, combined = cv2.threshold(combined, 200, 255, cv2.THRESH_BINARY)

        sketch = cv2.cvtColor(combined, cv2.COLOR_GRAY2BGR)

        AB = np.concatenate((img, sketch), axis=1)
        #AB = np.concatenate((img, img), axis=1)
        
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, AB)

        count += 1

print("Test dataset creado")