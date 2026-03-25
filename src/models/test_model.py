import os

os.system("""
python src/models/apdrawing_gan/test.py \
--dataroot ./data/processed \
--name cats_pix2pix \
--model apdrawing_gan \
--netG unet_256 \
--dataset_mode aligned \
--which_direction AtoB \
--phase test \
--num_test 50 \
--gpu_ids 0
""")