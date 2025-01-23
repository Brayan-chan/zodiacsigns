from flask import Flask, request, render_template, jsonify
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
from zodiac_signs import *

app = Flask(__name__)

cred = credentials.Certificate("autenticate-8786c-firebase-adminsdk-88any-8c83f948c4.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        day = request.form['day']
        month = request.form['month'].lower()

        months = {
            'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
            'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
        }

        try:
            day = int(day)
            if day <= 0 or day > 31:
                raise ValueError("Día inválido")
        except ValueError:
            raise ValueError("Día inválido")

        try:
            if month.isdigit():
                month = int(month)
                if month <= 0 or month > 12:
                    raise ValueError("Mes inválido")
            else:
                month = months[month]
        except KeyError:
            raise ValueError("Mes inválido")

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
            'document_id': doc_ref.id,
            'status': 'success'
        }
    except Exception as e:
        response = {
            'message': str(e),
            'status': 'error'
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)