import tensorflow as tf
import cv2
import numpy as np


class Model:
    model = None


    # Preds_Labels
    preds_dict = {
        0:"CNV",
        1:"DME",
        2:"DRUSEN",
        3:"Glaucoma_Negative",
        4:"Glaucoma_Positive",
        5:"MildDemented",
        6:"ModerateDemented",
        7:"NORMAL",
        8:"NonDemented",
        9:"VeryMildDemented"}

    #Preds_Inverse
    preds_inverse_dict = {'CNV': 0, 'DME': 1, 'DRUSEN': 2, 'Glaucoma_Negative': 3, 'Glaucoma_Positive': 4, 'MildDemented': 5, 'ModerateDemented': 6, 'NORMAL': 7, 'NonDemented': 8, 'VeryMildDemented': 9}

    #Subcat Mapping
    subcats = {
        "Glaucoma":
        [3,4],
        "Diabetes":
        [0,1,2,7],
        "Alzheimers":
        [5,6,8,9]
    }

    def __init__(self,model_dir):
        self.model = tf.keras.models.load_model(model_dir)

    def predict_image(self,img_dir,subcat="Glaucoma"):
        # print("Its Working")
        img = cv2.imread(img_dir)
        img = cv2.resize(img,(150,150))
        img = np.reshape(img,(1,150,150,3))

        preds = self.model.predict(img)
        preds = list(tf.nn.softmax(preds).numpy()[0])

        max_pred = preds.index(max([preds[inx] for inx in self.subcats[subcat]]))
        
        # print(self.preds_dict[max_pred])
        return self.preds_dict[max_pred]

        # for categories in self.subcats[subcat]


        # print(self.model.predict(img))

# if __name__ == "__main__":
#     model = Model("./static/model/model.h5")
#     model.predict_image()