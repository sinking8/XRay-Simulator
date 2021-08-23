import tensorflow as tf
import cv2
import numpy as np


class Model:
    model = None
    def __init__(self,model_dir):
        self.model = tf.keras.models.load_model(model_dir)

    def predict_image(self):
        print("Its Working")
        img = cv2.imread("./static/images/test_img.jpeg")
        img = cv2.resize(img,(150,150))
        img = np.reshape(img,(1,150,150,3))
        print(self.model.predict(img))

# if __name__ == "__main__":
#     model = Model("./static/model/model.h5")
#     model.predict_image()