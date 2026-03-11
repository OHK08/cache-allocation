CACHE_LATENCY = 5
NETWORK_LATENCY = 50


def compute_latency(hit_ratio):

    return (
        hit_ratio * CACHE_LATENCY +
        (1 - hit_ratio) * NETWORK_LATENCY
    )