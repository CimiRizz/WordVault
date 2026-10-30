"""Voikko morphology endpoint; sends no image and retains no submitted text."""
from flask import Flask, request, jsonify, make_response
import libvoikko
import re

app = Flask(__name__)
voikko = libvoikko.Voikko('fi')
WORD = re.compile(r"^[^\W\d_]+(?:[’'\-][^\W\d_]+)*$", re.UNICODE)

@app.after_request
def cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Cache-Control'] = 'no-store'
    return resp

@app.get('/')
@app.get('/health')
def health():
    return jsonify(status='ok', service='WordVault Voikko')

@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze():
    if request.method == 'OPTIONS':
        return make_response('', 204)
    if request.content_length and request.content_length > 20000:
        return jsonify(error='Liian suuri pyyntö'), 413
    payload = request.get_json(silent=True) or {}
    words = payload.get('words', [])
    if not isinstance(words, list) or len(words) > 250:
        return jsonify(error='Sanoja saa olla enintään 250'), 400
    results = []
    for word in words:
        if not isinstance(word, str) or len(word) > 45 or not WORD.fullmatch(word):
            results.append({'word': str(word)[:45], 'lemmas': []})
            continue
        try:
            analyses = voikko.analyze(word.lower())
            lemmas = []
            for item in analyses:
                base = item.get('BASEFORM', '').strip()
                if base and base not in lemmas:
                    lemmas.append(base)
            results.append({'word': word, 'lemmas': lemmas[:8]})
        except Exception:
            results.append({'word': word, 'lemmas': []})
    return jsonify(results=results)
