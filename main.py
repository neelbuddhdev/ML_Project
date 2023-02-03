from flask import Flask, request, jsonify, render_template
from predict import recommend_crop
from config import images

crop_recommender_app = Flask(__name__)

@crop_recommender_app.route("/")
@crop_recommender_app.route("/home")
def home():
    return render_template("index.html", url="https://img.freepik.com/free-vector/welcome-neon-sign-vector_53876-76088.jpg?w=2000", P='', N='', K='', temperature='', humidity='', ph='', rainfall='')

@crop_recommender_app.route('/predict',methods=['POST'])
def predict():
    N = request.form.get('N')
    P = request.form.get('P')
    K = request.form.get('K')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    rainfall = request.form.get('rainfall')
    ph = request.form.get('ph')
    crop_name = recommend_crop([[P, N, K, temperature, humidity, ph, rainfall]])
    return render_template("result.html", url=images[crop_name], crop_name=crop_name.capitalize())


if __name__ == '__main__':
    crop_recommender_app.run()