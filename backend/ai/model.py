import tensorflow as tf
from collections import Counter
import cv2
import numpy

inception = tf.keras.applications.InceptionV3()
with open("ai/labels.txt", mode="r") as file:
    labels = list(map(lambda x: x.replace('\n', ''), file.readlines()))


def classify(image):
    image = image.reshape((-1, 299, 299, 3))
    image = tf.keras.applications.inception_v3.preprocess_input(image)
    predictions = inception.predict(image).flatten()

    return {labels[i]: float(predictions[i]) for i in range(1000)}


def prediction(image):
    image = cv2.imdecode(numpy.fromstring(image.file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image, (299, 299), 3)
    label = classify(image)
    k = Counter(label)
    high = k.most_common(1)

    return high[0]
