from flask import Flask, jsonify
import re

app = Flask(__name__)

word_list = open('enable1.txt').read().splitlines()

@app.route('/<letters>')
def filter_words(letters):
    pattern = r'^[^' + re.escape(letters) + r']{5}$'

    filtered_words = [word for word in word_list if re.match(pattern, word)]

    return jsonify(filtered_words)

if __name__ == '__main__':
    app.run(debug=True)
