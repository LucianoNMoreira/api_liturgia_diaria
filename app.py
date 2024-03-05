from flask import Flask, jsonify
from flask_cors import CORS
from extractor.ExtractorService import ExtractorService

app = Flask(__name__)
CORS(app)

@app.route('/')
def homepage():
    liturgy = ExtractorService.getScrapy()

    response = {
        'objective': 'A API_LITURGIA_DIARIA visa disponibilizar via api as leituras para facilitar a criação de aplicações que almejam a evangelização.',
        'source':'Canção Nova',
        'today': liturgy
    }

    return jsonify(response)
