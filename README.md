🍯 Product Price Tracker

Track and visualize price changes of any product from an e-commerce website. This tool can help you monitor fluctuating prices over time.

In this implementation, we track the price of Fresho Banana Robusta (500g) from BigBasket India.

🎓 Features

📈 Tracks price of a specific product over time

⏰ Can be scheduled to run daily using Cron (Windows Task Scheduler supported)

✨ Clean CSV logs for historical price analysis

📊 Visualizations possible using matplotlib / pandas

🔧 Configurable to track any product from any e-commerce site

⚙️ Technologies

Python 3.10+

Selenium (for JavaScript-rendered content)

BeautifulSoup (HTML parsing)

pandas (data processing)

ChromeDriver (headless browser automation)

⚖️ Setup Instructions

# 1. Clone the repo
$ git clone https://github.com/yourusername/product-price-tracker.git
$ cd product-price-tracker

# 2. Create a virtual environment (optional but recommended)
$ python -m venv .venv
$ .venv\Scripts\activate   # On Windows

# 3. Install dependencies
$ pip install -r requirements.txt

📝 Usage

tracker.py

This script will:

Open the product page using Selenium

Scrape the product name and price

Store it with a timestamp in price_history.csv

⏰ Scheduler Setup (Windows)

To run this script daily:

Open Task Scheduler on Windows

Click Create Basic Task

Set your schedule (e.g., Daily)

For Action, choose Start a program and browse to:

Program/script: python
Add arguments: path\to\tracker.py
Start in: path\to\your\project

📊 Output Example

Timestamp,Product,Price
2025-07-12 16:30:00,Fresho Banana Robusta (500g),29.00
2025-07-13 16:30:00,Fresho Banana Robusta (500g),28.00

🔄 Customizing for Another Product

To track a different product:

Replace the url in tracker.py with your product page URL

Update the HTML class selectors accordingly (use browser dev tools)

💡 Future Work

Multi-product tracking

Email notifications on price drop

Dashboard to visualize trends

Integration with databases like SQLite or PostgreSQL
