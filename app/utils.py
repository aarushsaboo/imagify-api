import glob
import os

def get_next_image_number():
    existing_images = glob.glob('static/images/output_*.png')
    return len(existing_images) + 1