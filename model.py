import tensorflow as tf
import numpy as np
from PIL import Image

def preprocess_image(image_path):
    # Load and resize the image
    image = Image.open(image_path).resize((50, 50))
    # Convert to a numpy array and normalize
    image_array = np.array(image).astype(np.float32) / 255.0
    # Add batch dimension
    return np.expand_dims(image_array, axis=0)

BASE_PATH_infect = "model/dataset/iarunava/cell-images-for-detecting-malaria/versions/1/cell_images/Parasitized/"
BASE_PATH_uninfect = "model/dataset/iarunava/cell-images-for-detecting-malaria/versions/1/cell_images/Uninfected/"
# Path to the new image
image_path = 'C241NThinF_IMG_20151207_124608_cell_22.png'

input_image = preprocess_image(BASE_PATH_uninfect + image_path)

model = tf.saved_model.load("model/1733281652")
predict_fn = model.signatures['serving_default']

# Pass the preprocessed image to the model
predictions = predict_fn(x=tf.convert_to_tensor(input_image))

# Access the predicted class and probabilities
predicted_class = np.argmax(predictions['probabilities'].numpy())
predicted_probabilities = predictions['probabilities'].numpy()
# print(f"Predicted Class: {predicted_class}, Probabilities: {predicted_probabilities}")

def make_prediction(img=input_image):
    # Pass the preprocessed image to the model
    predictions = predict_fn(x=tf.convert_to_tensor(img))

    # Access the predicted class and probabilities
    predicted_class = np.argmax(predictions['probabilities'].numpy())
    predicted_probabilities = predictions['probabilities'].numpy()
    # print(f"Predicted Class: {predicted_class}, Probabilities: {predicted_probabilities}")
    if predicted_class:
        return "infected"
    return "uninfected"


# print(make_prediction())
