#flask utils
from flask import Flask,render_template,request,redirect,url_for
import os
#keras
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
#define flask
app = Flask(__name__)

model = tf.keras.models.load_model('covidModel.h5')
from keras.applications.vgg16 import preprocess_input

def model_predict(img_path,model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    New_pred = np.argmax(classes, axis=1)
    if New_pred==[1]:
        return "Normal"
    else:
        return "Corona"

@app.route('/',methods=["GET"])
def hello_world():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def upload():
    if request.method=="POST": 
        uploaded_file=request.files["file"]
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(basepath,"uploads",uploaded_file.filename)
        print(file_path)
        uploaded_file.save(file_path)
        result=model_predict(file_path,model)
        return result

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)

