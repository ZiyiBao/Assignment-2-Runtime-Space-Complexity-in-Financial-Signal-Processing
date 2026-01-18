

import time
import tracemalloc
from dataclasses import dataclass
from typing import List
from models import MarketDataPoint, Strategy


@dataclass
class Metrics:
    n: int
    runtime: float
    peak_kb: float


def run(strategy: Strategy, ticks: List[MarketDataPoint]):
    for t in ticks:
        strategy.generate_signals(t)


def benchmark(strategy: Strategy, ticks: List[MarketDataPoint]) -> Metrics:
    tracemalloc.start()
    start = time.perf_counter()

    run(strategy, ticks)

    end = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return Metrics(len(ticks), end - start, peak / 1024)
