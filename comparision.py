import json
import matplotlib.pyplot as plt

from member2_cache_optimization.lru_lfu_comparison import compare
from member2_cache_optimization.cache_placement import (
    greedy_cache_placement,
    dp_cache_placement
)

# -------------------------------
# LOAD DATA
# -------------------------------
CACHE_CAPACITY = 10

with open("data/requests.json") as f:
    requests = json.load(f)

with open("data/content_list.json") as f:
    contents = json.load(f)

# -------------------------------
# LRU vs LFU
# -------------------------------
results = compare(requests, CACHE_CAPACITY)
total = len(requests)

lru_hr = results["LRU Hits"] / total
lfu_hr = results["LFU Hits"] / total

# -------------------------------
# LATENCY
# -------------------------------
CACHE_LATENCY = 5
NETWORK_LATENCY = 50

lru_latency = lru_hr * CACHE_LATENCY + (1 - lru_hr) * NETWORK_LATENCY
lfu_latency = lfu_hr * CACHE_LATENCY + (1 - lfu_hr) * NETWORK_LATENCY

# -------------------------------
# CACHE PLACEMENT
# -------------------------------
greedy = greedy_cache_placement(contents, CACHE_CAPACITY)
dp = dp_cache_placement(contents, CACHE_CAPACITY)

# -------------------------------
# PRINT RESULTS
# -------------------------------
print("\n===== CACHE PERFORMANCE COMPARISON =====\n")

print("LRU Hit Ratio:", round(lru_hr, 3))
print("LFU Hit Ratio:", round(lfu_hr, 3))

print("\nCache Placement:")
print("Greedy selected:", len(greedy))
print("Knapsack selected:", len(dp))

print("\nLatency:")
print("LRU:", round(lru_latency, 2))
print("LFU:", round(lfu_latency, 2))

print("\n=======================================")

# -------------------------------
# GRAPH 1: Hit Ratio
# -------------------------------
plt.figure()
plt.bar(["LRU", "LFU"], [lru_hr, lfu_hr])
plt.title("Hit Ratio Comparison")
plt.ylabel("Hit Ratio")
plt.show()

# -------------------------------
# GRAPH 2: Latency
# -------------------------------
plt.figure()
plt.bar(["LRU", "LFU"], [lru_latency, lfu_latency])
plt.title("Latency Comparison")
plt.ylabel("Latency (ms)")
plt.show()

# -------------------------------
# GRAPH 3: Cache Placement
# -------------------------------
plt.figure()
plt.bar(["Greedy", "Knapsack"], [len(greedy), len(dp)])
plt.title("Cache Placement Comparison")
plt.ylabel("Items Selected")
plt.show()

# -------------------------------
# GRAPH 4: Cache Size vs Hit Ratio
# -------------------------------
sizes = [5, 10, 15, 20]
lru_list = []
lfu_list = []

for size in sizes:
    res = compare(requests, size)
    lru_list.append(res["LRU Hits"] / total)
    lfu_list.append(res["LFU Hits"] / total)

plt.figure()
plt.plot(sizes, lru_list, marker='o', label="LRU")
plt.plot(sizes, lfu_list, marker='o', label="LFU")
plt.title("Cache Size vs Hit Ratio")
plt.xlabel("Cache Size")
plt.ylabel("Hit Ratio")
plt.legend()
plt.show()

# -------------------------------
# MULTI-OBJECTIVE COMPARISON
# -------------------------------
from member1_network_graph.shortest_path import dijkstra
import member1_network_graph.config as config
from member1_network_graph.graph_model import EDGE


def run_strategy(alpha, beta, gamma):
    config.alpha = alpha
    config.beta = beta
    config.gamma = gamma

    result = dijkstra(EDGE)
    return sum(result.values())


latency_only = run_strategy(1, 0, 0)
bandwidth_only = run_strategy(0, 1, 0)
energy_only = run_strategy(0, 0, 1)
hybrid = run_strategy(0.5, 0.3, 0.2)

print("\n===== MULTI-OBJECTIVE COMPARISON =====")
print("Latency Only:", round(latency_only, 2))
print("Bandwidth Only:", round(bandwidth_only, 2))
print("Energy Only:", round(energy_only, 2))
print("Hybrid:", round(hybrid, 2))

# -------------------------------
# GRAPH 5: Multi-objective
# -------------------------------
labels = ["Latency", "Bandwidth", "Energy", "Hybrid"]
values = [latency_only, bandwidth_only, energy_only, hybrid]

plt.figure()
plt.bar(labels, values)
plt.title("Single vs Multi-Objective Comparison")
plt.ylabel("Total Cost")
plt.show()