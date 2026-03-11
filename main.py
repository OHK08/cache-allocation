import json

from member3_simulation.simulation_engine import run_cache_comparison
from member3_simulation.plots import plot_hit_ratio, plot_latency
from member3_simulation.performance_metrics import compute_latency


def main():

    with open("data/requests.json") as f:
        requests = json.load(f)

    results = run_cache_comparison(requests)

    print("Hit Ratios:", results)

    latencies = {
        algo: compute_latency(hr)
        for algo, hr in results.items()
    }

    print("Latencies:", latencies)

    plot_hit_ratio(results)
    #plot_hit_ratio(results) 
    plot_latency(latencies)


if __name__ == "__main__":
    main()