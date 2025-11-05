from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
log = []
last_visit = None


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/log')
def view_log():
    global last_visit
    now = datetime.now()
    seconds_since_last = None
    if last_visit:
        seconds_since_last = (now - last_visit).total_seconds()
    last_visit = now

    entry = {
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'time': now.strftime("%Y-%m-%d %H:%M:%S"),
        'since_last': seconds_since_last
    }
    log.append(entry)
    return render_template('log.html', log=log)


if __name__ == '__main__':
    app.run(debug=True)
