from flask import Flask, request, render_template, jsonify
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
from zodiac_signs import *

app = Flask(__name__)

cred = credentials.Certificate("tallerbasedatos-db65c-firebase-adminsdk-fbsvc-b0af1ce74e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    day = int(request.form['day'])
    month = int(request.form['month'])
    zodiac_sign = get_zodiac_sign(day, month)
    birthday = {
        'Fecha de nacimiento': {
            'Día': day, 
            'Mes': month
        }
    }
    doc_ref = db.collection('Fecha de nacimiento').document()
    doc_ref.set(birthday)
    response = {
        'message': f'Naciste el {day}/{month} y tu signo zodiacal es {zodiac_sign}.',
        'document_id': doc_ref.id
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)