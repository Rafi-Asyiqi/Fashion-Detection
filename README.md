# Fashion Item Classification Web App 👕👖🧥

This project is a web application built using **Flask** and **TensorFlow** that allows users to classify various fashion items by uploading an image. It uses a trained deep learning model to predict the category of clothing, including traditional attire like **peci**, **hijab**, and **teluk belanga**.

## 🚀 Features
- Upload an image of clothing (e.g., T-shirt, trouser, dress, hijab, etc.)
- Real-time prediction using a TensorFlow deep learning model
- Clean and responsive UI using HTML, CSS, and JavaScript
- Support for traditional fashion items in classification

## 🧠 Model
The model (`fashion.h5`) is a CNN trained on an extended Fashion MNIST dataset that includes additional traditional clothing classes.

## 🛠 Technologies Used
- Flask (Python web framework)
- TensorFlow (Deep Learning)
- Numpy (Numerical computations)
- HTML/CSS & JavaScript (Frontend)
- Tkinter (Only partially included, not used in this web version)

## 📁 Project Structure
```
├── app.py                # Flask backend
├── fashion.h5            # Pre-trained model
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   └── uploads/          # Static assets like logo image
└── README.md             # Project documentation
```

## ⚙️ How to Run Locally
1. Clone this repository:
```bash
git clone https://github.com/yourusername/fashion-classification-app.git
cd fashion-classification-app
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to:
```
http://127.0.0.1:5000/
```

## 📷 Sample UI
![Sample UI](static/uploads/sample_ui.png)

## ✨ Future Improvements
- Add more clothing categories
- Improve image preprocessing pipeline
- Enhance model accuracy with more diverse datasets
- Add drag-and-drop upload and camera capture

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.