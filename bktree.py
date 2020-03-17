''' BKTree Implementation'''


from collections.abc import MutableMapping

__all__ = ['Node', 'BKTree', 'hamming_distance']

def hamming_distance(a, b):
    return sum([1 for a,b in zip(a,b) if a!=b])

class Node(MutableMapping):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.mapping = {}

    def __len__(self):
        return len(self.mapping)

    def __iter__(self):
        return iter(self.mapping)

    def __setitem__(self, key, value):
        self.mapping[key] = value 

    def __getitem__(self, key):
        return self.mapping[key]

    def __delitem__(self, key):
        del self.mapping[key]

class BKTree:
    def __init__(self, func):
        self.root = None
        self._distance = func 

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return

        current = self.root
        while True:
            distance = self._distance(current.key, key)
            if distance in current:
                current = current[distance]
            else:
                current[distance] = Node(key, value)
                break
         
    def search(self, key, radius):
        remaining, results = [self.root], []
        while remaining:
            node = remaining.pop()
            distance = self._distance(node.key, key)
            if distance <= radius:
                results.append(node)
            remaining.extend([
                child for child_distance, child in node.items()
                if distance-radius <= child_distance <= distance+radius
            ])
        return results

if __name__ == '__main__':
    pass
