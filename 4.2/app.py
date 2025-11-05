from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def root_page():
    return render_template('index.html')


@app.route('/get_schedule_from_ion/<date>')
def get_schedule_from_ion(date):
    try:
        url = f"https://ion.tjhsst.edu/api/schedule/{date}?format=json"
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'error': 'Invalid date or server error'}), 400
        return response.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
