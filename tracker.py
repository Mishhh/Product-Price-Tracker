import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# Scrape.do API setup
API_TOKEN = "a9745136af2d4217a6b984674246d76b6602464fc32"
product_url = "https://www.bigbasket.com/pd/10000027/fresho-banana-robusta-500-g/?nc=smart_basket"
api_url = f"https://api.scrape.do?token={API_TOKEN}&url={product_url}"

# Send request via Scrape.do
response = requests.get(api_url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract product name and price
try:
    product_name = soup.find("h1", class_="Description___StyledH-sc-82a36a-2").get_text(strip=True)
    price_tag = soup.find("td", class_="Description___StyledTd-sc-82a36a-4")
    price = price_tag.get_text(strip=True) if price_tag else None

    if not price:
        raise ValueError("Price not found!")

    print(f"✅ Product: {product_name}")
    print(f"💰 Price: {price}")

    # Save to CSV
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = {"Timestamp": now, "Product": product_name, "Price": price}
    filename = "banana_price_history.csv"

    if os.path.exists(filename):
        df = pd.read_csv(filename)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(filename, index=False)
    print("📦 Price tracked and stored successfully!")

except Exception as e:
    print("❌ Error during scraping:", e)
