from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/roll/<int:num_sides>')
@app.route('/roll/<int:num_sides>/<int:num_dice>')
def roll(num_sides, num_dice=1):
    if num_sides <= 0 or num_dice <= 0:
        return render_template('invalid.html')
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return render_template('roll.html', rolls=rolls, sides=num_sides, dice=num_dice)


@app.errorhandler(404)
def not_found(e):
    return render_template('invalid.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
