import os
from PIL import Image

path_A = '../../data/interim/train/A'
path_B = '../../data/interim/train/B'
output_path = '../../data/processed/train'

os.makedirs(output_path, exist_ok=True)

files = sorted(os.listdir(path_A))

for file in files:
    img_A = Image.open(os.path.join(path_A, file)).convert('RGB')
    img_B = Image.open(os.path.join(path_B, file)).convert('RGB')

    # asegurar mismo tamaño
    img_B = img_B.resize(img_A.size)

    # concatenar horizontalmente
    new_img = Image.new('RGB', (img_A.width * 2, img_A.height))
    new_img.paste(img_A, (0, 0))
    new_img.paste(img_B, (img_A.width, 0))

    new_img.save(os.path.join(output_path, file))