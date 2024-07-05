import requests
import base64
from PIL import Image
import io
import os
from app.utils import get_next_image_number
from flask import current_app, url_for

def generate_image(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config["API_TOKEN"]}'
    }
    data = {'prompt': prompt}

    response = requests.post(current_app.config['API_URL'], json=data, headers=headers)
    response.raise_for_status()

    response_data = response.json()
    base64_image = response_data['result']

    image_data = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(image_data))

    image_number = get_next_image_number()
    image_filename = f'output_{image_number:03d}.png'
    image_path = os.path.join('static', 'images', image_filename)
    image.save(image_path)

    return image_filename