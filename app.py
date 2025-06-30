from tkinter import Image
from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf

# Inisialisasi aplikasi Flask
app = Flask(__name__, static_folder='static', template_folder='templates')

# Load model
model = tf.keras.models.load_model('fashion.h5')

# Label mapping
label_map = {
    "T-shirt/top" : 0,
    "Trouser" : 1,
    "Pullover" : 2,
    "Dress" : 3,
    "Coat" : 4,
    "Sandal" : 5,
    "Shirt" : 6,
    "Sneaker" : 7,
    "Bag" :8,
    "Ankle Boot" :9,
    "peci" :10,
    "hijab" :11,
    "teluk belanga" :12,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_array = data.get('input')

        if not input_array or len(input_array) != 28 * 28:
            return jsonify({'error': 'Input gambar tidak valid'}), 400

        # Convert list ke numpy array dan reshape
        input_np = np.array(input_array, dtype=np.float32).reshape(1, 28, 28, 1)

        # Prediksi
        prediction = model.predict(input_np)
        predicted_index = int(np.argmax(prediction))
        predicted_label = label_map.get(predicted_index, 'Tidak diketahui')

        return jsonify({'prediction': predicted_label})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)
