from flask import Flask, render_template

app = Flask(__name__)
page_visits = 0


@app.route('/')
def index():
    global page_visits
    page_visits += 1
    return render_template('index.html', count=page_visits)


if __name__ == '__main__':
    app.run(debug=True)
