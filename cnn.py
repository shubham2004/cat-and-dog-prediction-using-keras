# i use try and except to skip the faulty image in dataset
# Importing Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
# Initialising the CNN
# their are two types of CNN in here i use sequential
classifier = Sequential()
# creating Convolution matrix and  performing convolution
#here 32 is conv layer filter size and 3,3 is conv matrix use for convolution and input shape is 64*64*3 here 3 is rgb layers of a single image
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
# Max Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# again doing convolution on the first layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
#again applying max pooling 
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Flattening
# this layer convert 2D image or lets say vector into 1D vector
classifier.add(Flatten())
# Full connection
# this step is same as neural network the last flatterned layer is used as input to neural network 
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator
# this is data generator
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
try:
    training_set = train_datagen.flow_from_directory('dataset/training_set',
    target_size = (64, 64),
    batch_size = 32,
    class_mode = 'binary')
except Exception as e:
        print(e)
# test set generator
try:
    test_set = test_datagen.flow_from_directory('dataset/test_set',
    target_size = (64, 64),
    batch_size = 32,
    class_mode = 'binary')
except Exception as e:
        print(e)
# training the classifier
try:
    classifier.fit_generator(training_set,
    steps_per_epoch = 8000,
    epochs = 25,
    validation_data = test_set,
    validation_steps = 2000)
except Exception as e:
        print(e)
# Making new predictions
import numpy as np
from keras.preprocessing import image
#taking new image to predict
test_image = image.load_img('dataset/8dog.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
print(result)
#extracting result
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'

print(prediction)
