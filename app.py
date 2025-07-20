from flask import Flask,jsonify,request,render_template
import joblib

app = Flask(__name__)
model = joblib.load('lr.house_model.joblib')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    MedInc = request.args.get('MedInc', type=float)
    HouseAge = request.args.get('HouseAge', type=float)
    Population = request.args.get('Population', type=float)
    AvgOccup = request.args.get('AvgOccup', type=float)
    Latitude = request.args.get('Latitude', type=float)
    AveRooms = request.args.get('AveRooms', type=float)
    
    input_data = [MedInc, HouseAge, Population, AvgOccup, Latitude, AveRooms]
    result = model.predict([input_data])
    return jsonify(f'The predicted house price is: {result[0]:.2f}')

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/')
# def home():
#     return ('Welcome to House Prediction')

# @app.route('/prediction')
# def predction():
#     MedInc = request.args.get('MedInc',type=int)
#     HouseAge = request.args.get('HouseAge',type=int)
#     Population = request.args.get('Population',type=int)
#     AvgOccup = request.args.get('AvgOccup',type=int)
#     Latitude = request.args.get('Latitude',type=int)
#     AveRooms = request.args.get('AveRooms',type=int)
    
#     input = [MedInc,HouseAge,Population,AvgOccup,Latitude,AveRooms]
#     result = model.predict([input])
#     output = jsonify(f'The Prediction is :{result}')
