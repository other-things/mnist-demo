import tensorflow as tf
from PIL import Image
import numpy as np


image_size = (28, 28)


# load model
model = tf.keras.models.load_model('tensorflow_model/mnist_ann_model.h5')

graph = tf.get_default_graph()


def predict_image(test_image):
	# load test image, resize and normalize it
	img = Image.open(test_image)
	img.thumbnail(image_size, Image.ANTIALIAS)
	img = img.convert('L')
	image_data = np.asarray(img, dtype=np.float32)
	image_data = image_data / 255
	image_data_test = image_data.reshape((1, image_size[0], image_size[1]))

	global graph
	with graph.as_default():

		# predit the output 
		classes = model.predict(image_data_test)
		image_pred = str(np.argmax(classes))
		confidence = round(classes[0][np.argmax(classes)], 2) * 100
		print(image_pred, confidence)
	
		return image_pred, confidence


# test with dummy image
if __name__ == '__main__':
	predict_image('tensorflow_model/seven.png')