import numpy as np
import json
import random


def generate_random_requests(content_ids, num_requests=1000):
    requests = [random.choice(content_ids) for _ in range(num_requests)]
    return requests


def generate_zipf_requests(content_ids, num_requests=1000, alpha=1.2):
    n = len(content_ids)

    zipf_dist = np.random.zipf(alpha, num_requests)
    zipf_dist = [content_ids[i % n] for i in zipf_dist]

    return zipf_dist


def save_requests(requests, filename="../data/requests.json"):
    with open(filename, "w") as f:
        json.dump(requests, f)


if __name__ == "__main__":

    content_ids = list(range(50))   # assume 50 items

    req = generate_zipf_requests(content_ids, 1000)

    save_requests(req)

    print("Requests generated and saved.")