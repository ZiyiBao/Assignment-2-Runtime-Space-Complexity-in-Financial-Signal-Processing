
The figure above shows runtime as a function of input size for both strategies.

The NaiveMovingAverageStrategy exhibits super-linear growth. When the input
size increases by a factor of 10 (from 10k to 100k ticks), runtime increases
by more than 60x, which is consistent with O(n²) behavior caused by recomputing
the moving average from the full price history at each tick.

In contrast, the WindowedMovingAverageStrategy demonstrates approximately
linear scaling. Runtime increases proportionally with input size, consistent
with O(n) complexity, since each tick requires only constant-time deque
updates and running sum adjustments.