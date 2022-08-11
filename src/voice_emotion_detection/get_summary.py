
def getSummary(phone):
    import pyrebase
    import json
    config = {
        "apiKey": "AIzaSyDLCeQr8snT35fP6Un01QVhcS0VSfhZcjs",
        "authDomain": "smart-infotainment-system.firebaseapp.com",
        "databaseURL": "https://smart-infotainment-system-default-rtdb.firebaseio.com",
        "projectId": "smart-infotainment-system",
        "storageBucket": "smart-infotainment-system.appspot.com",
        "messagingSenderId": "477191060729",
        "appId": "1:477191060729:web:fb8d349dc6bef9a098b628",
        "measurementId": "G-Y8P0BFE6XQ"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    predictionList = db.child("Predictions").get()
    predicParamList = []

    # print(phone)
    for prediction in predictionList.each():
        test = prediction.val()
        if test["phone"] == phone: 
            predicParamList.append(prediction.val())     
    return predicParamList