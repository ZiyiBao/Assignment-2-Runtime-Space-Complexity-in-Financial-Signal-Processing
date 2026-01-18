
import csv
from datetime import datetime
from typing import List
from models import MarketDataPoint


def load_market_data_csv(path: str) -> List[MarketDataPoint]:
    """
    Time: O(n)
    Space: O(n)
    """
    data = []

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(
                MarketDataPoint(
                    timestamp=datetime.fromisoformat(row["timestamp"]),
                    symbol=row["symbol"],
                    price=float(row["price"])
                )
            )
    return data
