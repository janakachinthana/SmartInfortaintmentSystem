from flask import Flask, render_template, request, jsonify
from src.voice_emotion_detection.get_user_prediction import getUserPrediction
from src.voice_emotion_detection.predict_results import checkAthentification
from src.voice_emotion_detection.get_summary import getSummary

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>WELCOME SMART INFORTAITEMENT SYSTEM</h1>"
 
@app.route('/voice-emotion-detection/login', methods=["GET","POST"])
def users():
    if request.method == "GET":
       
        return render_template('index.html')
    elif request.method == "POST":

         return "This is get request!"

    return "Something went wrong"

@app.route('/voice-emotion-detection/summary', methods=["GET","POST"])
def summary():
    if request.method == "GET":

        return "HI"

    elif request.method == "POST":

        output = request.form.to_dict()
        phone = output["phone"]
        result = getSummary(phone)

        # if result == "True":
        #     userList = getUserPrediction()
        #     return render_template('userlist.html',userList = userList)

        # if result == "False":
        #      return render_template('login.html', username = "Invalid Credintials!")
             
    return render_template('predictionList.html',predictionList = result)  


@app.route('/voice-emotion-detection/userlist', methods=["GET","POST"])
def userlist():
    if request.method == "GET":

        return "HI"

    elif request.method == "POST":

        output = request.form.to_dict()
        username = output["username"]
        password = output["password"]
        result = checkAthentification(username, password)

        if result == "True":
            userList = getUserPrediction()
            return render_template('userlist.html',userList = userList)

        if result == "False":
             return render_template('login.html', username = "Invalid Credintials!")
             
    return "Something went wrong"   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

