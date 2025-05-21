import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_amazon_product_details(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return {"error": f"Failed to fetch. Status code: {response.status_code}"}
        
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find(id="productTitle")
        title = title.get_text().strip() if title else "N/A"

        price_span = soup.find("span", class_="a-offscreen")
        price = price_span.get_text().strip().replace("₹", "").replace(",", "") if price_span else "N/A"

        image_tag = soup.find("img", id="landingImage")
        image_url = image_tag["src"] if image_tag else ""

        return {
            "title": title,
            "price": float(price) if price != "N/A" else None,
            "image": image_url
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    test_url = "https://www.amazon.in/dp/B0CV7KZLL4/"
    data = get_amazon_product_details(test_url)
    print(data)
