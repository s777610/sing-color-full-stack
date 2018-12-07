import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import Config



application = Flask(__name__)
application.config.from_object(Config)
application.url_map.strict_slashes = False
db = SQLAlchemy(application)
mail = Mail(application)


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
        key_holder = request.form['key_holder']
        item_type = request.form['order_type']
        order = Order(name, email, phone, address, letters, key_holder, item_type)
        if item_type == 'single':
            order.single_letter_calc_price()
        else:
            order.multi_letter_calc_price()
        try:
            order.save_to_db() # we are tring to store this, even this already exisit
        except:
            old_order = Order.find_by_email(email)
            old_order.delete_from_db()
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
            order.email_to_seller()
            order.email_to_buyer()
            order.delete_from_db()
            return render_template('confirmation.html', amount=order.price)
        else:
            return render_template('confirmation.html', text="購買失敗")
    return redirect(url_for('home'))



if __name__ == "__main__":
    application.run(debug=True, port=4883)