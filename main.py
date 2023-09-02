from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form.get('age')
    gender = request.form.get('gender')
    weather = request.form.get('weather')
    Place_change = request.form.get('Place_change')
    Time = request.form.get('Time(Hours)')



    input_query = np.array([[age, gender, weather, Place_change, Time]])

    result = model.predict(input_query)[0]
    result = int(result)
    return jsonify({'Suguest': result})

if __name__ == '__main__':
    app.run(debug=True)


