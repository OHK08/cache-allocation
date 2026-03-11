import matplotlib.pyplot as plt


def plot_hit_ratio(results):

    algorithms = list(results.keys())
    values = list(results.values())

    plt.figure()

    plt.bar(algorithms, values)

    plt.title("Cache Hit Ratio Comparison")
    plt.ylabel("Hit Ratio")

    plt.show()


def plot_cache_size_vs_hit_ratio(simulation_func, requests):

    cache_sizes = [5, 10, 15, 20]

    lru = []
    lfu = []

    for size in cache_sizes:

        results = simulation_func(requests, size)

        lru.append(results["LRU"])
        lfu.append(results["LFU"])

    plt.figure()

    plt.plot(cache_sizes, lru, label="LRU")
    plt.plot(cache_sizes, lfu, label="LFU")

    plt.xlabel("Cache Size")
    plt.ylabel("Hit Ratio")

    plt.title("Cache Size vs Hit Ratio")

    plt.legend()

    plt.show()



def plot_hit_ratio(results):

    algorithms = list(results.keys())
    values = list(results.values())

    plt.figure()
    plt.bar(algorithms, values)

    plt.title("Cache Hit Ratio Comparison")
    plt.ylabel("Hit Ratio")

    plt.show()


def plot_latency(latencies):

    algorithms = list(latencies.keys())
    values = list(latencies.values())

    plt.figure()
    plt.bar(algorithms, values)

    plt.title("Average Latency Comparison")
    plt.ylabel("Latency (ms)")

    plt.show()