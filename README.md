# 🧺 Product Price Tracker

Track and visualize price changes of any product from an e-commerce website.  
💡 Stay informed and make smarter buying decisions using real-time and historical price data.

> **Example:** This implementation monitors the price of **Fresho Banana Robusta (500g)** from **BigBasket India**.

---

## 📌 Features

- 📈 **Track product prices over time**  
- ⏰ **Schedule automatic runs** (via **Windows Task Scheduler** or Cron)  
- 📂 **Store historical prices** in clean CSV format  
- 📊 **Visualize trends** using **Matplotlib** / **Pandas**  
- 🔧 **Easily configurable** to track prices from **any product or site**  

---

## 🧰 Technologies Used

| Tool/Library       | Purpose                                 |
|--------------------|-----------------------------------------|
| `Python 3.10+`      | Core language                          |
| `Selenium`          | To scrape JavaScript-rendered content  |
| `BeautifulSoup`     | Parse and extract HTML content         |
| `Pandas`            | Store and manage price data            |
| `Matplotlib`        | Visualization of price trends          |
| `Windows Scheduler` | Automate daily tracking                |


## 📅 Schedule Cron Job (Windows)

To schedule daily execution:

1. Open **Task Scheduler**
2. Create new task → set **trigger** (daily)
3. In **Action** tab → use path to `python.exe`  
   Example:
   ```
   Program/script: C:\Path\To\Python\python.exe  
   Add arguments: tracker.py  
   ```

---

## 📉 Sample Visualization

> ![Price Trend](images/price_trend.png)

---
