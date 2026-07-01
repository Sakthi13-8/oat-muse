from flask import Flask, render_template, request, jsonify, session, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sakthii@138",
    database="oatmuse"
)

cursor = db.cursor()

# SECRET KEY (required for session/cart)
app.secret_key = "oatmuse_secret_key"


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# PRODUCTS API (15 PRODUCTS)
# =========================
@app.route("/api/products")
def products():
    product_list = [
        {"id": 1, "name": "Oat Muse Hydrating Face Serum", "price": 499, "image": "serum.png"},
        {"id": 2, "name": "Oat Muse Vitamin C Brightening Serum", "price": 549, "image": "vitamin_c_serum.png"},
        {"id": 3, "name": "Oat Muse Barrier Repair Cream", "price": 599, "image": "barrier_cream.png"},
        {"id": 4, "name": "Oat Muse Daily Moisturizer", "price": 399, "image": "moisturizer.png"},
        {"id": 5, "name": "Oat Muse Under Eye Repair Cream", "price": 399, "image": "eyecream.png"},
        {"id": 6, "name": "Oat Muse Cooling Eye Gel", "price": 429, "image": "eye_gel.png"},
        {"id": 7, "name": "Oat Muse Nourishing Lip Balm", "price": 199, "image": "lip_balm.png"},
        {"id": 8, "name": "Oat Muse Lip Repair Mask", "price": 249, "image": "lip_mask.png"},
        {"id": 9, "name": "Oat Muse Glow Facial Oil", "price": 699, "image": "facial_oil.png"},
        {"id": 10, "name": "Oat Muse Gentle Cleanser", "price": 349, "image": "cleanser.png"},
        {"id": 11, "name": "Oat Muse Night Repair Cream", "price": 649, "image": "night_cream.png"},
        {"id": 12, "name": "Oat Muse Oat & Honey Face Cream", "price": 599, "image": "oat_honey_cream.png"},
        {"id": 13, "name": "Oat Muse Hydrating Mist", "price": 299, "image": "mist.png"},
        {"id": 14, "name": "Oat Muse Milk Serum", "price": 599, "image": "recovery_serum.png"},
        {"id": 15, "name": "Oat Muse Complete Skincare Collection", "price": 2499, "image": "collection.png"}
    ]

    return jsonify(product_list)


# =========================
# CONTACT FORM
# =========================
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("first-name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("New message:", name, email, message)

    return "Message sent successfully!"


# =========================
# ADD TO CART
# =========================
@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    product = request.json

    print("Received Product:", product)   # <-- Add this line

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(product)
    session.modified = True

    print("Current Cart:", session["cart"])   # <-- Add this line

    return jsonify({
        "message": "Added to cart",
        "cart": session["cart"]
    })
# =========================
# CART PAGE
# =========================
@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)

    return render_template("cart.html", cart=cart_items, total=total)

@app.route("/checkout")
def checkout():
    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)

    return render_template(
        "checkout.html",
        cart=cart_items,
        total=total
    )
@app.route("/place-order", methods=["POST"])
def place_order():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]

    cart_items = session.get("cart", [])

    total = sum(item["price"] for item in cart_items)

    cursor.execute("""
        INSERT INTO orders
        (customer_name, email, phone, address, total)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, email, phone, address, total))

    db.commit()

    print("========== NEW ORDER ==========")
    print("Customer:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Address:", address)
    print("Products:", cart_items)
    print("Total:", total)
    print("===============================")

    session["cart"] = []

    return render_template(
        "success.html",
        name=name,
        total=total
    )
# =========================
# REMOVE FROM CART
# =========================
@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():
    name = request.form.get("name")

    cart = session.get("cart", [])

    cart = [item for item in cart if item["name"] != name]

    session["cart"] = cart
    session.modified = True

    return redirect("/cart")

@app.route("/admin/orders")
def view_orders():
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    return render_template("orders.html", orders=orders)

# =========================
# START SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)