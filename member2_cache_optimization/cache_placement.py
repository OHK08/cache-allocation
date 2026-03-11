"""
Cache Placement using Greedy and Dynamic Programming
Objective:
Minimize weighted sum of latency, bandwidth, and energy.
"""

import numpy as np
from .knapsack import knapsack_01

# Adjustable weights
ALPHA = 0.5   # latency weight
BETA = 0.3    # bandwidth weight
GAMMA = 0.2   # energy weight


def compute_cost(content, cache_level):
    """
    cache_level:
    0 = edge
    1 = regional
    2 = cloud
    """

    latency = content["latency"][cache_level]
    bandwidth = content["bandwidth"][cache_level]
    energy = content["energy"][cache_level]

    return ALPHA * latency + BETA * bandwidth + GAMMA * energy


# ---------------------------
# Greedy Cache Placement
# ---------------------------

def greedy_cache_placement(contents, capacity):

    value_per_size = []

    for content in contents:

        cost_edge = compute_cost(content, 0)
        cost_cloud = compute_cost(content, 2)

        benefit = cost_cloud - cost_edge

        ratio = benefit / content["size"]

        value_per_size.append((ratio, content))


    value_per_size.sort(reverse=True, key=lambda x: x[0])

    selected = []
    used = 0

    for ratio, content in value_per_size:

        if used + content["size"] <= capacity:

            selected.append(content)
            used += content["size"]

    return selected


# ---------------------------
# Dynamic Programming Placement
# ---------------------------

def dp_cache_placement(contents, capacity):

    values = []
    weights = []

    for content in contents:

        cost_edge = compute_cost(content, 0)
        cost_cloud = compute_cost(content, 2)

        benefit = cost_cloud - cost_edge

        values.append(benefit)
        weights.append(content["size"])

    selected_indices = knapsack_01(values, weights, capacity)

    selected = [contents[i] for i in selected_indices]

    return selected