# cost_functions.py

import config

def calculate_cost(latency, bandwidth, energy):
    """
    Multi-objective cost function:

    C = αL + βB + γE
    """
    return (
        config.alpha * latency
        + config.beta * bandwidth
        + config.gamma * energy
    )