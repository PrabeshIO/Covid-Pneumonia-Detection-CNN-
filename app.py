from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model("Bestmodel")

def predict_label(img_path):
	img = image.load_img(img_path,target_size=(150,150))
	images = image.img_to_array(img) 
	images = np.expand_dims(images,axis=0)
	prediction = model.predict(images)
	if prediction == 0:
		return('Sorry! Covid pneumonia detected') 
	else: 
		return('Your Chest Xray is normal') 

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']
		img_path = "static/" + img.filename	
		img.save(img_path)
		p = predict_label(img_path)
	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	app.run(debug = True)