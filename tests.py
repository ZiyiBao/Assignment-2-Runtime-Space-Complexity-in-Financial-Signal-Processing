
from datetime import datetime
from models import MarketDataPoint
from strategies import WindowedMovingAverageStrategy


def test_windowed_strategy_runs():
    strat = WindowedMovingAverageStrategy(3)
    ticks = [
        MarketDataPoint(datetime.now(), "AAPL", p)
        for p in [1, 2, 3, 4]
    ]
    for t in ticks:
        strat.generate_signals(t)
