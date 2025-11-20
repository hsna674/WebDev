from flask import Flask, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'


def create_or_retrieve():
    if 'user_state' not in session:
        session['user_state'] = {'visits': 0, 'cars': 0, 'cows': 0}
    return session['user_state']


@app.route('/')
def home():
    user_state = create_or_retrieve()
    user_state['visits'] += 1
    session['user_state'] = user_state
    return render_template('index.html', user_data=user_state)


@app.route('/buycar')
def buy_car():
    user_state = create_or_retrieve()
    user_state['cars'] += 1
    session['user_state'] = user_state
    return redirect(url_for('home'))


@app.route('/buycow')
def buy_cow():
    user_state = create_or_retrieve()
    user_state['cows'] += 1
    session['user_state'] = user_state
    return redirect(url_for('home'))


@app.route('/clearinventory')
def clear_inventory():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
