import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv("banana_price_history.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])


df["Price"] = df["Price"].str.replace("Price:", "").str.replace("₹", "").str.strip()
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")


print("Available products:\n", df["Product"].unique())


product_name = input("Enter product name to visualize: ").strip()
product_df = df[df["Product"] == product_name]

if product_df.empty:
    print("❌ Product not found.")
else:
    plt.figure(figsize=(10, 5))
    plt.plot(product_df["Timestamp"], product_df["Price"], color='green', marker='o')


    for x, y in zip(product_df["Timestamp"], product_df["Price"]):
        if pd.notna(y):
            plt.text(x, y, f"₹{y:.2f}", fontsize=8, ha='right', va='bottom')

    plt.title(f"Price Trend Over Time: {product_name}")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.grid(True)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()
