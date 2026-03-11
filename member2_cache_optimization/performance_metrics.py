"""
Calculate latency, bandwidth, and energy performance
"""

def calculate_metrics(requests, cache_contents, content_dict):

    total_latency = 0
    total_bandwidth = 0
    total_energy = 0


    for req in requests:

        content = content_dict[req]

        if req in cache_contents:

            level = 0

        else:

            level = 2


        total_latency += content["latency"][level]
        total_bandwidth += content["bandwidth"][level]
        total_energy += content["energy"][level]


    return {

        "Latency": total_latency,
        "Bandwidth": total_bandwidth,
        "Energy": total_energy
    }
