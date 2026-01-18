
import csv
import random
from datetime import datetime, timedelta

N = 100_000
symbol = "AAPL"
start_time = datetime(2025, 1, 1, 9, 30)
price = 100.0

with open("market_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "symbol", "price"])

    for i in range(N):
        price += random.uniform(-0.5, 0.5)
        writer.writerow([
            (start_time + timedelta(seconds=i)).isoformat(),
            symbol,
            round(price, 2)
        ])


