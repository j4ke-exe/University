import os, uuid, time
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'a_default_secret_key')

orders_db = {}

pizza_menu = [
    {"id": 1, "name": "Classic Margherita", "price": 5.00, "image": "1.webp"},
    {"id": 2, "name": "Garden Vegetarian", "price": 6.00, "image": "2.webp"},
    {"id": 3, "name": "Spicy Pepperoni", "price": 6.25, "image": "3.webp"},
    {"id": 4, "name": "Tropical Hawaiian", "price": 6.70, "image": "4.webp"},
    {"id": 5, "name": "Ultimate Meat Feast", "price": 7.45, "image": "5.webp"},
    {"id": 6, "name": "Smokey BBQ Chicken", "price": 7.50, "image": "6.webp"},
    {"id": 7, "name": "Zesty Buffalo Chicken", "price": 8.25, "image": "7.webp"},
    {"id": 8, "name": "Vegan Delight Supreme", "price": 6.95, "image": "8.webp"},
]

class CheckoutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone', validators=[DataRequired(), Regexp('^\d+$', message="Phone number must be digits only"), Length(min=10, max=15)])
    submit = SubmitField('Place Order')

def calculate_order_total(order_items):
    total_cost = 0.0
    for item in order_items:
        pizza = next((pizza for pizza in pizza_menu if pizza['id'] == item['id']), None)
        if pizza:
            total_cost += pizza['price'] * item['quantity']
    return round(total_cost, 2)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu=pizza_menu)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = []
    form_data = request.form
    pizza_id = int(form_data['id'])
    quantity = int(form_data['quantity'])
    pizza = next((pizza for pizza in pizza_menu if pizza['id'] == pizza_id), None)
    
    if pizza:
        session['cart'].append({
            'id': pizza_id,
            'name': pizza['name'],
            'price': pizza['price'],
            'quantity': quantity
        })
        session.modified = True

    return redirect(url_for('menu'))

@app.route('/cart')
def cart():
    total_cost = calculate_order_total(session.get('cart', []))
    return render_template('cart.html', cart=session.get('cart', []), total_cost=total_cost)

@app.route('/update_item', methods=['POST'])
def update_item():
    item_id = int(request.form.get('item_id'))
    action = request.form.get('action')
    
    # Find the item in the cart
    item = next((item for item in session['cart'] if item['id'] == item_id), None)
    
    # If the item was found, then update the quantity or remove it
    if item:
        if action == 'increase':
            item['quantity'] += 1
        elif action == 'decrease':
            item['quantity'] -= 1
            # If the quantity is 0, then remove the item from the cart
            if item['quantity'] == 0:
                session['cart'].remove(item)
    else:
        flash('Item not found in cart.', 'error')

    session.modified = True
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    if form.validate_on_submit():
        timestamp = time.time()  # Current timestamp
        customer_info = {
            "name": form.name.data,
            "address": form.address.data,
            "email": form.email.data,
            "phone": form.phone.data
        }
        order_details = session.get('cart', [])
        order_id = str(uuid.uuid4())
        orders_db[order_id] = {
            "customer_info": customer_info,
            "order_details": order_details,
            "status": "Processing",
            "timestamp": timestamp  # Store order timestamp
        }
        
        session.pop('cart', None)  # Clear the shopping cart after placing the order
        
        flash('Your order has been placed successfully! Your order ID is {}'.format(order_id), 'success')
        return redirect(url_for('track_order', order_id=order_id))
    return render_template('checkout.html', form=form)

@app.route('/track_order', methods=['GET', 'POST'])
def track_order():
    order_id = request.args.get('order_id') or request.form.get('order_id')
    order = orders_db.get(order_id) if order_id else None
    if order:
        # Simulate calculating total cost and estimated delivery time
        order['total_cost'] = calculate_order_total(order['order_details'])
        order['estimated_delivery'] = "45 minutes after order placement"
        
        # Update status based on time elapsed (for demonstration)
        elapsed_time = time.time() - order["timestamp"]
        if elapsed_time > 60:
            order["status"] = "In Delivery"
        if elapsed_time > 120:
            order["status"] = "Delivered"
    else:
        flash('Order ID not found. Please check your input and try again.', 'error')
    
    return render_template('track_order.html', order=order, order_id=order_id)

if __name__ == '__main__':
    app.run(debug=True)