"""Assignment 6: deterministic and randomized kth-smallest selection (k is 1-based)."""
import random

def median_of_medians(values, k):
    if not 1 <= k <= len(values):
        raise ValueError('k must be between 1 and len(values)')
    if len(values) <= 5:
        return sorted(values)[k - 1]
    medians = [sorted(values[i:i+5])[len(values[i:i+5])//2] for i in range(0, len(values), 5)]
    pivot = median_of_medians(medians, (len(medians)+1)//2)
    lows = [x for x in values if x < pivot]
    equals = [x for x in values if x == pivot]
    highs = [x for x in values if x > pivot]
    if k <= len(lows):
        return median_of_medians(lows, k)
    if k <= len(lows) + len(equals):
        return pivot
    return median_of_medians(highs, k - len(lows) - len(equals))

def randomized_quickselect(values, k, rng=None):
    if not 1 <= k <= len(values):
        raise ValueError('k must be between 1 and len(values)')
    rng = rng or random.Random()
    a = list(values)
    while True:
        if len(a) == 1:
            return a[0]
        pivot = rng.choice(a)
        low = [x for x in a if x < pivot]
        equal = [x for x in a if x == pivot]
        high = [x for x in a if x > pivot]
        if k <= len(low):
            a = low
        elif k <= len(low) + len(equal):
            return pivot
        else:
            k -= len(low) + len(equal)
            a = high

if __name__ == '__main__':
    sample = [9, 2, 2, 7, 5, 1]
    for k in range(1, len(sample)+1):
        assert median_of_medians(sample, k) == sorted(sample)[k-1]
        assert randomized_quickselect(sample, k) == sorted(sample)[k-1]
    print('Selection tests passed.')
