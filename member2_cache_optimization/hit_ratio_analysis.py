"""
Hit Ratio Analysis
"""

import matplotlib.pyplot as plt


def calculate_hit_ratio(total_requests, hits):

    return hits / total_requests


def plot_hit_ratio(results):

    methods = list(results.keys())
    ratios = list(results.values())

    plt.bar(methods, ratios)

    plt.title("Cache Hit Ratio Comparison")

    plt.xlabel("Algorithm")
    plt.ylabel("Hit Ratio")

    plt.show()