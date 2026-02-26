from cache_placement import greedy_cache_placement
import json


with open("../data/content_list.json") as f:

    contents = json.load(f)


capacity = 30

selected = greedy_cache_placement(contents, capacity)

print("Selected contents:")

for c in selected:

    print(c["id"])