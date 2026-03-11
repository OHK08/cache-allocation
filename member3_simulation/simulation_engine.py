import json
import random

from member2_cache_optimization.lru_lfu_comparison import compare
from member2_cache_optimization.cache_placement import (
    greedy_cache_placement,
    dp_cache_placement
)

CACHE_CAPACITY = 10


def run_cache_comparison(requests):

    results = compare(requests, CACHE_CAPACITY)

    lru_hits = results["LRU Hits"]
    lfu_hits = results["LFU Hits"]

    total = len(requests)

    return {
        "LRU": lru_hits / total,
        "LFU": lfu_hits / total
    }


def run_cache_placement(contents):

    greedy = greedy_cache_placement(contents, CACHE_CAPACITY)
    dp = dp_cache_placement(contents, CACHE_CAPACITY)

    return {
        "Greedy": len(greedy),
        "Knapsack": len(dp)
    }


if __name__ == "__main__":

    with open("data/requests.json") as f:
        requests = json.load(f)

    with open("data/content_list.json") as f:
        contents = json.load(f)

    cache_results = run_cache_comparison(requests)
    placement_results = run_cache_placement(contents)

    print("Hit Ratios:", cache_results)
    print("Placement Results:", placement_results)