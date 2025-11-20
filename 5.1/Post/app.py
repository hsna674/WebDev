from flask import Flask, render_template, request

app = Flask(__name__)

meals = {"Dinner": 12, "Lunch": 8, "Breakfast": 6}
drinks = {"Water": 0, "Soda": 2, "Coffee": 3}

orders = []
total_sales = 0


@app.route('/')
def form():
    return render_template('form.html', meals=meals, drinks=drinks)


@app.route('/result', methods=['POST'])
def result():
    meal = request.form.get('meal')
    drink = request.form.get('drink')
    qty = int(request.form.get('qty', 1))
    senior = request.form.get('senior')
    special = request.form.get('special', '')
    price = meals[meal] + drinks[drink]
    total = price * qty
    if senior == 'on':
        total *= 0.9
    global total_sales
    total_sales += total
    orders.append(1)
    return render_template('result.html', meal=meal, drink=drink, qty=qty, total=round(total, 2), special=special)


@app.route('/manager')
def manager():
    return render_template('manager.html', total_orders=len(orders), total_sales=round(total_sales, 2))


if __name__ == '__main__':
    app.run(debug=True)
