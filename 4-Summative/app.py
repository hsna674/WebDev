from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

word_list = [w.lower() for w in open('enable1.txt').read().splitlines() if len(w) == 5]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getwords')
def getwords():
    green = request.args.get('green', '_____')
    yellow = request.args.get('yellow', '')
    grey = request.args.get('grey', '')

    pattern = '^'
    for ch in green:
        pattern += ch if ch.isalpha() else '[a-z]'
    pattern += '$'

    filtered = [w for w in word_list if re.match(pattern, w)]

    if grey:
        for g in grey.split(','):
            filtered = [w for w in filtered if g not in w]

    if yellow:
        for y in yellow.split(','):
            filtered = [w for w in filtered if y in w]

    return jsonify({"valid_words": filtered})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
