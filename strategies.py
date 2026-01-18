
from collections import deque
from typing import Dict, List
from models import MarketDataPoint, Signal, Strategy


class NaiveMovingAverageStrategy(Strategy):
    """
    Time:
      - per tick: O(t)
      - total: O(n^2)
    Space: O(n)
    """

    def __init__(self):
        self.history: Dict[str, List[float]] = {}

    def generate_signals(self, tick: MarketDataPoint) -> List[Signal]:
        prices = self.history.setdefault(tick.symbol, [])
        prices.append(tick.price)

        ma = sum(prices) / len(prices)

        if tick.price > ma:
            return [Signal(tick.timestamp, tick.symbol, "BUY", tick.price, ma)]
        elif tick.price < ma:
            return [Signal(tick.timestamp, tick.symbol, "SELL", tick.price, ma)]
        return []


class WindowedMovingAverageStrategy(Strategy):
    """
    Time:
      - per tick: O(1)
      - total: O(n)
    Space: O(k)
    """

    def __init__(self, window_size=10):
        self.k = window_size
        self.buffers = {}
        self.sums = {}

    def generate_signals(self, tick: MarketDataPoint) -> List[Signal]:
        buf = self.buffers.setdefault(tick.symbol, deque())
        total = self.sums.get(tick.symbol, 0.0)

        buf.append(tick.price)
        total += tick.price

        if len(buf) > self.k:
            total -= buf.popleft()

        self.sums[tick.symbol] = total
        ma = total / len(buf)

        if tick.price > ma:
            return [Signal(tick.timestamp, tick.symbol, "BUY", tick.price, ma)]
        elif tick.price < ma:
            return [Signal(tick.timestamp, tick.symbol, "SELL", tick.price, ma)]
        return []
