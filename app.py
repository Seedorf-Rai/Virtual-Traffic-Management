from flask import Flask ,request, render_template
from datetime import datetime
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
with open("random_forest_model.pkl",'rb') as f:
    loaded_model = pickle.load(f)

print(loaded_model.predict("4/22/2024 10:30"))

@app.route("/forecast",methods=["GET", "POST"])
def products():
    if request.method == 'GET':
        return render_template('forecast.html')
    elif request.method == 'POST':
        date_string = request.form['date']
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        date = date_object.strftime("%d/%m/%Y")
        time = request.form['time']
        print('Time',time)
        print('Date',date)
    return render_template('forecast.html')

    # try:
    #     predicted_traffic =

@app.route("/live")
def live():
    return render_template('Live.html')

@app.route("/route")
def route():
    return render_template('route.html')

if __name__ == '__main__':
    app.run(debug=True , port=8080)