"""
LRU and LFU Cache comparison
"""

from collections import defaultdict, OrderedDict


# -----------------------
# LRU Cache
# -----------------------

class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = OrderedDict()
        self.hits = 0


    def request(self, key):

        if key in self.cache:

            self.cache.move_to_end(key)
            self.hits += 1

        else:

            if len(self.cache) >= self.capacity:

                self.cache.popitem(last=False)

            self.cache[key] = True


# -----------------------
# LFU Cache
# -----------------------

class LFUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(int)
        self.hits = 0


    def request(self, key):

        if key in self.cache:

            self.freq[key] += 1
            self.hits += 1

        else:

            if len(self.cache) >= self.capacity:

                lfu = min(self.freq, key=self.freq.get)

                del self.cache[lfu]
                del self.freq[lfu]

            self.cache[key] = True
            self.freq[key] = 1


# -----------------------
# Comparison Function
# -----------------------

def compare(requests, capacity):

    lru = LRUCache(capacity)
    lfu = LFUCache(capacity)

    for r in requests:

        lru.request(r)
        lfu.request(r)

    return {

        "LRU Hits": lru.hits,
        "LFU Hits": lfu.hits
    }