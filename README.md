# Algorithms & Data Structures · Python

Graph algorithms and a probabilistic data structure, from UCSB's CS 130A.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)

## Projects

### [Bloom filter study](BloomFilter)

Implemented a Bloom filter from scratch with two custom hash functions, then measured how the false-positive rate changes with the number of hash functions, comparing the two hash functions and the measured rate against the theoretical one. The [written report](BloomFilter/Bloom%20Filter%20Proj.pdf) walks through the experiments and plots.

### [Graph problems](Project%201)

| Script | Problem | Algorithm |
|---|---|---|
| [`10KindsOfPeople.py`](Project%201/10KindsOfPeople.py) | Given a grid map, answer "can these two cells reach each other?" for many queries | Label connected regions once with iterative DFS, then answer each query in O(1) |
| [`BuildDeps.py`](Project%201/BuildDeps.py) | Given build rules and a changed file, list everything that must be rebuilt, in order | Reverse the dependency graph and topologically sort with DFS |
| [`GrapeVine.py`](Project%201/GrapeVine.py) | Simulate how a rumor spreads through a social network over a number of days | Breadth-first spread with per-person skepticism thresholds |

Each script reads its input from standard input:

```bash
python3 "Project 1/BuildDeps.py" < input.txt
```
