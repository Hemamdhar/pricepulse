# 🛒 PricePulse

**Smart Price Tracking and Product Comparison Tool (Python Version)**

PricePulse is a Python-based web application that tracks product prices in real time, displays historical trends, and compares prices across different e-commerce platforms. It helps users save money by buying at the right time and from the best source.

## 🚀 Features

- 🔍 **Real-Time Price Tracking** – Track live product prices from Amazon, Flipkart, and other e-commerce websites.
- 📈 **Price History Visualization** – View historical price trends using graphs.
- 🔔 **Smart Alerts** – Receive alerts (via email or Telegram) when a product’s price drops below your target.
- ⚖️ **Product Comparison** – Compare the same product across multiple platforms.
- ❤️ **Wishlist Tracking** – Maintain and monitor a list of products.

## 🛠️ Tech Stack

- **Backend**: Python (Flask / Django)
- **Web Scraping**: BeautifulSoup, Requests, Selenium (if needed)
- **Database**: SQLite / MongoDB
- **Graphing**: Matplotlib / Plotly
- **Notifications**: smtplib (for Email) or Telegram Bot API
- **Frontend**: HTML, CSS, JavaScript (optional)

## 🧠 How It Works

1. User enters a product URL.
2. Python scraper fetches product data (price, name, etc.).
3. Data is saved in the database with timestamps.
4. Graphs show how the price has changed over time.
5. If the current price is below user-defined threshold → alert is sent.

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/pricepulse.git
cd pricepulse

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
