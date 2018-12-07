import os
import stripe
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Message

from application import db
from application import mail


SINGLE_LETTER_PRICE = 180
MULTI_LETTER_PRICE = 200
BASE_PRICE = 20
KEY_PRICE = 19

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, name, email, phone, address, price=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.price = price
        

    def single_letter_calc_price(self, num_letter, key):
        price = 0
        if key:
            price = price + KEY_PRICE
        price = price + num_letter * SINGLE_LETTER_PRICE
        if num_letter > 5:
            price = int(price * 0.9)
        self.price = price
        return price

    def multi_letter_calc_price(self, num_letter, key):
        price = MULTI_LETTER_PRICE * 2 + BASE_PRICE
        num = num_letter - 2
        if key:
            price = price + KEY_PRICE
        if num == 0: # if just 2 letter
            self.price = price
            return price
        price = price + num * MULTI_LETTER_PRICE
        self.price = price
        return price

    def charge_with_stripe(self, card):
        try:
            stripe.api_key = os.environ['SECRET_KEY']
            stripe.Charge.create(
                amount=self.price,
                currency='usd',
                card=card, # get the token from buyer form
                description='Stripe Flask')
            return True
        except:
            return False

    def email_to_seller(self):
        # recipients=["2018singcolor@gmail.com"]
        msg = Message(f'訂單, {self.email}, {self.name}',
                sender='noreply@demo.com',
                recipients=["2018singcolor@gmail.com"])  
        msg.body = f""" 
        買家資料： 
        姓名：{self.name}
        Email：{self.email}
        電話：{self.phone}
        郵寄地址：{self.address}
        價錢：{self.price}
        """
        mail.send(msg)

    def email_to_buyer(self):
        msg = Message(f'Sing Color 認證函',
                sender='noreply@demo.com',
                recipients=[f"{self.email}"])  
        msg.body = f""" 
        姓名：{self.name}
        Email：{self.email}
        電話：{self.phone}
        地址：{self.address}
        已付款：{self.price}

        
        客服電話：0937255052
        客服信箱：2018singcolor@gmail.com
        """
        mail.send(msg)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

# create table after this ORM defined
db.create_all()