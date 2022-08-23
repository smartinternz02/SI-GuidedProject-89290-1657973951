import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.compat.v1.get_default_graph()
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
model = load_model("C:/Users/gouth/Desktop/iceberg.h5")

@app.route('/')
def index():
    return render_template('index.html', methods= ['GET'])

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == "POST":
        f = request.files["image"]
        
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,secure_filename(f.filename))
        print("upload folder is ", filepath)
        f.save(filepath)
        
        x = tf.keras.utils.load_img(filepath,target_size = (75,75))
       # print(filepath)
      #  x = tf.keras.utils.load_img(img)
        x = np.expand_dims(x,axis =0)
        
        #with graph.as_default():
        #preds = model.predict_classes(x)
        preds = np.argmax(model.predict(x))
            
            
        pred = int(preds)
        print("HERE LIes \n" ,pred)
        if pred:
            text ="Beware!! Iceberg ahead."
        else:
            text = "You are safe!! It's a Ship"
    print(text)    
    return text


    
if __name__ == '__main__':
    app.run()
        
        
        
    
    
    