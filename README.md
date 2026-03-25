Project_GANs
==============================


Project Organization
------------
cats-sketch-gan/
│
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── cats_photos/
│   │
│   ├── processed/
│   │   ├── train/
│   │   │   └── AB/   ← imágenes lado a lado
│   │   └── test/
│   │       └── AB/
│   │
│   └── interim/
│       └── sketches/
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_results_visualization.ipynb
│
├── src/
│   ├── data/
│   │   ├── make_dataset.py
│   │   └── make_test_dataset.py
│   │
│   ├── models/
│   │   ├── apdrawing_gan/       
│   │   │   ├── __init__.py
│   │   │   ├── train.py
│   │   │   ├── test.py
│   │   │
│   │   │   ├── models/
│   │   │   │   ├── base_model.py
│   │   │   │   ├── apdrawing_gan_model.py
│   │   │   │   └── networks.py
│   │   │   │
│   │   │   ├── options/
│   │   │   │   ├── base_options.py
│   │   │   │   ├── train_options.py
│   │   │   │   └── test_options.py
│   │   │   │
│   │   │   ├── data/
│   │   │   │   └── aligned_dataset.py
│   │   │   │
│   │   │   └── util/
│   │   │       └── util.py
│   │
│   │   ├── train_model.py   
│   │   └── test_model.py
│
├── models/   ← aquí se guardan los .pth
│
├── reports/
│   └── figures/
│
└── results/
    └── cats_pix2pix/


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
