import timeit
import time2colour
from datetime import datetime

def benchmark():
    t = datetime(2023, 10, 27, 12, 34, 56)

    # Benchmark get_colours_for_time
    time_taken = timeit.timeit(lambda: time2colour.get_colours_for_time(t), number=100000)
    print(f"get_colours_for_time (100,000 calls): {time_taken:.4f} seconds")

    # Benchmark individual functions with varying inputs
    def test_all_variants():
        for h in range(24):
            time2colour.get_colour_12(h)
        for m in range(60):
            time2colour.get_colour_60(m)

    time_taken_variants = timeit.timeit(test_all_variants, number=1000)
    print(f"All variants (1,000 iterations of 24h + 60m): {time_taken_variants:.4f} seconds")

if __name__ == "__main__":
    benchmark()
