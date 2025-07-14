import pandas as pd
import matplotlib.pyplot as plt

# Load historical data
df = pd.read_csv("banana_price_history.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Show available products
print("Available products:\n", df["Product"].unique())

# Choose product to visualize
product_name = input("Enter product name to visualize: ").strip()
product_df = df[df["Product"] == product_name]

if product_df.empty:
    print("❌ Product not found.")
else:
    plt.figure(figsize=(5, 5)) 
    plt.plot(product_df["Timestamp"], product_df["Price"], marker='o')
    plt.title(f"Price Trend: {product_name}")
    plt.xlabel("Time")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
