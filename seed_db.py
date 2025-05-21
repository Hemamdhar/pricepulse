from scraper import get_amazon_product_details
from database import create_tables, insert_product, insert_price

url = "https://www.amazon.in/dp/B0CV7KZLL4/"

# Step 1: scrape data
data = get_amazon_product_details(url)
print("Scraped Data:", data)

# Step 2: store in DB
create_tables()
product_id = insert_product(url, data["title"], data["image"])
insert_price(product_id, data["price"])

print("✔️ Product saved with ID:", product_id)
