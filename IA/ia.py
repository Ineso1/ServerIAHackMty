import tensorflow as tf
import numpy as np
from tensorflow import keras

batch_size = 32
img_height = 180
img_width = 180

model = keras.models.load_model('model.h5')

# Check its architecture
model.summary()

# Evaluate the model
img = keras.preprocessing.image.load_img('./ambar.jpeg', target_size=(img_height, img_width))

img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)