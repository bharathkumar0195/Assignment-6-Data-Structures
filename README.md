# Assignment 6 — Medians, Order Statistics and Elementary Data Structures

Course: MSCS-532-M70 | Student: Bharath Kumar Origanti

## Requirements
Python 3.9+; standard library only.

## Run
```bash
python selection_algorithms.py
python data_structures.py
python benchmark.py
```

`benchmark.py` prints a CSV table; to save it, run `python benchmark.py > results.csv`. Timing results will vary by machine.

## Contents
- `selection_algorithms.py`: Median of Medians (worst-case O(n)) and Randomized Quickselect (expected O(n)). `k` is one-based.
- `data_structures.py`: array, matrix, stack, queue and singly linked list implementations.
- `benchmark.py`: random, sorted and reverse-sorted input benchmarks.
- `results.csv`: measured sample run.
- `Assignment_6_Report.docx`: design, analysis, observations and applications.

## Summary
Both selection methods correctly handle duplicates. Randomized Quickselect was generally faster in this sample benchmark, while Median of Medians has a stronger worst-case guarantee.
