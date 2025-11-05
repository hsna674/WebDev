from flask import Flask, jsonify, render_template

app = Flask(__name__)

upvotes = 0
downvotes = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upvote')
def upvote():
    global upvotes
    upvotes += 1
    return jsonify({'upvotes': upvotes, 'downvotes': downvotes})


@app.route('/downvote')
def downvote():
    global downvotes
    downvotes += 1
    return jsonify({'upvotes': upvotes, 'downvotes': downvotes})


@app.route('/counts')
def counts():
    return jsonify({'upvotes': upvotes, 'downvotes': downvotes})


if __name__ == '__main__':
    app.run(debug=True)
