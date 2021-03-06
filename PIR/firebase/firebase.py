import pyrebase
from time import time

config = {
    "apiKey": "AIzaSyALG_2SdJS3GN1Ibpj_LGSrbmjXjJjrlvQ",
    "authDomain": "household-iot.firebaseapp.com",
    "databaseURL": "https://household-iot.firebaseio.com",
    "projectId": "household-iot",
    "storageBucket": "household-iot.appspot.com",
    "messagingSenderId": "1062863439327"
}

def firebase_init(config):
    return pyrebase.initialize_app(config)

def add_image_record(firebase, img_url):
    db = firebase.database()
    record = {
        "timestamp": time(),
        "url": img_url,
        "label": "PIR Event"
    }
    db.child("snapshots").push(record)

def save_image_to_bucket(firebase, img):
    storage = firebase.storage()
    # as admin
    node = "images/" + img
    storage.child(node).put(img)
    return storage.child(node).get_url(None)
