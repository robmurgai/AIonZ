# AIonZ
Playing with ML Models on IBM System Z

## Outline:
1. Create an AI model on Z
2. Run the model
3. Show the Guess the AI model made.
4. Credits




## How would you guess the price of a house?

- Maybe you would consider the Size of the House, Area, Condition, Age of the house, School Districts, etc
- You would also want Comparable housing Prices
- And of course, the more accurate your data, the more accurate you answer.  Otherwise its Garbage in, Garbage out.




## What are you going to see
- Train on prices of 6 houses - given the number of bedrooms in each house.  
- The bedrooms will be 0 to 5.
- Guess the prices of a house with 7 bedrooms.




## Get my environment ready
Provision a VM
Install Anaconda Python Libraries
Install TensorFlow.




## Code the training part of my AI model 
Number of Bedrooms in the House
	
  
  
  
  
### Training Data with Number of Bedrooms and Price of the House
Let's say a studio starts at 50K and then for every bedroom the price goes up by 50K, so 1 bedroom is 100K, 2 Bedroom is 150K etc.
- Bedrooms: 1, Price: $100,000
- Bedrooms: 0 (Studio Apartment), Price: $50,000
- Bedrooms: 2, Price: $150,000
- Bedrooms: 3, Price: $200,000
- Bedrooms: 4, Price: $250,000
- Bedrooms: 5, Price: $300,000

PS:   The equation for the Home Price = $50,000 + $50,000  X  Num_of_Bedrooms




## Scoring the Model
I am going to ask it the price of a house with 7 Bedrooms.

Python Program: tf_lab1_home_prices.py




## Run the Program
$ ssh ubuntu@<IP Address of Your VM>
$ docker run -it --rm -v $PWD:/tmp -w /tmp icr.io/ibmz/tensorflow:2.5.0 python ./tf_lab1_home_prices.py

  The output would look something like this:

  2022-03-08 19:47:05.090768: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:176] None of the MLIR Optimization Passes are enabled (registered 2)
  2022-03-08 19:47:05.091975: I tensorflow/core/platform/profile_utils/cpu_utils.cc:114] CPU Frequency: 10940500000 Hz
  
  
  
  
  Epoch 1/500
  1/1 [==============================] - 0s 195ms/step - loss: 2.2278
  Epoch 2/500
  1/1 [==============================] - 0s 994us/step - loss: 1.4779
  Epoch 3/500
  1/1 [==============================] - 0s 723us/step - loss: 0.9943
  .........
  .................
  .........................
  ...................................
  ............................................
  Epoch 496/500
  1/1 [==============================] - 0s 696us/step - loss: 3.5272e-04
  Epoch 497/500
  1/1 [==============================] - 0s 682us/step - loss: 3.4857e-04
  Epoch 498/500
  1/1 [==============================] - 0s 680us/step - loss: 3.4446e-04
  Epoch 499/500
  1/1 [==============================] - 0s 710us/step - loss: 3.4040e-04
  Epoch 500/500
  1/1 [==============================] - 0s 623us/step - loss: 3.3639e-04


  For x=7, the model predicted y=[[4.037854]]
  The price of the house is around $403,785.41



## Glossary
### What is Tensorflow
TensorFlow is an open-source end-to-end platform that enables developers to easily build and deploy ML powered applications.. It is a math library that can be used across a range of Machine Learning tasks but has a particular focus on training and scoring of deep neural networks. It also has an ecosystem of tools, libraries and community resources


### What is Numpy
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The ancestor of NumPy, Numeric, was originally created by Jim Hugunin with contributions from several other developers


### What is keras
Keras is an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library and focuses on being user-friendly, modular, and extensible. 




## Credits
- [Tensorflow Fundamentals YouTube Videos](https://www.youtube.com/playlist?list=PLOU2XLYxmsII9mzQ-Xxug4l2o04JBrkLV)
- [Tensorflow Image ported on Z - z Ecosystem Open Source Team](https://ibm.github.io/ibm-z-oss-hub/main/main.html)








