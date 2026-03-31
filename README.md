# 🐱 **Cat Sketch Generation with GANs**

Este proyecto implementa una Red Generativa Antagónica (GAN) para convertir imágenes de gatos en sketches tipo dibujo a lápiz, utilizando una arquitectura basada en Pix2Pix.

## Descripción

El objetivo es aprender una transformación de imágenes (image-to-image translation), donde el modelo recibe una fotografía de un gato y genera su versión en sketch. Para esto se utiliza un enfoque supervisado con pares de imágenes alineadas (foto | sketch).

## Modelo

El modelo está compuesto por:

- Generador (U-Net 256): transforma la imagen real en un sketch, conservando la estructura.
- Discriminador: evalúa si los sketches son reales o generados.

La función de pérdida combina:

- GAN Loss: mejora el realismo
- L1 Loss: mantiene la similitud con la imagen original

## Dataset

El dataset está organizado en formato alineado:

train/
  ├── img1.jpg   (A | B)
  ├── img2.jpg
test/
  ├── img1.jpg   (A | B)

Donde:

A: imagen real (foto)
B: sketch generado con OpenCV

## Entrenamiento

El modelo se entrena con:

- Imágenes de tamaño: 256×256
- Batch size: 4
- 15 épocas iniciales + 5 de ajuste fino
- lambda_L1 = 25

## Evaluación
Se evaluó el modelo con métricas cuantitativas y cualitativas:

**Métricas**:
- SSIM: 0.47 → similitud estructural moderada
- PSNR: 9.81 → calidad limitada con diferencias visibles
- FID: 106.31 → diferencia notable entre distribuciones

También se implementó una métrica personalizada tipo FID, basada en:

- distancia entre medias
- determinante de covarianzas

## Estructura del proyecto

## Estructura del proyecto

```bash
cats-sketch-gan/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── cats_photos/
│   │   ├── cats_sketches/
│   │   └── cats_test/
│   ├── processed/
│   │   ├── train/
│   │   └── test/
│   └── interim/
│       └── train/
│           ├── A/
│           └── B/
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_MIH_Modeling.ipynb
│   └── 03.1_MIH_Modeling.ipynb
├── src/
│   ├── data/
│   │   ├── make_dataset.py
│   │   └── make_test_dataset.py
│   ├── models/
│   │   ├── apdrawing_gan/
│   │   │   ├── train.py
│   │   │   └── test.py
│   │   ├── train_model.py
│   │   └── test_model.py
├── models/
├── reports/
│   └── figures/
└── results/
    └── cats_pix2pix/
```