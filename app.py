from flask import Flask, request, render_template, redirect  # <-- add redirect import
from scraper import get_amazon_product_details
from database import create_tables, insert_product, insert_price
from apscheduler.schedulers.background import BackgroundScheduler
import time
import sqlite3

app = Flask(__name__)
create_tables()

# In-memory list of product URLs (temporary; later we’ll use DB)
tracked_products = [
    "https://www.amazon.in/dp/B0CV7KZLL4/"
]

def scheduled_scrape():
    print("🔁 Running scheduled scrape...")

    for url in tracked_products:
        data = get_amazon_product_details(url)
        if "error" in data:
            print(f"Error scraping {url}: {data['error']}")
            continue

        product_id = insert_product(url, data["title"], data["image"])
        insert_price(product_id, data["price"])
        print(f"✔️ Scraped and stored: {data['title']} - ₹{data['price']}")

# Start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_scrape, 'interval', minutes=60)

def track_all_products():
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute("SELECT id, url FROM products")
    rows = c.fetchall()
    for product_id, url in rows:
        data = get_amazon_product_details(url)
        insert_price(product_id, data["price"])
    conn.close()

# Add this job to the scheduler to run every 12 hours
scheduler.add_job(func=track_all_products, trigger="interval", hours=12)

scheduler.start()

@app.route("/")
def index():
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute("SELECT id, title, image FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

@app.route("/track", methods=["POST"])
def track():
    url = request.form["url"]
    tracked_products.append(url)
    return f"Tracking started for: {url}"

@app.route("/add", methods=["POST"])
def add_product():
    url = request.form["url"]
    data = get_amazon_product_details(url)
    product_id = insert_product(url, data["title"], data["image"])
    insert_price(product_id, data["price"])
    return redirect("/")

@app.route("/history/<int:product_id>")
def get_price_history(product_id):
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute("SELECT price, timestamp FROM prices WHERE product_id = ? ORDER BY timestamp", (product_id,))
    rows = c.fetchall()
    conn.close()

    history = [{"price": row[0], "timestamp": row[1]} for row in rows]
    return {"history": history}

if __name__ == "__main__":
    app.run(debug=True)

