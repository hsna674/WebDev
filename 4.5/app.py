from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getwords')
def get_words():
    green = request.args.get('green', '_____')
    yellow = request.args.get('yellow', '')
    grey = request.args.get('grey', '')

    green_list = list(green)
    yellow_list = yellow.split(',') if yellow else []
    grey_list = grey.split(',') if grey else []

    return jsonify({
        "green": green_list,
        "yellow": yellow_list,
        "grey": grey_list
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
