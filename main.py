
from data_loader import load_market_data_csv
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from profiler import benchmark
from reporting import plot

SIZES = [1_000, 10_000, 100_000]


def main():
    data = load_market_data_csv("market_data.csv")

    strategies = {
        "Naive": NaiveMovingAverageStrategy,
        "Windowed": lambda: WindowedMovingAverageStrategy(10),
    }

    results = {}

    for name, ctor in strategies.items():
        results[name] = []
        for n in SIZES:
            strat = ctor()
            metrics = benchmark(strat, data[:n])
            results[name].append(metrics)
            print(name, n, metrics)

    plot(results, "runtime_scaling.png")



if __name__ == "__main__":
    main()
