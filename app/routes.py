from flask import Blueprint, request, jsonify
from app.image_generator import generate_image
import os
from flask import send_file, abort, current_app, send_from_directory

main = Blueprint('main', __name__)

@main.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    try:
        image_filename = generate_image(prompt)
        return jsonify({'image_url': f'/static/images/{image_filename}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
# These are the end points I'm NOT using( the one below is not needed as i set my static folder's location properly)
# @main.route('/static/images/<filename>', methods=['GET'])
# def serve_image(filename):
#     image_path = os.path.join(current_app.root_path, '..', 'static', 'images', filename)
#     if os.path.exists(image_path):
#         return send_file(image_path)
#     else:
#         abort(404)
#     # return send_from_directory('static/images', filename)

@main.route('/', methods=['GET'])
def home():
    image_path = os.path.join(current_app.root_path, '..', 'static', 'images', 'output_001.png')
    return send_file(image_path, mimetype='image/png')