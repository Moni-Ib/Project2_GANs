import os

os.system("""
python src/models/apdrawing_gan/train.py \
--dataroot ./data/processed \
--name cats_pix2pix \
--model apdrawing_gan \
--netG unet_256 \
--dataset_mode aligned \
--which_direction AtoB \
--display_id -1 \
--batch_size 4 \
--niter 25 \
--niter_decay 25 \
--fineSize 256 \
--loadSize 256 \
--gpu_ids 0 \
--lambda_L1 50 \
--num_threads 2
""")