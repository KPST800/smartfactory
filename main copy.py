from flask import Flask, jsonify, request
import json


    
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def basic():
    param1 = request.args.get('power', "-1")
    param2 = request.args.get('gyro', "-1")
    param3 = request.args.get('audio', "-1")

    print(param1)
    print(param1.split(','))
    print(param2)
    print(param2.split(','))
    print(param3)
    print(param3.split(','))
    return_str = 'power: '+param1+', gyro: '+param2+', audio: '+param3
    print(return_str)

    return "OK"

if __name__ == "__main__":
    app.run( host='0.0.0.0',threaded=True)
    
    
