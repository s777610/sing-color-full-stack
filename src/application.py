import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecretkey'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.url_map.strict_slashes = False
db = SQLAlchemy(application)


@application.route('/')
def home():
    return render_template("index.html")


@application.route('/order', methods=['GET', 'POST'] )
def order():
    if request.method == 'POST':
        from models.order import Order
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        letters = request.form['letters']
        key_html = request.form['key']
        key = True if key_html == 'true' else False
        order_type = request.form['order_type']
        num_letter = len(letters)
        order = Order(name, email, phone, address)
        if order_type == 'single':
            order.single_letter_calc_price(num_letter, key)
        else:
            order.multi_letter_calc_price(num_letter, key)
        order.save_to_db()
        return render_template("checkout.html", order=order, key=os.environ['PUBLISHABLE_KEY'])
    return render_template("order.html")


@application.route('/charge/<string:email>', methods=['POST'])
def charge(email):
    if request.method == 'POST':
        from models.order import Order
        card = request.form['stripeToken'] # get the token from buyer form
        order = Order.find_by_email(email)
        success = order.charge_with_stripe(card)
        if success:
            # sending email to naked and buyer
            order.delete_from_db()
            return render_template('confirmation.html', amount=order.price)
        else:
            return render_template('confirmation.html', text="購買失敗")
    return redirect(url_for('home'))



if __name__ == "__main__":
    application.run(debug=True, port=4883)