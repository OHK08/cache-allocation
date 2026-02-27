# graph_model.py

import config

# ===============================
# Node Definitions
# ===============================

EDGE = "EDGE"
REGIONAL1 = "REGIONAL1"
REGIONAL2 = "REGIONAL2"
CLOUD1 = "CLOUD1"
CLOUD2 = "CLOUD2"

nodes = [EDGE, REGIONAL1, REGIONAL2, CLOUD1, CLOUD2]

# ===============================
# Edge Definitions
# (Latency, Bandwidth, Energy)
# ===============================

network_links = {
    (EDGE, REGIONAL1): {"latency": 10, "bandwidth": 5, "energy": 4},
    (EDGE, REGIONAL2): {"latency": 15, "bandwidth": 6, "energy": 5},
    (REGIONAL1, CLOUD1): {"latency": 20, "bandwidth": 8, "energy": 7},
    (REGIONAL2, CLOUD2): {"latency": 18, "bandwidth": 7, "energy": 6},
    (REGIONAL1, REGIONAL2): {"latency": 12, "bandwidth": 6, "energy": 5},
}

# Convert to undirected graph
def build_graph():
    graph = {node: {} for node in nodes}

    for (u, v), metrics in network_links.items():
        cost = (
            config.alpha * metrics["latency"]
            + config.beta * metrics["bandwidth"]
            + config.gamma * metrics["energy"]
        )

        graph[u][v] = cost
        graph[v][u] = cost

    return graph