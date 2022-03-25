#Import tensorflow Library, import Numpy Library, import Keras
import tensorflow as tf
import numpy as np
from tensorflow import keras

#Define the Deep Learning Model
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

#Provide the training Data
xs = np.array([1.0, 0.0, 2.0, 3.0, 4.0, 5.0], dtype=float)       <== Number of Bedrooms
ys = np.array([1.0, 0.5, 1.5, 2.0, 2.5, 3.0], dtype=float)       <== Price of the house in $100,000

#Train the Neural Network
model.fit(xs, ys, epochs=500)

#Score the model i.e., make a guess for x = 7 (Price of a 7 bedroom house)
print(model.predict([7.0]))
