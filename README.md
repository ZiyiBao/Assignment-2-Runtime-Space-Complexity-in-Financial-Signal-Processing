Runtime & Space Complexity in Financial Signal Processing
Overview:

This project compares two moving average trading strategies to analyze how
algorithmic design choices affect runtime and memory usage. 

Data:

Market data is synthetically generated to control input size and isolate
algorithmic performance.

To generate the dataset:

python generate_data.py


The generated market_data.csv includes the following columns:

timestamp
symbol
price

Strategies:

NaiveMovingAverageStrategy:

Time complexity: O(n²)

Space complexity: O(n)

Recomputes the moving average from the full price history at each tick.


WindowedMovingAverageStrategy:

Time complexity: O(n)

Space complexity: O(k)

Maintains a fixed-size rolling window with a running sum.

Profiling:

Runtime and memory usage were measured using:

time.perf_counter

tracemalloc

Benchmarks were run on:

1,000 ticks

10,000 ticks

100,000 ticks



Results：

Naive 1000 Metrics(n=1000, runtime=0.0048022999544627964, peak_kb=8.9453125)

Naive 10000 Metrics(n=10000, runtime=0.10876189998816699, peak_kb=228.076171875)

Naive 100000 Metrics(n=100000, runtime=7.194273700006306, peak_kb=927.859375)

Windowed 1000 Metrics(n=1000, runtime=0.0036146999918855727, peak_kb=2.0703125)

Windowed 10000 Metrics(n=10000, runtime=0.038250700046774, peak_kb=146.732421875)

Windowed 100000 Metrics(n=100000, runtime=0.34865189995616674, peak_kb=147.884765625)


The naive strategy exhibits super-linear runtime growth, while the windowed
strategy scales approximately linearly. At 100,000 ticks, the optimized
strategy runs under 1 second with low memory usage.


Visualization and result:
runtime_scaling.png
complexity_report.md

How to Run:
generate_data.py
main.py

Tests:
tests.py



