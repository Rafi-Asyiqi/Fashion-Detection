# Fashion Item Classification Web App 👕👖🧥

This project is a web application built using **Flask** and **TensorFlow** that allows users to classify various fashion items by uploading an image. It uses a trained deep learning model to predict the category of clothing, including traditional attire like **peci**, **hijab**, and **teluk belanga**.

## 🚀 Features
- Upload an image of clothing (e.g., T-shirt, trouser, dress, hijab, etc.)
- Real-time prediction using a TensorFlow deep learning model
- Clean and responsive UI using HTML, CSS, and JavaScript
- Support for traditional fashion items in classification

## 🧠 Model
The model (`fashion.h5`) is a CNN trained on an extended Fashion MNIST dataset that includes additional traditional clothing classes.

## 🧾 About Fashion MNIST Dataset
The Fashion MNIST dataset is a benchmark image dataset created by Zalando Research as a more challenging replacement for the classic MNIST digit dataset. It consists of 70,000 grayscale images of fashion items categorized into 10 classes. Each image is 28x28 pixels, and represents a single item of clothing, such as a shirt, sneaker, or bag.

Fashion MNIST is widely used in the machine learning community for developing and testing image classification models due to its simplicity, small size, and relevance to real-world applications in the retail and fashion industries.
📦 Dataset Structure:
- Training set: 60,000 images
- Test set: 10,000 images
- Image size: 28x28 pixels, grayscale
- Number of classes: 10

link : https://www.kaggle.com/datasets/zalando-research/fashionmnist

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
│   └── index.html
│   └── layout.html
│   └── kontak.html
│   └── tentang.html
│   └── uji_gambar.html   # Frontend HTML
├── static/
│   └── uploads/
│   └── styles.css        # Static assets like logo image
└── README.md             # Project documentation
```

## ⚙️ How to Run Locally
1. Clone this repository:
```bash
git clone https://github.com/Rafi-Asyiqi/Fashion-Detection.git
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
![image](https://github.com/user-attachments/assets/88956195-3db5-4cb8-be2c-92d4cb654c51)



## 🔮 Future Improvements
To enhance the performance and scalability of this clothing classification system, the following improvements are planned for future development:

Add More Clothing Categories
Currently, the system supports a limited number of clothing types. Future versions will expand the number of categories to include more diverse fashion items such as accessories (e.g., hats, scarves), traditional clothing, and subcategories (e.g., short sleeve vs. long sleeve shirts) to better reflect real-world product variety.

Improve Image Preprocessing Pipeline
Enhancing the image preprocessing step — such as implementing advanced techniques like background removal, edge detection, image sharpening, or color normalization — can significantly improve the quality of input data and lead to better model predictions.

Enhance Model Accuracy with More Diverse Datasets
Training the model on more diverse and real-world datasets, including images from various lighting conditions, angles, and backgrounds, will improve its robustness and generalization. Integrating custom datasets alongside Fashion MNIST can help the model perform better in practical applications, such as in e-commerce platforms or mobile apps.



## 📁 Dataset
This project uses a combination of public datasets and a custom-built dataset to classify various types of clothing items, including traditional Indonesian attire.

1. Fashion MNIST Dataset (from Kaggle)
A widely-used public dataset obtained from Kaggle, the Fashion MNIST dataset includes 70,000 grayscale images (28x28 px) representing 10 categories of modern fashion items such as T-shirts, trousers, coats, sneakers, and more. It serves as the primary dataset for training the model on common, everyday clothing.

link kaggle : https://www.kaggle.com/code/gpreda/cnn-with-tensorflow-keras-for-fashion-mnist/notebook

2. Custom Traditional Clothing Dataset
To complement the Fashion MNIST dataset and address the lack of cultural variety, a custom dataset was created by collecting images from online sources. This dataset contains colored images of traditional Indonesian clothing items, organized into the following labeled folders:
📁 hijab
📁 peci
📁 teluk belanga
Each folder contains multiple image samples representing the respective clothing category. These images were manually curated and labeled to ensure clarity and consistency. The images are used to extend the classification capability of the model beyond modern fashion and into traditional wear, helping the system recognize a broader range of clothing relevant to local cultural contexts.

## Demo Result

https://github.com/user-attachments/assets/66d02ed4-99e3-499f-a229-06b257c3e6c6



