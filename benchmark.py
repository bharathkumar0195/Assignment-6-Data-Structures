"""Reproducible benchmarks; results depend on machine and Python version."""
import random
import time
from statistics import median
from selection_algorithms import median_of_medians, randomized_quickselect

def run():
    print('distribution,n,median_of_medians_ms,randomized_quickselect_ms')
    for n in (100, 1000, 5000):
        rng = random.Random(2026)
        base = [rng.randrange(n*2) for _ in range(n)]
        for name, values in [('random',base),('sorted',sorted(base)),('reverse',sorted(base,reverse=True))]:
            times = []
            for fn in (median_of_medians, randomized_quickselect):
                trials = []
                for _ in range(5):
                    start = time.perf_counter()
                    answer = fn(values, (n+1)//2)
                    trials.append((time.perf_counter()-start)*1000)
                    assert answer == sorted(values)[(n+1)//2-1]
                times.append(median(trials))
            print(f'{name},{n},{times[0]:.4f},{times[1]:.4f}')
if __name__ == '__main__': run()
