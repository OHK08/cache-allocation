def compute_hit_ratio(hits, misses):

    total = hits + misses

    if total == 0:
        return 0

    return hits / total


def compute_latency(hit_ratio):

    cache_latency = 5
    network_latency = 50

    avg_latency = (hit_ratio * cache_latency) + ((1-hit_ratio) * network_latency)

    return avg_latency


def compute_bandwidth(misses):

    bandwidth_per_miss = 10

    return misses * bandwidth_per_miss


def compute_energy(misses):

    energy_per_fetch = 2

    return misses * energy_per_fetch